#!/usr/bin/env python
"""
This module contains metadata about each metric reported to SignalFx
by the RabbitMQ plugin.

Each metric contains two fields:
    metric_type - The kind of data represented by the metric, either 'gauge',
        'counter', or 'cumulative_counter'
    verbosity_level - An integer representing at what level the plugin
        verbosity must be set to in order for the metric to be reported to
        SignalFx. For example, if the plugin verbosity level is set to
        DEBUG (2), metrics with verbosity_level INFO (1) or DEBUG (2) will be
        reported, but TRACE (3) will not. To set the verbosity level, modify
        the VerbosityLevel setting in the plugin config file, usually
        10_rabbitmq.conf
"""
# Verbosity constants
INFO = 1
DEBUG = 2
TRACE = 3
VERBOSITY_LEVELS = {
    "info": INFO,
    "debug": DEBUG,
    "trace": TRACE
}

metric_data = {
    'channel.connection_details.peer_port': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'channel.consumer_count': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'channel.global_prefetch_count': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'channel.message_stats.ack': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'channel.message_stats.ack_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'channel.message_stats.confirm': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'channel.message_stats.confirm_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'channel.message_stats.deliver': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'channel.message_stats.deliver_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'channel.message_stats.deliver_get': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'channel.message_stats.deliver_get_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'channel.message_stats.publish': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'channel.message_stats.publish_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'channel.messages_unacknowledged': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'channel.messages_uncommitted': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'channel.messages_unconfirmed': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'channel.number': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'channel.prefetch_count': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'connection.channel_max': {
        'metric_type': 'counter',
        'verbosity_level': TRACE
    },
    'connection.channels': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'connection.connected_at': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'connection.frame_max': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'connection.peer_port': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'connection.port': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'connection.recv_cnt': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'connection.recv_oct': {
        'metric_type': 'counter',
        'verbosity_level': DEBUG
    },
    'connection.recv_oct_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'connection.send_cnt': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'connection.send_oct': {
        'metric_type': 'counter',
        'verbosity_level': DEBUG
    },
    'connection.send_oct_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'connection.send_pend': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'connection.timeout': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'exchange.message_stats.confirm': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'exchange.message_stats.confirm_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'exchange.message_stats.publish_in': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'exchange.message_stats.publish_in_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'exchange.message_stats.publish_out': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'exchange.message_stats.publish_out_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.disk_free': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'node.disk_free_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.disk_free_limit': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'node.fd_total': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'node.fd_used': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'node.fd_used_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.io_read_avg_time': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'node.io_read_avg_time_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.io_read_bytes': {
        'metric_type': 'counter',
        'verbosity_level': DEBUG
    },
    'node.io_read_bytes_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.io_read_count': {
        'metric_type': 'counter',
        'verbosity_level': DEBUG
    },
    'node.io_read_count_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.io_sync_avg_time': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'node.io_sync_avg_time_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.io_write_avg_time': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'node.io_write_avg_time_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.mem_limit': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'node.mem_used': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'node.mem_used_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.mnesia_disk_tx_count': {
        'metric_type': 'counter',
        'verbosity_level': DEBUG
    },
    'node.mnesia_disk_tx_count_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'node.mnesia_ram_tx_count': {
        'metric_type': 'counter',
        'verbosity_level': DEBUG
    },
    'node.mnesia_ram_tx_count_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'node.net_ticktime': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'node.proc_total': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.proc_used': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.proc_used_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.processors': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'node.run_queue': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'node.sockets_total': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'node.sockets_used': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'node.sockets_used_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'node.uptime': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'queue.backing_queue_status.avg_ack_egress_rate': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'queue.backing_queue_status.avg_ack_ingress_rate': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'queue.backing_queue_status.avg_egress_rate': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'queue.backing_queue_status.avg_ingress_rate': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'queue.backing_queue_status.len': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.backing_queue_status.next_seq_id': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'queue.backing_queue_status.q1': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'queue.backing_queue_status.q2': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'queue.backing_queue_status.q3': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'queue.backing_queue_status.q4': {
        'metric_type': 'gauge',
        'verbosity_level': TRACE
    },
    'queue.consumer_utilisation': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.consumers': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'queue.disk_reads': {
        'metric_type': 'counter',
        'verbosity_level': DEBUG
    },
    'queue.disk_writes': {
        'metric_type': 'counter',
        'verbosity_level': DEBUG
    },
    'queue.memory': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'queue.message_bytes': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'queue.message_bytes_persistent': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.message_bytes_ram': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.message_bytes_ready': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.message_bytes_unacknowledged': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.message_stats.ack': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'queue.message_stats.ack_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.message_stats.deliver': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'queue.message_stats.deliver_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.message_stats.deliver_get': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'queue.message_stats.deliver_get_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.message_stats.publish': {
        'metric_type': 'counter',
        'verbosity_level': INFO
    },
    'queue.message_stats.publish_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.messages': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'queue.messages_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.messages_persistent': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'queue.messages_ram': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.messages_ready': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'queue.messages_ready_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.messages_ready_ram': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.messages_unacknowledged': {
        'metric_type': 'gauge',
        'verbosity_level': INFO
    },
    'queue.messages_unacknowledged_details.rate': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    },
    'queue.messages_unacknowledged_ram': {
        'metric_type': 'gauge',
        'verbosity_level': DEBUG
    }
}
