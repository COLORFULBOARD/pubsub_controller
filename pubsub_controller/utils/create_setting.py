# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import os


def main(gcp_project_id, subscription_id, polling_time):
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
            'GCP_PROJECT_ID = \'{}\''.format(gcp_project_id),
            'SUBSCRIPTION_ID = \'{}\''.format(subscription_id),
            'POLLING_TIME = {}'.format(polling_time),
            '',
        ])
        fd.write(settings)
