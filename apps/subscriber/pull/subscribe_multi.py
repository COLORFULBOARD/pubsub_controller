# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import importlib
from apps.utils.log import log, error_log
from apps.subscriber.pull.subscribe_base import SubscribeBase


class SubscribeMulti(SubscribeBase):

    @classmethod
    def received_function(cls, message):
        """
        Pub/Subメッセージで指定されたClassを実行する
        :param message: subscribeしたメッセージ
        """
        if 'target' in message.attributes:
            # メッセージAttributeの['target']で指定されたmoduleをimportし、mainメソッドを実行
            target_module_path = 'apps.subscriber.pull.exec_classes.{}'.format(message.attributes['target'])
            log('Exec : {}'.format(target_module_path))
            try:
                target = importlib.import_module(target_module_path)
                if target:
                    has_main = False
                    for x in dir(target):
                        if x == 'main':
                            has_main = True
                            break
                    if has_main:
                        target.main(message.data, message.attributes)
                    else:
                        error_log('Module {} has not main method.'.format(target_module_path))
            except ImportError:
                error_log('Module {} not found.'.format(target_module_path))
                raise
            except Exception as e:
                error_log('Exec {}. error : {}'.format(target_module_path, e))
                raise
        else:
            log('target module name is not found')
