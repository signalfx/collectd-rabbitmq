#!/usr/bin/env python

import httplib
import json
from time import time, sleep

# Quick and dirty integration test for multiple broker support for RabbitMQ for
# one collectd instance. This test script is intended to be run with
# docker-compose with the provided docker-compose.yml configuration.

# This is not very flexible but could be expanded to support other types of
# integration tests if so desired.

BROKER_HOSTS = [
    'broker34',
    'broker35',
    'broker36',
]
TIMEOUT_SECS = 60


def get_metric_data():
    # Use httplib instead of requests so we don't have to install stuff with pip
    conn = httplib.HTTPConnection("fake_sfx", 8080)
    conn.request("GET", "/")
    resp = conn.getresponse()
    conn.close()
    return json.loads(resp.read())


def wait_for_metrics_from_each_broker():
    start = time()
    for broker in BROKER_HOSTS:
        print 'Waiting for metrics from broker %s...' % (broker,)
        eventually_true(lambda: any([broker in m.get('plugin_instance') for m in get_metric_data()]),
                        TIMEOUT_SECS - (time() - start))
        print 'Found!'


def eventually_true(f, timeout_secs):
    start = time()
    while True:
        try:
            assert f()
        except AssertionError:
            if time() - start > timeout_secs:
                raise
            sleep(1)
        else:
            break


if __name__ == "__main__":
    wait_for_metrics_from_each_broker()
