# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import threading
import signal
import time

from pubsub_controller.settings import (
    GCP_PROJECT_ID,
    POLLING_TIME,
    SUBSCRIPTION_ID,
)
from pubsub_controller.utils.log import log, error_log
from pubsub_controller.subscriber.pull.subscribe_multi import SubscribeMulti

SUBSCRIPTION_NAME = 'projects/' + GCP_PROJECT_ID + '/subscriptions/{unique}'


def subscribe_multi():
    """
    メッセージを受け取って指定されたClassを実行する
    Pub/subメッセージのattributeに {target: ClassName} を指定すると、
    ClassNameのmainメソッドを実行する。
    """
    SubscribeMulti.pull(SUBSCRIPTION_NAME.format(unique=SUBSCRIPTION_ID))


def subscriber_all_close(end=False):
    """
    全てのSubscriberをCloseする。
    """
    SubscribeMulti.close(end)


def sync_stop_subscriber(end=False):
    """
    全てのSubscriberを停止する。(同期)
    :param end: Subscriberを完全に終了するかどうか。
    """
    t = threading.Thread(target=subscriber_all_close, args=(end,))
    t.start()
    t.join(timeout=60)


def main():
    """
    常駐プロセスとして起動する。
    指定されたSubscriberをThreadとして起動する。 
    """
    log('Start Pull Subscriber.')

    def signal_handler(signum, stack):
        """
        受け取ったSIGNALに応じて終了処理をハンドリングする。
        :param signum: default
        :param stack: default
        """
        sync_stop_subscriber(end=True)
        log('Stop Pull Subscriber. signal by {}'.format(signum))
        exit(0)

    # SIGNALに応じたハンドリング
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    threads = []

    try:
        threads.append(subscribe_multi)

        for thread in threads:
            t = threading.Thread(target=thread)
            t.start()

        # 定期的にSubscriberClose -> Openを繰り返す
        while True:
            time.sleep(POLLING_TIME)
            sync_stop_subscriber()

    except Exception as e:
        error_log('Error Pull Subscriber. ... {}'.format(e))
        exit(1)

if __name__ == '__main__':
    main()
