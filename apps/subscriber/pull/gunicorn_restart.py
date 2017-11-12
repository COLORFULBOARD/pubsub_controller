# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import subprocess

from apps.utils.log import log, error_log
from apps.subscriber.pull.subscribe_base import SubscribeBase


class GunicornRestart(SubscribeBase):

    @classmethod
    def received_function(cls, message):
        """
        "gunicorn restart"コマンドを発行する。
        :param message: subscribeしたメッセージ
        """
        if message.data == cls.__name__:
            # Subscribeしたメッセージがクラス名と一致すれば実行
            log('Restarting Gunicorn at Supervisor.')
            # Gunicorn Restart Command
            restart_command = 'supervisorctl restart gunicorn'
            try:
                log('start subprocess. command = {}'.format(restart_command))
                stdout = subprocess.check_output(restart_command, shell=True)
                log('subprocess output = {}'.format(stdout))
                log('subprocess finished.')
            except subprocess.CalledProcessError as process_error:
                error_log('subprocess error. cmd = {}'.format(process_error.cmd))
                error_log('subprocess error. returncode = {}'.format(process_error.returncode))
                error_log('subprocess error. output = {}'.format(process_error.output))
                raise
            except Exception as e:
                error_log('subprocess error : {}'.format(e))
                raise
