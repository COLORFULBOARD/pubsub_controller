# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
)

import json
import click

from pubsub_controller.utils.create_setting import main as init_setting
from pubsub_controller.subscriber.pull.pull_subscriber import main as subscriber
from pubsub_controller.publisher.publish_message import publish as publisher


@click.group()
def cmd():
    pass


@cmd.command(name='init', short_help='init the setting')
def setting_init():
    message = """PubSub Controller Setup Start.
    This package will fetch one subscription and pull if there is a message.
    If you have not created Pub/Sub\'s topic and subscription on the GCP Console yet, please create it.
    """
    click.echo(message)

    project_id = click.prompt('Please input GCP_PROJECT_ID', type=str)
    subscription_id = click.prompt('Please input SUBSCRIPTION_ID', type=str)
    polling_time = click.prompt('Please input fetch interval second(default: 60)', type=int, default=60)

    init_setting(project_id, subscription_id, polling_time)
    click.echo('PubSub Controller Setup Finished.')


@cmd.command(name='subscribe', short_help='exec subscriber')
def run_subscriber():
    subscriber()


@cmd.command(name='publish', short_help='publish from CLI')
@click.argument('topic', nargs=1, type=str)
@click.argument('message', nargs=1, type=str)
@click.argument('attr', nargs=1, type=json.loads)
def publish(topic, message, attr):
    publisher(topic, message, **attr)
