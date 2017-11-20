# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

from apps.utils.log import log, error_log


class MetaSample(object):

    @classmethod
    def main(cls, message_data, message_attr):
        """
        MetaClass_Sample
        """
        log(message_data)
        if 'text' in message_attr:
            log(message_attr['text'])
