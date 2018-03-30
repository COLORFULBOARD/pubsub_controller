# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import importlib
from pubsub_controller.utils.log import log, error_log
from pubsub_controller.subscriber.pull.subscribe_base import SubscribeBase


class SubscribeMulti(SubscribeBase):

    @classmethod
    def received_function(cls, message):
        """
        Pub/Subメッセージで指定されたClassを実行する
        :param message: subscribeしたメッセージ
        """
        if 'target' in message.attributes:
            # メッセージAttributeの['target']で指定されたmoduleをimportし、mainメソッドを実行
            target_module_path = 'pubsub_controller.subscriber.pull.exec_classes.{}'.format(message.attributes['target'])
            log('Exec : {}'.format(target_module_path))
            try:
                target = importlib.import_module(target_module_path)
            except ImportError:
                error_log('Module "{}" not found.'.format(target_module_path))
                raise
            except Exception as e:
                error_log('Exec "{}". error : {}'.format(target_module_path, e))
                raise
            else:
                if hasattr(target, 'main'):
                    target.main(message.data, message.attributes)
                else:
                    error_log('Module {} has not main method.'.format(target_module_path))
        else:
            log('Require target module name.')
