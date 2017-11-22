# Pub/Sub Controller

## Description
GCP Pub/Subを使いやすくするためのModule。

## Usage
- Settings<br>
`setting.py`の内容を環境に合わせて編集します。<br>
    - GCP_PROJECT_ID<br>
    GCPのProjectIDを指定します。
    - SUBSCRIBE_MULTI_KEY<br>
    このProjectで汎用的に使用するSubscriptionKeyを指定します。

- Subscriber<br>
`apps/subscriber/pull/exec_classes/exec_sample.py`<br>
を参考に、mainメソッドを定義したModuleを作成すると、<br>
`SUBSCRIBE_MULTI_KEY`で指定したSubscriptionに来たメッセージの<br>
{target: ModuleName} で指定されたModuleを実行します。

- Pull Subscriber<br>
SubscriptionをPullする常駐プロセス。
    - config<br>
    Pull Subscriberは常駐プロセスとして動作するため、<br>
    参考までにsupervisorのconfigファイルを作成しています。
    
- Publisher<br>
    - Exec on CommandLine
        - `python cli_publish.py -t test-topic -m test_data -a '{"target":"exec_sample","text":"test_text"}'`<br>
            - `-t = topic name`
            - `-m = message data`
            - `-a = (Optional) message attribute`
    - Exec on PythonCode
        ```python
        from apps.publisher.publish_message import publish
        publish('test-topic', 'test_data', {'target':'exec_sample','text':'test_text'})
        ```

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