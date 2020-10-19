#!/usr/bin/env python
# Copyright (C) 2015 SignalFx, Inc.

import base64
import json
import pprint
import ssl

import collectd
from six.moves import urllib

import metric_info

# Global constants
DEFAULT_API_TIMEOUT = 60  # Seconds to wait for the RabbitMQ API to respond
DEFAULT_FIELD_LENGTH = 1023  # Assumes usage of the SignalFx fork of collectd
DEFAULT_METRIC_TYPE = "gauge"
DEFAULT_REALM = "RabbitMQ Management"
DEFAULT_VERBOSITY = metric_info.INFO
DEFAULT_VHOST_NAME = "default"
DIMENSION_NAMES = frozenset(("node", "name", "vhost"))
PLUGIN_NAME = "rabbitmq"

# Global list of brokers configured.  Each module gets added as a separate
# broker.
BROKERS = []


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
    if dimensions.get("vhost") == "/":
        dimensions["vhost"] = DEFAULT_VHOST_NAME
    return dimensions


def determine_metric_type(metric_name):
    """
    Determines the type of a metric (e.g. gauge, counter, etc.) by
    looking up the name in a mapping.

    Args:
    metric_name (str): The name of the metric

    Returns:
    str: The metric type
    """
    if metric_name not in metric_info.metric_data:
        return DEFAULT_METRIC_TYPE
    return metric_info.metric_data[metric_name]["metric_type"]


class Broker:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.host = ""
        self.port = ""
        self.api_endpoints = []
        self.field_length = DEFAULT_FIELD_LENGTH
        self.http_timeout = DEFAULT_API_TIMEOUT
        self.verbosity_level = DEFAULT_VERBOSITY
        self.broker_name = ""
        self.extra_dimensions = ""
        self.ssl_key_file = ""
        self.ssl_key_passphrase = ""
        self.ssl_cert_file = ""
        self.ssl_ca_cert_file = ""
        self.ssl_enabled = False
        self.ssl_verify = False

    def _api_call(self, url):
        """
        Makes a REST call against the RabbitMQ API.

        Args:
        url (str): The URL to get, including endpoint

        Returns:
        list: The JSON response
        """
        req = urllib.request.Request(url)

        # This is technically non-standard to send auth header upfront, but
        # RabbitMQ doesn't mind.  The alternative is globally modifying the
        # urllib with an opener each time before making a request.
        req.add_header(
            "Authorization",
            "Basic " + base64.b64encode(("%s:%s" % (self.username, self.password)).encode("utf-8")).decode("utf-8"),
        )

        context = None

        if self.ssl_enabled:
            context = ssl.create_default_context(cafile=self.ssl_ca_cert_file)
            if not self.ssl_verify:
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
            if self.ssl_cert_file:
                context.load_cert_chain(certfile=self.ssl_cert_file, keyfile=self.ssl_key_file,
                                        password=self.ssl_key_passphrase)

        try:
            resp = urllib.request.urlopen(req, timeout=self.http_timeout, context=context)
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            collectd.error("Error making API call (%s) %s" % (e, url))
            return []
        try:
            return json.load(resp)
        except ValueError as e:
            collectd.error("Error parsing JSON for API call (%s) %s" % (e, url))
            return []

    def get_metrics_and_dimensions(self):
        metrics = {}
        base_url = "%s://%s:%s/api" % ("https" if self.ssl_enabled else "http", self.host, self.port)

        for endpoint in self.api_endpoints:
            resp_list = self._api_call("%s/%s" % (base_url, endpoint))

            base_name = endpoint.rstrip("s")  # Report dimensions as singular
            for resp in resp_list:
                dimensions = extract_dimensions(resp)
                collectd.debug("Using dimensions:")
                collectd.debug(pprint.pformat(dimensions))
                metrics = self.determine_metrics(resp, base_name=base_name)
                yield metrics, dimensions

    def post_current_metrics(self):
        """
        Posts metrics to collectd.

        Args:
        metrics (dict): Mapping of {metric_name: value, ...}
        dimensions (dict): Mapping of {dimension_name: value, ...}
        """
        for metrics, dimensions in self.get_metrics_and_dimensions():
            for metric, value in metrics.items():
                datapoint = collectd.Values(meta={"0": True})
                datapoint.type = determine_metric_type(metric)
                datapoint.type_instance = metric
                datapoint.plugin = PLUGIN_NAME
                dim_string = self._format_dimensions(dimensions)
                datapoint.plugin_instance = self.broker_name + dim_string
                datapoint.values = (value,)

                pprint_dict = {
                    "plugin": datapoint.plugin,
                    "plugin_instance": datapoint.plugin_instance,
                    "type": datapoint.type,
                    "type_instance": datapoint.type_instance,
                    "values": datapoint.values,
                }
                collectd.debug(pprint.pformat(pprint_dict))

                datapoint.dispatch()

    def _format_dimensions(self, dimensions):
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
        # Collectd limits the plugin_instance field size, so truncate anything
        # longer than that.
        # account for the 2 brackets at either end
        trunc_len = self.field_length - 2
        dim_pairs = []
        # Put the name dimension first because it is more likely to be unique
        # and we don't want it to get truncated.
        if "name" in dimensions:
            dim_pairs.append("name=%s" % dimensions["name"])
        dim_pairs.extend("%s=%s" % (k, v) for k, v in dimensions.items() if k != "name")
        dim_str = ",".join(dim_pairs)[:trunc_len]

        if self.extra_dimensions:
            dim_str += ",%s" % self.extra_dimensions

        return "[%s]" % dim_str

    def determine_metrics(self, stats, base_name=""):
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
            for stat_name, stat_val in stat_dict.items():
                if base_name:
                    metric_name = "%s.%s" % (metric_base, stat_name)
                else:
                    metric_name = stat_name
                if isinstance(stat_val, dict):
                    stack.append((metric_name, stat_val))
                else:
                    if self.is_metric_allowed(metric_name, stat_val):
                        metrics[metric_name] = stat_val
        return metrics

    def is_metric_allowed(self, name, val):
        """
        Determines if a metric is allowed to be posted to collectd and SignalFx
        given its name and value. A metric is allowed if:
        -The metric value is a number.
            A positive number if the metric is a counter
        -The metric name is in the global list of allowed metrics
        -The metric verbosity level is <= the plugin verbosity level

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
        if name not in metric_info.metric_data:
            return False
        # Disallow metrics that are only reported at a higher verbosity level
        if metric_info.metric_data[name]["verbosity_level"] > self.verbosity_level:
            return False
        # Disallow counters with negative values. These cause a TypeError or
        # OverflowError with the collectd python plugin.
        if metric_info.metric_data[name]["metric_type"] == "counter" and val < 0:
            return False
        # Allow everything else
        return True


def config(config_values):
    """
    Loads information from the RabbitMQ collectd plugin config file.

    Args:
    config_values (collectd.Config): Object containing config values
    """

    b = Broker()

    # We use only single values so this works fine
    config_map = dict([(c.key, c.values[0]) for c in config_values.children])

    required_keys = ("Username", "Password", "Host", "Port")

    # Make sure all required config settings are present, and log them
    collectd.info("Using config settings:")
    for key in required_keys:
        if key not in config_map or not config_map[key]:
            raise ValueError("Missing required config setting: %s" % key)

    opt_to_endpoint_map = {
        "CollectChannels": "channels",
        "CollectConnections": "connections",
        "CollectExchanges": "exchanges",
        "CollectNodes": "nodes",
        "CollectQueues": "queues",
    }

    for key, value in list(config_map.items()):
        if key == "Username":
            b.username = value
        elif key == "Password":
            b.password = value
        elif key == "Host":
            b.host = value
        elif key == "Port":
            b.port = value
        # Optional settings below
        elif key in opt_to_endpoint_map and value:
            b.api_endpoints.append(opt_to_endpoint_map[key])
        elif key == "HTTPTimeout" and value:
            b.http_timeout = int(value)
        elif key == "FieldLength" and value:
            b.field_length = int(value)
        elif key == "VerbosityLevel" and value:
            level = value.lower()
            if level not in metric_info.VERBOSITY_LEVELS:
                raise ValueError("VerbosityLevel must be one of %s" % list(metric_info.VERBOSITY_LEVELS.keys()))
            b.verbosity_level = metric_info.VERBOSITY_LEVELS[level]
        elif key == "BrokerName":
            b.broker_name = value
        # This is supposed to be a preformatted string like
        # "key=value,key2=value2"
        elif key == "Dimensions":
            b.extra_dimensions = value
        elif key == "SSLKeyFile":
            b.ssl_key_file = value
        elif key == "SSLKeyPassphrase":
            b.ssl_key_passphrase = value
        elif key == "SSLCertFile":
            b.ssl_cert_file = value
        elif key == "SSLCACertFile":
            b.ssl_ca_cert_file = value
        elif key == "SSLEnabled":
            b.ssl_enabled = value
        elif key == "SSLVerify":
            b.ssl_verify = value

        collectd.info("Collecting metrics for: %s" % pprint.pformat(b.api_endpoints))

    BROKERS.append(b)

    if len(BROKERS) > 1:
        if any([not br.broker_name for br in BROKERS]):
            raise ValueError("BrokerName must be specified if configuring " "multiple plugin instances!")


def init():
    """
    The initialization callback is essentially a no-op for this plugin.
    """
    collectd.info("Initializing RabbitMQ plugin")


def read():
    """
    Makes API calls to RabbitMQ and records metrics to collectd.
    """
    for b in BROKERS:
        b.post_current_metrics()


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
