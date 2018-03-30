# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

from pubsub_controller.utils.log import log, error_log


def main(message_data, message_attr):
    """
    Exec Sample
    Require define "main(message_data, message_attr)" method
    """
    log(message_data)
    if 'text' in message_attr:
        log(message_attr['text'])
