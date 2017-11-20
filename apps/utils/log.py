# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import sys
from datetime import datetime as dt


def log(msg):
    sys.stdout.write(str('{date} {msg}'.format(date=dt.now(), msg=msg)) + '\n')
    sys.stdout.flush()


def error_log(msg):
    sys.stderr.write(str('{date} {msg}'.format(date=dt.now(), msg=msg)) + '\n')
    sys.stderr.flush()
