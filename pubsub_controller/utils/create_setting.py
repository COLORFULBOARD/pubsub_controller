# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import os

def main():
    print('PubSub Controller Setup Start.')
    print('This package will fetch one subscription and pull if there is a message.')
    print('If you have not created Pub/Sub\'s topic and subscription on the GCP Console yet, please create it.')
    GCP_PROJECT_ID = raw_input('Please input GCP_PROJECT_ID >>>  ')
    SUBSCRIPTION_ID = raw_input('Please input SUBSCRIPTION_ID >>>  ')
    POLLING_TIME = raw_input('Please input fetch interval second(blank: 60) >>>  ')
    if not POLLING_TIME:
        POLLING_TIME = 60
    else:
        try:
            int(POLLING_TIME)
        except ValueError:
            print('Error')
            print('  Interval second is not number.')
            return

    # pip install libraries path
    path = os.path.abspath(__file__).split('/utils')[0]

    with open(str('{}/settings.py'.format(path)), str('w')) as fd:
        settings = '\n'.join([
            '# -*- coding: utf-8 -*-',
            'from __future__ import (',
            '   absolute_import,',
            '   division,',
            '   print_function,',
            '   unicode_literals',
            ')',
            '',
            'GCP_PROJECT_ID = \'{}\''.format(GCP_PROJECT_ID),
            'SUBSCRIPTION_ID = \'{}\''.format(SUBSCRIPTION_ID),
            'POLLING_TIME = {}'.format(POLLING_TIME),
            '',
        ])
        fd.write(settings)

    print('Setup Finished.')
