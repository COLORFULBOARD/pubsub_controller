# Pub/Sub Controller

## Description
Fetch the Subscription of the GCP Pub/Sub regularly, and if there is a message execute the script specified by the key in the message.<br><br>
GCP Pub/SubのSubscriptionを定期的にFetchし、メッセージがあればメッセージ内のキーで指定されたスクリプトを実行する。

## Installation and Try to this sample.
0. Create Pub/Sub topic and subscription on GCP. (ex: test-topic/test-sub)
1. `pip install pubsub_controller`
2. `pubsub-init` and input your Pub/Sub setting<br>(ex: GCP_PROJECT_ID=your project id / SUBSCRIPTION_ID=test-sub)
3. `subscribe`
4. Subscriber will start immediately.
5. Open Another Terminal Window.
6. `publish -t test-topic -m test_data -a '{"target":"exec_sample","text":"test_text"}'`
7. In the Subscriber's window you will see the contents of the message you just published!

## Details
- Settings<br>
`pubsub_controller/settings.py` Required parameters are set here.<br>
(It is set automatically by the `pubsub-init` command)<br>
    - GCP PROJECT ID<br>
    Your GCP ProjectID
    - SUBSCRIPTION ID<br>
    Enter the Subscription ID to be used.<br>
    If the Subscription name is `projects/hoge-project/subscriptions/fuga`, please enter `fuga`.
    - Interval Second<br>
    Enter the interval to fetch Subscription in seconds.<br>

- Subscriber<br>
If you need a new subscriber, please refer to `apps/subscriber/pull/exec_classes/exec_sample.py` and create it.

- Pull Subscriber<br>
This is a resident process that pulls Subscription.
    - config<br>
    For reference, I am creating a supervisor config file.<br>
    `apps/subscriber/pull/config/pull_subscriber.ini`

- Publisher<br>
Execute from the CLI or Python script and publish the message to the topic.
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
