#!/usr/bin/env python
# Copyright (C) 2015 SignalFx, Inc.

import json
import pprint
import urllib2

import collectd

import metric_info

# Global constants
DEFAULT_API_TIMEOUT = 1  # Seconds to wait for the RabbitMQ API to respond
DEFAULT_METRIC_TYPE = 'gauge'
DEFAULT_VHOST_NAME = 'default'
DIMENSION_NAMES = frozenset(('node', 'name', 'vhost'))
PLUGIN_NAME = 'rabbitmq'

# These are determined by the plugin config settings and are set by config()
api_endpoints = []
api_urls = {}
plugin_config = {}


def _api_call(url):
    """
    Makes a REST call against the RabbitMQ API.

    Args:
    url (str): The URL to get, including endpoint

    Returns:
    list: The JSON response
    """
    try:
        resp = urllib2.urlopen(url, timeout=DEFAULT_API_TIMEOUT)
    except (urllib2.HTTPError, urllib2.URLError) as e:
        collectd.error("Error making API call (%s) %s" % (e, url))
        return []
    try:
        return json.load(resp)
    except ValueError, e:
        collectd.error("Error parsing JSON for API call (%s) %s" % (e, url))
        return []


def _format_dimensions(dimensions):
    """
    Formats a dictionary of dimensions to a format that enables them to be
    specified as key, value pairs in plugin_instance to signalfx. E.g.

    >>> dimensions = {'a': 'foo', 'b': 'bar'}
    >>> _format_dimensions(dimensions)
    "[a=foo,b=bar]"

    Args:
    dimensions (dict): Mapping of {dimension_name: value, ...}

    Returns:
    str: Comma-separated list of dimensions
    """
    # Collectd limits the plugin_instance field size to 63 characters, so
    # truncate anything longer than that (leaving room for the 2 brackets)
    MAX_FIELD_LEN = 61
    dim_pairs = ["%s=%s" % (k, v) for k, v in dimensions.iteritems()]
    dim_str = ",".join(dim_pairs)[:MAX_FIELD_LEN]
    return "[%s]" % dim_str


def post_metrics(metrics, dimensions):
    """
    Posts metrics to collectd.

    Args:
    metrics (dict): Mapping of {metric_name: value, ...}
    dimensions (dict): Mapping of {dimension_name: value, ...}
    """
    for metric, value in metrics.iteritems():
        datapoint = collectd.Values()
        datapoint.type = determine_metric_type(metric)
        datapoint.type_instance = metric
        datapoint.plugin = PLUGIN_NAME
        datapoint.plugin_instance = _format_dimensions(dimensions)
        datapoint.values = (value,)
        pprint_dict = {
            'plugin': datapoint.plugin,
            'plugin_instance': datapoint.plugin_instance,
            'type': datapoint.type,
            'type_instance': datapoint.type_instance,
            'values': datapoint.values
        }
        collectd.debug(pprint.pformat(pprint_dict))
        datapoint.dispatch()


def extract_dimensions(stat_dict):
    """
    Given a dictionary of RabbitMQ stats, extract some special ones
    that we want to treat as dimensions rather than metrics.
    Modifies the original dictionary to remove the dimension keys.

    Args:
    stat_dict (dict): Dictionary of stats

    Returns:
    dict: {dimension_name: dimension_val, ...}
    """
    dimensions = {}
    for dimension in DIMENSION_NAMES:
        if dimension in stat_dict:
            dimensions[dimension] = stat_dict.pop(dimension)
    # Special case to rename the default vhost to something more legible
    if dimensions.get('vhost') == '/':
        dimensions['vhost'] = DEFAULT_VHOST_NAME
    return dimensions


def is_metric_allowed(name, val):
    """
    Determines if a metric is allowed to be posted to SignalFx given its
    name and value. This is determined by the following criteria:
    -The metric value is a number
    -The metric name is in the global list of allowed metrics

    Args:
    name (str): The name of the metric, e.g. queue.message_stats.ack
    val: The value of the metric.

    Returns:
    bool: True if the metric can be posted, False if not.
    """
    # Disallow metrics that aren't numbers
    if not isinstance(val, (int, float)) or isinstance(val, bool):
        return False
    # Disallow metrics that aren't in the list of approved metrics
    if name not in metric_info.metric_types:
        return False
    # Allow everything else
    return True


def determine_metric_type(metric_name):
    """
    Determines the type of a metric (e.g. gauge, counter, etc.) by
    looking up the name in a mapping.

    Args:
    metric_name (str): The name of the metric

    Returns:
    str: The metric type
    """
    return metric_info.metric_types.get(metric_name, DEFAULT_METRIC_TYPE)


def determine_metrics(stats, base_name=''):
    """
    Iterate through a dictionary of RabbitMQ stats and determine
    metric names, values, and dimensions.

    Args:
    stats (dict): Dictionary of stats
    base_name (str): (Optional) A name to prepend to every metric name
    """
    metrics = {}
    stack = [(base_name, stats)]
    while stack:
        metric_base, stat_dict = stack.pop()
        for stat_name, stat_val in stat_dict.iteritems():
            if base_name:
                metric_name = "%s.%s" % (metric_base, stat_name)
            else:
                metric_name = stat_name
            if isinstance(stat_val, dict):
                stack.append((metric_name, stat_val))
            else:
                if is_metric_allowed(metric_name, stat_val):
                    metrics[metric_name] = stat_val
    return metrics


def config(config_values):
    """
    Loads information from the RabbitMQ collectd plugin config file.

    Args:
    config_values (collectd.Config): Object containing config values
    """
    global plugin_config, api_endpoints
    desired_keys = ('Username', 'Password', 'Host', 'Port', 'Realm')
    for val in config_values.children:
        if val.key in desired_keys:
            plugin_config[val.key] = val.values[0]
        elif val.key == 'CollectChannels' and val.values[0]:
            api_endpoints.append('channels')
        elif val.key == 'CollectConnections' and val.values[0]:
            api_endpoints.append('connections')
        elif val.key == 'CollectExchanges' and val.values[0]:
            api_endpoints.append('exchanges')
        elif val.key == 'CollectNodes' and val.values[0]:
            api_endpoints.append('nodes')
        elif val.key == 'CollectQueues' and val.values[0]:
            api_endpoints.append('queues')
    # Make sure all required config settings are present, and log them
    collectd.info("Using config settings:")
    for key in desired_keys:
        val = plugin_config.get(key)
        if val is None:
            raise ValueError("Missing required config setting: %s" % key)
        collectd.info("%s=%s" % (key, val))
    collectd.info("Collecting metrics for: %s" % pprint.pformat(api_endpoints))

    # Populate the API URLs now that we have the config
    base_url = ("http://%s:%s/api" %
                (plugin_config['Host'], plugin_config['Port']))
    auth = urllib2.HTTPBasicAuthHandler()
    auth.add_password(realm=plugin_config['Realm'],
                      user=plugin_config['Username'],
                      passwd=plugin_config['Password'],
                      uri=base_url)
    opener = urllib2.build_opener(auth)
    urllib2.install_opener(opener)
    for endpoint in api_endpoints:
        url = "%s/%s" % (base_url, endpoint)
        api_urls[endpoint] = url


def init():
    """
    The initialization callback is essentially a no-op for this plugin.
    """
    collectd.info("Initializing RabbitMQ plugin")


def read():
    """
    Makes API calls to RabbitMQ and records metrics to collectd.
    """
    metrics = {}
    for endpoint in api_endpoints:
        resp_list = _api_call(api_urls[endpoint])
        base_name = endpoint.rstrip('s')  # Report dimensions as singular
        for resp in resp_list:
            dimensions = extract_dimensions(resp)
            collectd.debug("Using dimensions:")
            collectd.debug(pprint.pformat(dimensions))
            metrics = determine_metrics(resp, base_name=base_name)
            post_metrics(metrics, dimensions)


def shutdown():
    """
    The shutdown callback is essentially a no-op for this plugin.
    """
    collectd.info("Stopping RabbitMQ plugin")


def setup_collectd():
    """
    Registers callback functions with collectd
    """
    collectd.register_config(config)
    collectd.register_init(init)
    collectd.register_read(read)
    collectd.register_shutdown(shutdown)


setup_collectd()
