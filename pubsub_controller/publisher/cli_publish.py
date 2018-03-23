# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import json
import argparse
from pubsub_controller.utils.log import log
from pubsub_controller.publisher.publish_message import publish

def main():
    """CLIから起動し、指定されたメッセージをPublishする
    :param -t: topic name to publish
    :param -m: publish message
    :param -a: (optional) message attribute of json format

    """
    parser = argparse.ArgumentParser(
        prog='publish_message.py',
        usage='Exec on terminal.',
        add_help=True,
    )
    parser.add_argument('-t', '--topic', help='topic name', required=True, type=str)
    parser.add_argument('-m', '--message', help='message data', required=True, type=str)
    parser.add_argument('-a', '--attr', help='(optional) message attribute of json format', type=json.loads)

    args = parser.parse_args()
    log('Argument : {}'.format(args))
    message_attr = args.attr if args.attr else {}

    publish(topic_name=args.topic, message_data=args.message, **message_attr)

if __name__ == '__main__':
    main()