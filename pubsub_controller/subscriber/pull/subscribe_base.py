# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

from google.cloud import pubsub_v1
from pubsub_controller.utils.log import log, error_log


class SubscribeBase(object):

    subscription = None
    end = False

    @classmethod
    def received_function(cls, message):
        """
        CallBack内で実行したい処理のAbstract Function
        :param message: Subscribeしたメッセージ
        """
        pass

    @classmethod
    def close(cls, end=False):
        """
        future.result()しているのをcloseして処理終了させる
        """
        cls.end = end
        cls.subscription.close()

    @classmethod
    def pull(cls, subscription_name):
        """
        Pullリクエストを行い、メッセージをSubscribeする。
        callbackメソッドにてメッセージの正常応答と、メッセージに対応した処理を行う。
        :param subscription_name: "projects/"から始まるSubscription名称
        """

        while not cls.end:
            # SubscriberClientを作成
            subscriber = pubsub_v1.SubscriberClient()

            # MessageをPull出来たら実行されるCallBack
            def callback(message):
                log('Received message: {}'.format(message))
                message.ack()
                # メッセージ受信後処理をCall
                cls.received_function(message)

            # Subscriber
            flow_control = pubsub_v1.types.FlowControl()
            cls.subscription = subscriber.subscribe(subscription_name, flow_control=flow_control)
            # Open the subscription, passing the callback.
            future = cls.subscription.open(callback)

            log('Listening for messages on {}'.format(subscription_name))

            try:
                # Publisherのメッセージを待ち受ける(ブロッキングされる)
                future.result()
                log('Closed for messages on {}'.format(subscription_name))
            except KeyboardInterrupt:
                log('Stopped Subscribe on {}'.format(subscription_name))
                cls.subscription.close()
            except Exception as e:
                error_log('subscription error. detail = {}'.format(e))
                cls.subscription.close()
