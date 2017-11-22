# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import json
import argparse
from apps.utils.log import log
from apps.publisher.publish_message import publish


if __name__ == '__main__':
    """CLIから起動し、指定されたメッセージをPublishする
    
    """
    parser = argparse.ArgumentParser(
        prog='publish_message.py',
        usage='Exec on terminal.',
        add_help=True,
    )
    parser.add_argument('-t', '--topic', help='topic name', required=True, type=str)
    parser.add_argument('-m', '--message', help='message data', required=True, type=str)
    parser.add_argument('-a', '--attr', help='message attr', type=json.loads)

    args = parser.parse_args()
    log('Argument : {}'.format(args))
    message_attr = args.attr if args.attr else {}

    publish(topic_name=args.topic, message_data=args.message, **message_attr)
