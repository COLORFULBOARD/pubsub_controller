# Pub/Sub Controller

## Description
GCP Pub/SubのSubscriptionを定期的にFetchし、メッセージがあればメッセージ内のキーで指定されたスクリプトを実行する。

## Usage
- Settings<br>
`python setup.py install` でセットアップを開始します。<br>
    - GCP PROJECT ID<br>
    GCPのProjectIDを指定
    - SUBSCRIPTION ID<br>
    このProjectで使用するSubscriptionIDを指定<br>
    例) Subscription nameが`projects/hoge-project/subscriptions/fuga`の場合は`fuga`を指定
    - Interval Second<br>
    SubscriptionをFetchする間隔(秒)<br>

- Subscriber<br>
`apps/subscriber/pull/exec_classes/exec_sample.py`<br>
を参考に、所定のmainメソッドを定義したModuleを作成すると、<br>
Setup時に`SUBSCRIPTION ID`で指定したSubscriptionに来たメッセージに含まれる<br>
{target: ModuleName} のModuleNameを実行します。

- Pull Subscriber<br>
SubscriptionをPullする常駐プロセス。
    - config<br>
    Pull Subscriberは常駐プロセスとして動作するため、<br>
    参考までにsupervisorのconfigファイルを作成しています。
    
- Publisher<br>
CLIまたはPythonスクリプトから実行し、指定のtopicへメッセージをPublishする。
    - Exec on CommandLine
        - `python cli_publish.py -t test-topic -m test_data -a\ `<br>`'{"target":"exec_sample","text":"test_text"}'`<br>
            - arguments
                - `-t = topic name`
                - `-m = message data`
                - `-a = (Optional) message attribute`
    - Exec on PythonCode
        ```python
        from apps.publisher.publish_message import publish
        publish('test-topic', 'test_data', {'target':'exec_sample','text':'test_text'})
        ```
## Try to this sample.
0. Create Pub/Sub topic and subscription on GCP. (ex: test-topic/test-sub)
1. `git clone https://github.com/COLORFULBOARD/pubsub_controller.git`
2. `cd pubsub_controller`
3. `pipenv install`
4. `python setup.py install`
5. ``export PYTHONPATH= `pwd` ``
6. `python apps/subscriber/pull/pull_subscriber.py`
7. Open Another Terminal Window.
8. ``export PYTHONPATH= `pwd` ``
9. `python cli_publish.py -t test -m test_data -a '{"target":"exec_sample","text":"test_text"}'`
10. In the Subscriber's window you will see the contents of the message you just published!

## Option
- Custom Subscriber
    1. 新たにSubscriberを定義する場合は、
    `apps/subscriber/pull/subscribe_base.py`<br>
    を継承し、<br>
    `received_function`をオーバーライドしたClassを作成して下さい。
    2. `apps/subscriber/pull/pull_subscriber.py`に<br>
    ```CustomSubscriber.pull(SUBSCRIPTION_NAME.format(unique='unique_key'))```<br>
    を実行するメソッドを作成し、`pull_subscriber.py`の`threads`にメソッドをappendして下さい。
    3. `pull_subscriber.py`の```subscriber_all_close```に<br>
    ```CustomSubscriber.close(end)```メソッドを追加して下さい。