#!/usr/bin/env python
"""
Unit test for the RabbitMQ collectd plugin. Meant to be run with pytest.
"""
# Copyright (C) 2015 SignalFx, Inc.

import collections
import mock
import sys

import sample_responses


class MockCollectd(mock.MagicMock):
    """
    Mocks the functions and objects provided by the collectd module
    """
    @staticmethod
    def log(log_str):
        print log_str

    debug = log
    info = log
    warning = log
    error = log


def mock_api_call(url):
    """
    Returns example statistics from the sample_responses module.

    Args:
    url (str): The URL whose results to mock
    """
    endpoint = url.split('/')[-1]
    return getattr(sample_responses, endpoint)


sys.modules['collectd'] = MockCollectd()

import rabbitmq

mock_config = mock.Mock()
ConfigOption = collections.namedtuple('ConfigOption', ['key', 'values'])
mock_config.children = [
    ConfigOption('Username', ('guest',)),
    ConfigOption('Password', ('guest',)),
    ConfigOption('Host', ('localhost',)),
    ConfigOption('Port', (15672,)),
    ConfigOption('Realm', ('RabbitMQ Management',)),
    ConfigOption('CollectChannels', (True,)),
    ConfigOption('CollectConnections', (True,)),
    ConfigOption('CollectExchanges', (True,)),
    ConfigOption('CollectNodes', (True,)),
    ConfigOption('CollectQueues', (True,)),
]
rabbitmq.config(mock_config)


@mock.patch('rabbitmq._api_call', mock_api_call)
def test_read():
    """
    Tests the read() method of the collectd plugin. This codepath exercises
    most of the code in the plugin.
    """
    rabbitmq.read()
