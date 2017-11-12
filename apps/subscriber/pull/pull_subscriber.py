# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import threading
import signal
import time

from settings import GCP_PROJECT_ID
from apps.utils.log import log, error_log
from apps.subscriber.pull.gunicorn_restart import GunicornRestart

SUBSCRIPTION_NAME = 'projects/' + GCP_PROJECT_ID + '/subscriptions/{unique}'


def gunicorn_restart():
    """
    メッセージを受け取ってgunicorn restartする。
    *** Subscriberを増やす際はこのようなメソッドを追加し、メインのthreadsにappendする。 ***
    """
    GunicornRestart.pull(SUBSCRIPTION_NAME.format(unique='unique_key'))


def subscriber_all_close():
    """
    全てのSubscriberをCloseする。
    *** Subscriberを増やした際は追加する。 ***
    """
    GunicornRestart.close()


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
        t = threading.Thread(target=subscriber_all_close)
        t.start()
        t.join(timeout=60)
        log('Stop Pull Subscriber. signal by {}'.format(signum))
        exit(0)


    # SIGNALに応じたハンドリング
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    threads = []

    try:
        # threadsに格納されているメソッド分、daemonを作成する。
        threads.append(gunicorn_restart)

        for thread in threads:
            t = threading.Thread(target=thread)
            t.daemon = True
            t.start()

        # プロセスを常駐させる
        while True:
            time.sleep(10)

    except Exception as e:
        error_log('Error Pull Subscriber. ... {}'.format(e))
        exit(1)

if __name__ == '__main__':
    main()
