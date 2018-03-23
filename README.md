# Pub/Sub Controller

## Description
Fetch the Subscription of the GCP Pub/Sub regularly, and if there is a message execute the script specified by the key in the message.<br><br>
GCP Pub/SubのSubscriptionを定期的にFetchし、メッセージがあればメッセージ内のキーで指定されたスクリプトを実行する。

## Installation and Try to this sample.
1. Create Pub/Sub topic and subscription on GCP. (ex: test-topic/test-sub)
2. `pip install pubsub_controller`
3. `psc init` and input your Pub/Sub setting<br>(ex: GCP_PROJECT_ID=your project id / SUBSCRIPTION_ID=test-sub)
4. `psc subscribe`
5. Subscriber will start immediately.
6. Open Another Terminal Window.
7. `psc publish test test-message '{"target":"exec_sample","text":"test_text"}'`
8. In the Subscriber's window you will see the contents of the message you just published!

## How to add running process when message received.
1. Create a new python file under "exec_classes" directory.
- The same Python filename as the name specified by the attribute "target" key of the message to be published is executed.
2. Implement `def main (message_data, message_attr)` and describe what you want to do after receiving the message.
- "message_data" contains the contents of the received message.
- "message_attr" contains optional attributes of the received message.

## Details
- Settings<br>
`pubsub_controller/settings.py` Required parameters are set here.<br>
(It is set automatically by the `psc init` command)<br>
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
        - `psc publish test test-message '{"target":"exec_sample","text":"test_text"}'`<br>
            - arguments
                - `arg1 = topic name`
                - `arg2 = message data`
                - `arg3 = message attribute(json format)`
    - Exec on PythonCode
        ```python
        from apps.publisher.publish_message import publish
        publish('test-topic', 'test_data', {'target':'exec_sample','text':'test_text'})
        ```
