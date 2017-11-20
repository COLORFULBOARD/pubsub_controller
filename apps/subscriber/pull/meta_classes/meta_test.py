# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from apps.utils.log import log, error_log


class MetaTest(object):

    @classmethod
    def main(cls, message):
        """
        test
        """
        log('meta_test')
        if 'text' in message:
            log(message.text)
