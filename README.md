# Collectd RabbitMQ Plugin

## Introduction

collectd-rabbitmq is a [collectd](http://www.collectd.org/) plugin that
collects statistics from RabbitMQ. The plugin uses the [RabbitMQ Management Plugin](https://www.rabbitmq.com/management.html)
to poll for statistics on a RabbitMQ server, then reports them to collectd.

When collectd is configured to publish metrics to SignalFx, metrics from this
plugin will be named according to the format:
`<metric type>.<category>.<statistic>`

For example:

```
gauge.connection.recv_oct_details.rate
counter.connection.send_oct
gauge.queue.message_stats.deliver_get_details.rate
```

## Requirements

* Collectd 4.9 or later (for the Python plugin)
* Python 2.6 or later
* RabbitMQ 3.0 or later
* RabbitMQ Management Plugin

## Configuration

SignalFx maintains a sample configuration file for this plugin here: [10-rabbitmq.conf](https://github.com/signalfx/integrations/blob/master/collectd-rabbitmq/10-rabbitmq.conf)

The following mandatory configuration options describe how the plugin will
connect to the RabbitMQ Management API:

* Username - the username for authentication
* Password - the password for authentication
* Host - hostname or IP address of the RabbitMQ server running the RabbitMQ
         Management Plugin
* Port - the port of the RabbitMQ Management API

The following boolean configuration options may be added to enable collection
of specific statistics:

* CollectChannels - enables collection of channel statistics
* CollectConnections - enables collection of connection statistics
* CollectExchanges - enables collection of exchange statistics
* CollectNodes - enables collection of node statistics
* CollectQueues - enables collection of queue statistics

An additional configuration option is available:

* IsHttps - Boolean for if host is https protocol. Default is False. 
* HTTPTimeout - Integer value in seconds before timing out when connecting
to the RabbitMQ Management API. Defaults to 60 seconds.
* FieldLength - Set the number of characters used to encode dimension data.
This option should only be set if you are using a non-SignalFx fork of
collectd that specifies fewer than 1024 characters for DATA_MAX_NAME_LEN in
plugin.h.
* VerbosityLevel - Representation of the quantity of metrics generated by
RabbitMQ that are actually reported to SignalFx. If not specified, the default
value is "info". The verbosity levels are as follows:

        "info": Only the most commonly-used metrics are reported
        "debug": Additonal metrics useful for debugging are reported
        "trace": All available metrics are reported

## Known Issues

### Truncating of long dimensions in the plugin_instance field

Collectd has a length limit on the plugin_instance field, which this plugin
uses to post dimensions to SignalFx. The dimensions include the node name,
vhost name, and queue name.

The combination of these names as generated by RabbitMQ may exceed the
length limit. As a result, the dimensions posted to SignalFx may be truncated.

This has no effect on the metrics and values to SignalFx, only some of the
RabbitMQ-specific dimensions associated with those metrics.

The length limit depends on which fork of collectd you are using.
The SignalFx fork of collectd has a 1023-character limit, while the
standard fork has a 127-character limit (63 characters prior to version 5.6.0).
If you are using the standard collectd and your dimensions are being truncated,
consider switching to the SignalFx fork.
See <https://signalfx-product-docs.readthedocs-hosted.com/en/latest/integrations/collectd-info.html>
for more information.

If you are not using the SignalFx fork, you should set the FieldLength
setting in the plugin configuration file to match your version of
collectd. For example:

```
FieldLength 63
```
