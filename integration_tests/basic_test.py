"""
Basic integration tests of RabbitMQ that make sure the plugin loads in collectd
and sends something
"""
from functools import partial as p
import os
from textwrap import dedent

from collectdtesting import run_collectd, run_container, container_ip
from collectdtesting.assertions import wait_for, has_datapoint_with_dim
import pytest

PLUGIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

@pytest.mark.parametrize("rabbitmq_version", [
    "3.4",
    "3.5",
    "3.6",
])
def test_basic_metrics(rabbitmq_version):
    config = dedent("""
        LoadPlugin python
        <Plugin python>
          ModulePath "/opt/collectd-plugin"

          Import rabbitmq

          <Module rabbitmq>
            BrokerName "mybroker"
            Username "guest"
            Password "guest"
            Host "{host}"
            Port "15672"
            CollectChannels false
            CollectConnections true
            CollectExchanges true
            CollectNodes true
            CollectQueues true
            FieldLength 1023
            HTTPTimeout 20
            VerbosityLevel "info"
            Dimensions "testdim=5"
          </Module>
        </Plugin>
    """)
    with run_container("rabbitmq:%s-management" % rabbitmq_version) as rabbitmq_cont:
        with run_collectd(config.format(host=container_ip(rabbitmq_cont)), PLUGIN_DIR) \
                as (ingest, _):
            assert wait_for(p(has_datapoint_with_dim, ingest, "plugin", "rabbitmq")), \
                "Didn't received a rabbitmq datapoint"
