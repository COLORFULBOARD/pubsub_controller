# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import sys
import ast
from google.cloud import pubsub_v1
from apps.utils.log import log, error_log
from settings import GCP_PROJECT_ID


def __encode_byteString(target):
    if isinstance(target, unicode):
        return target.encode('utf-8')
    else:
        return target


def main(topic_name, message_data, **message_attr):
    """
    受け取った値を元にPub/SubメッセージをPublishする
    :param topic_name: Publish target Topic 
    :param message_data: Publish message data
    :param message_attr: (optional)Publish message attr
    """
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(GCP_PROJECT_ID, topic_name)
    log('Publishing for message on {}'.format(topic_name))

    data = __encode_byteString(message_data)
    publisher.publish(topic_path, data=data, **message_attr)

    log('Published message.')

if __name__ == '__main__':
    args = sys.argv
    if not len(args) == 3 and not len(args) == 4:
        error_log('Require argument. topic_name, message_data, (optional)message_attr')
        error_log('Input argument is {}'.format(args))
        exit(1)

    print('Argument : {}'.format(args))
    message_attr = None
    if len(args) == 4:
        try:
            message_attr = ast.literal_eval(args[3])
        except Exception as e:
            error_log('Invalid argument. Attr is must be dict format.')
            exit(1)

    main(topic_name=args[1], message_data=args[2], **message_attr)

