# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from apps.utils.log import log, error_log
from apps.subscriber.pull.subscribe_base import SubscribeBase
from apps.subscriber.pull.meta_classes import *


class SubscribeMeta(SubscribeBase):

    @classmethod
    def received_function(cls, message):
        """
        Subscribeメッセージで指定されたClassを実行する
        :param message: subscribeしたメッセージ
        """
        if 'target' in message:
            target_class_name = message.target
            # Subscribeしたメッセージがクラス名と一致すれば実行
            log('Exec : {}'.format(target_class_name))
            try:
                target_class = eval(target_class_name)
                if target_class:
                    has_main = False
                    for x in dir(target_class):
                        if x == 'main':
                            has_main = True
                            break
                    if has_main:
                        target_class.main(message)
                    else:
                        error_log('Class {} has not main method.'.format(target_class_name))
                else:
                    error_log('Class {} not found.'.format(target_class_name))
            except Exception as e:
                error_log('Exec {}. error : {}'.format(target_class_name, e))
                raise
