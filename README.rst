Pub/Sub Controller
==================

Description
-----------

Fetch the Subscription of the GCP Pub/Sub regularly, and if there is a
message execute the script specified by the key in the message.


GCP Pub/SubのSubscriptionを定期的にFetchし、
メッセージがあればメッセージ内のキーで指定されたスクリプトを実行する。

Installation and Try to this sample.
------------------------------------

#. Create Pub/Sub topic and subscription on GCP. (ex: test-topic/test-sub)
#. ``pip install pubsub_controller``
#. ``pubsub-init`` and input your Pub/Sub setting. (ex: GCP_PROJECT_ID=your project id / SUBSCRIPTION_ID=test-sub)
#. ``subscribe``
#. Subscriber will start immediately.
#. Open Another Terminal Window.
#. ``publish -t test-topic -m test_data -a '{"target":"exec_sample","text":"test_text"}'``
#. In the Subscriber’s window you will see the contents of the message you just published!

Installation and Try to this sample.
------------------------------------

1. Create a new python file under "exec_classes" directory.

    - The same Python filename as the name specified by the attribute "target" key of the message to be published is executed.

2. Implement ``def main (message_data, message_attr)`` and describe what you want to do after receiving the message.

    - "message_data" contains the contents of the received message.
    - "message_attr" contains optional attributes of the received message.

Details
-------

-  Settings ``pubsub_controller/settings.py`` Required parameters are
   set here. (It is set automatically by the ``pubsub-init`` command)

   -  GCP PROJECT ID Your GCP ProjectID
   -  SUBSCRIPTION ID Enter the Subscription ID to be used. If the
      Subscription name is ``projects/hoge-project/subscriptions/fuga``,
      please enter ``fuga``.
   -  Interval Second Enter the interval to fetch Subscription in
      seconds.

-  Subscriber If you need a new subscriber, please refer to
   ``apps/subscriber/pull/exec_classes/exec_sample.py`` and create it.

-  Pull Subscriber This is a resident process that pulls Subscription.

   -  config For reference, I am creating a supervisor config file.
      ``apps/subscriber/pull/config/pull_subscriber.ini``

-  Publisher Execute from the CLI or Python script and publish the
   message to the topic.

   -  Exec on CommandLine

      - ``python cli_publish.py -t test-topic -m test_data -a '{"target":"exec_sample","text":"test_text"}'``

      -  arguments

         -  ``-t = topic name``
         -  ``-m = message data``
         -  ``-a = (Optional) message attribute``

   -  Exec on PythonCode

      .. code-block:: python

         from apps.publisher.publish_message import publish

         publish('test-topic', 'test_data', {'target':'exec_sample','text':'test_text'})
