# -*- coding:utf-8 -*-
import re
from setuptools import setup, find_packages

try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''

try:
    with open('LICENSE') as f:
        license = f.read()
except IOError:
    license = ''

with open('pubsub_controller/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            fd.read(), re.MULTILINE).group(1)

setup(
    name='pubsub_controller',
    version=version,
    description='It provides a resident process that periodically pull subscribes and publish on CLI and Python.',
    long_description=readme,
    author='SENSY Inc.',
    url='https://github.com/COLORFULBOARD/pubsub_controller',
    license=license,
    install_requires=[
        'google-cloud-pubsub==0.30.1'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pubsub-init = pubsub_controller.utils.create_setting:main',
            'subscribe = pubsub_controller.subscriber.pull.pull_subscriber:main',
            'publish = pubsub_controller.publisher.cli_publish:main',
        ],
    },
)
