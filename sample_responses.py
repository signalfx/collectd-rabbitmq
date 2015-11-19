queues = [
    {
        "arguments": {},
        "auto_delete": True,
        "backing_queue_status": {
            "avg_ack_egress_rate": 2412.18030640885,
            "avg_ack_ingress_rate": 2415.8358064180434,
            "avg_egress_rate": 2415.8358064180434,
            "avg_ingress_rate": 2415.8358064180434,
            "delta": [
                "delta",
                "undefined",
                0,
                "undefined"
            ],
            "len": 0,
            "next_seq_id": 36463,
            "q1": 0,
            "q2": 0,
            "q3": 0,
            "q4": 0,
            "target_ram_count": "infinity"
        },
        "consumer_utilisation": 0.9999996886159364,
        "consumers": 1,
        "disk_reads": 0,
        "disk_writes": 0,
        "durable": False,
        "exclusive_consumer_tag": "",
        "memory": 689912,
        "message_bytes": 624,
        "message_bytes_persistent": 0,
        "message_bytes_ram": 624,
        "message_bytes_ready": 0,
        "message_bytes_unacknowledged": 624,
        "message_stats": {
            "ack": 36411,
            "ack_details": {
                "rate": 2732.6
            },
            "deliver": 36454,
            "deliver_details": {
                "rate": 2741.0
            },
            "deliver_get": 36454,
            "deliver_get_details": {
                "rate": 2741.0
            },
            "publish": 36469,
            "publish_details": {
                "rate": 2741.2
            }
        },
        "messages": 52,
        "messages_details": {
            "rate": 8.6
        },
        "messages_persistent": 0,
        "messages_ram": 52,
        "messages_ready": 0,
        "messages_ready_details": {
            "rate": 0.0
        },
        "messages_ready_ram": 0,
        "messages_unacknowledged": 52,
        "messages_unacknowledged_details": {
            "rate": 8.6
        },
        "messages_unacknowledged_ram": 52,
        "name": "amq.gen-IexC4RkdXskmHR1zjqtQdg",
        "node": "rabbit@foobarnode",
        "policy": "",
        "recoverable_slaves": "",
        "state": "running",
        "vhost": "/"
    }
]

exchanges = [
    {
        "arguments": {},
        "auto_delete": False,
        "durable": True,
        "internal": False,
        "name": "",
        "type": "direct",
        "vhost": "/"
    },
    {
        "arguments": {},
        "auto_delete": False,
        "durable": True,
        "internal": False,
        "name": "amq.direct",
        "type": "direct",
        "vhost": "/"
    },
    {
        "arguments": {},
        "auto_delete": False,
        "durable": True,
        "internal": False,
        "name": "amq.fanout",
        "type": "fanout",
        "vhost": "/"
    },
    {
        "arguments": {},
        "auto_delete": False,
        "durable": True,
        "internal": False,
        "name": "amq.headers",
        "type": "headers",
        "vhost": "/"
    },
    {
        "arguments": {},
        "auto_delete": False,
        "durable": True,
        "internal": False,
        "name": "amq.match",
        "type": "headers",
        "vhost": "/"
    },
    {
        "arguments": {},
        "auto_delete": False,
        "durable": True,
        "internal": True,
        "name": "amq.rabbitmq.log",
        "type": "topic",
        "vhost": "/"
    },
    {
        "arguments": {},
        "auto_delete": False,
        "durable": True,
        "internal": True,
        "name": "amq.rabbitmq.trace",
        "type": "topic",
        "vhost": "/"
    },
    {
        "arguments": {},
        "auto_delete": False,
        "durable": True,
        "internal": False,
        "name": "amq.topic",
        "type": "topic",
        "vhost": "/"
    },
    {
        "arguments": {},
        "auto_delete": False,
        "durable": False,
        "internal": False,
        "message_stats": {
            "confirm": 30201376,
            "confirm_details": {
                "rate": 3428.8
            },
            "publish_in": 30201413,
            "publish_in_details": {
                "rate": 3429.4
            },
            "publish_out": 30201413,
            "publish_out_details": {
                "rate": 3429.4
            }
        },
        "name": "direct",
        "type": "direct",
        "vhost": "/"
    }
]

nodes = [
    {
        "applications": [
            {
                "description": "RabbitMQ AMQP Client",
                "name": "amqp_client",
                "version": "3.5.6"
            },
            {
                "description": "INETS  CXC 138 49",
                "name": "inets",
                "version": "5.9.7"
            },
            {
                "description": "ERTS  CXC 138 10",
                "name": "kernel",
                "version": "2.16.4"
            },
            {
                "description": "MNESIA  CXC 138 12",
                "name": "mnesia",
                "version": "4.11"
            },
            {
                "description": "MochiMedia Web Server",
                "name": "mochiweb",
                "version": "2.7.0-rmq3.5.6-git680dba8"
            },
            {
                "description": "CPO  CXC 138 46",
                "name": "os_mon",
                "version": "2.2.14"
            },
            {
                "description": "RabbitMQ",
                "name": "rabbit",
                "version": "3.5.6"
            },
            {
                "description": "RabbitMQ Management Console",
                "name": "rabbitmq_management",
                "version": "3.5.6"
            },
            {
                "description": "RabbitMQ Management Agent",
                "name": "rabbitmq_management_agent",
                "version": "3.5.6"
            },
            {
                "description": "RabbitMQ Web Dispatcher",
                "name": "rabbitmq_web_dispatch",
                "version": "3.5.6"
            },
            {
                "description": "SASL  CXC 138 11",
                "name": "sasl",
                "version": "2.3.4"
            },
            {
                "description": "ERTS  CXC 138 10",
                "name": "stdlib",
                "version": "1.19.4"
            },
            {
                "description": "webmachine",
                "name": "webmachine",
                "version": "1.10.3-rmq3.5.6-gite9359c7"
            },
            {
                "description": "XML parser",
                "name": "xmerl",
                "version": "1.3.5"
            }
        ],
        "auth_mechanisms": [
            {
                "description": "RabbitMQ Demo challenge-response authentication mechanism",
                "enabled": False,
                "name": "RABBIT-CR-DEMO"
            },
            {
                "description": "SASL PLAIN authentication mechanism",
                "enabled": True,
                "name": "PLAIN"
            },
            {
                "description": "QPid AMQPLAIN mechanism",
                "enabled": True,
                "name": "AMQPLAIN"
            }
        ],
        "cluster_links": [],
        "config_files": [
            "/etc/rabbitmq/rabbitmq.config"
        ],
        "contexts": [
            {
                "description": "RabbitMQ Management",
                "path": "/",
                "port": "15672"
            }
        ],
        "db_dir": "/data/mnesia/rabbit@foobarnode",
        "disk_free": 693854208,
        "disk_free_alarm": False,
        "disk_free_details": {
            "rate": 0.0
        },
        "disk_free_limit": 50000000,
        "enabled_plugins": [
            "rabbitmq_management"
        ],
        "exchange_types": [
            {
                "description": "AMQP fanout exchange, as per the AMQP specification",
                "enabled": True,
                "name": "fanout"
            },
            {
                "description": "AMQP direct exchange, as per the AMQP specification",
                "enabled": True,
                "name": "direct"
            },
            {
                "description": "AMQP headers exchange, as per the AMQP specification",
                "enabled": True,
                "name": "headers"
            },
            {
                "description": "AMQP topic exchange, as per the AMQP specification",
                "enabled": True,
                "name": "topic"
            }
        ],
        "fd_total": 1024,
        "fd_used": 20,
        "fd_used_details": {
            "rate": 0.0
        },
        "io_read_avg_time": 0,
        "io_read_avg_time_details": {
            "rate": 0.0
        },
        "io_read_bytes": 1,
        "io_read_bytes_details": {
            "rate": 0.0
        },
        "io_read_count": 1,
        "io_read_count_details": {
            "rate": 0.0
        },
        "io_sync_avg_time": 0,
        "io_sync_avg_time_details": {
            "rate": 0.0
        },
        "io_write_avg_time": 0,
        "io_write_avg_time_details": {
            "rate": 0.0
        },
        "log_file": "/data/log/rabbit@foobarnode.log",
        "mem_alarm": False,
        "mem_limit": 1580225331,
        "mem_used": 43495464,
        "mem_used_details": {
            "rate": 37004.8
        },
        "mnesia_disk_tx_count": 13,
        "mnesia_disk_tx_count_details": {
            "rate": 0.0
        },
        "mnesia_ram_tx_count": 16,
        "mnesia_ram_tx_count_details": {
            "rate": 0.0
        },
        "name": "rabbit@foobarnode",
        "net_ticktime": 60,
        "os_pid": "179",
        "partitions": [],
        "proc_total": 1048576,
        "proc_used": 198,
        "proc_used_details": {
            "rate": 0.0
        },
        "processors": 1,
        "rates_mode": "basic",
        "run_queue": 7,
        "running": True,
        "sasl_log_file": "/data/log/rabbit@foobarnode-sasl.log",
        "sockets_total": 829,
        "sockets_used": 3,
        "sockets_used_details": {
            "rate": 0.0
        },
        "type": "disc",
        "uptime": 27278495
    }
]

connections = [
    {
        "auth_mechanism": "PLAIN",
        "channel_max": 0,
        "channels": 1,
        "client_properties": {
            "capabilities": {
                "authentication_failure_close": True,
                "basic.nack": True,
                "connection.blocked": True,
                "consumer_cancel_notify": True,
                "exchange_exchange_bindings": True,
                "publisher_confirms": True
            },
            "copyright": "Copyright (C) 2007-2015 Pivotal Software, Inc.",
            "information": "Licensed under the MPL. See http://www.rabbitmq.com/",
            "platform": "Java",
            "product": "RabbitMQ",
            "version": "3.5.6"
        },
        "connected_at": 1447454073656,
        "frame_max": 131072,
        "host": "127.0.0.1",
        "name": "127.0.0.1:54814 -> 127.0.0.1:5672",
        "node": "rabbit@foobarnode",
        "peer_cert_issuer": "",
        "peer_cert_subject": "",
        "peer_cert_validity": "",
        "peer_host": "127.0.0.1",
        "peer_port": 54814,
        "port": 5672,
        "protocol": "AMQP 0-9-1",
        "recv_cnt": 117049856,
        "recv_oct": 16128209082,
        "recv_oct_details": {
            "rate": 66910.2
        },
        "send_cnt": 135569228,
        "send_oct": 106753380107,
        "send_oct_details": {
            "rate": 443076.4
        },
        "send_pend": 0,
        "ssl": False,
        "ssl_cipher": "",
        "ssl_hash": "",
        "ssl_key_exchange": "",
        "ssl_protocol": "",
        "state": "running",
        "timeout": 60,
        "type": "network",
        "user": "guest",
        "vhost": "/"
    },
    {
        "auth_mechanism": "PLAIN",
        "channel_max": 0,
        "channels": 1,
        "client_properties": {
            "capabilities": {
                "authentication_failure_close": True,
                "basic.nack": True,
                "connection.blocked": True,
                "consumer_cancel_notify": True,
                "exchange_exchange_bindings": True,
                "publisher_confirms": True
            },
            "copyright": "Copyright (C) 2007-2015 Pivotal Software, Inc.",
            "information": "Licensed under the MPL. See http://www.rabbitmq.com/",
            "platform": "Java",
            "product": "RabbitMQ",
            "version": "3.5.6"
        },
        "connected_at": 1447454073894,
        "frame_max": 131072,
        "host": "127.0.0.1",
        "name": "127.0.0.1:54815 -> 127.0.0.1:5672",
        "node": "rabbit@foobarnode",
        "peer_cert_issuer": "",
        "peer_cert_subject": "",
        "peer_cert_validity": "",
        "peer_host": "127.0.0.1",
        "peer_port": 54815,
        "port": 5672,
        "protocol": "AMQP 0-9-1",
        "recv_cnt": 938058,
        "recv_oct": 77569025339,
        "recv_oct_details": {
            "rate": 313140.4
        },
        "send_cnt": 132203038,
        "send_oct": 2836012874,
        "send_oct_details": {
            "rate": 11718.0
        },
        "send_pend": 0,
        "ssl": False,
        "ssl_cipher": "",
        "ssl_hash": "",
        "ssl_key_exchange": "",
        "ssl_protocol": "",
        "state": "flow",
        "timeout": 60,
        "type": "network",
        "user": "guest",
        "vhost": "/"
    }
]

channels = [
    {
        "acks_uncommitted": 0,
        "confirm": False,
        "connection_details": {
            "name": "127.0.0.1:54814 -> 127.0.0.1:5672",
            "peer_host": "127.0.0.1",
            "peer_port": 54814
        },
        "consumer_count": 1,
        "global_prefetch_count": 0,
        "message_stats": {
            "ack": 771229168,
            "ack_details": {
                "rate": 3257.8
            },
            "deliver": 771229188,
            "deliver_details": {
                "rate": 3255.4
            },
            "deliver_get": 771229188,
            "deliver_get_details": {
                "rate": 3255.4
            }
        },
        "messages_unacknowledged": 20,
        "messages_uncommitted": 0,
        "messages_unconfirmed": 0,
        "name": "127.0.0.1:54814 -> 127.0.0.1:5672 (1)",
        "node": "rabbit@foobarnode",
        "number": 1,
        "prefetch_count": 0,
        "state": "running",
        "transactional": False,
        "user": "guest",
        "vhost": "/"
    },
    {
        "acks_uncommitted": 0,
        "confirm": True,
        "connection_details": {
            "name": "127.0.0.1:54815 -> 127.0.0.1:5672",
            "peer_host": "127.0.0.1",
            "peer_port": 54815
        },
        "consumer_count": 0,
        "global_prefetch_count": 0,
        "message_stats": {
            "confirm": 771229197,
            "confirm_details": {
                "rate": 3255.2
            },
            "publish": 771229224,
            "publish_details": {
                "rate": 3253.6
            }
        },
        "messages_unacknowledged": 0,
        "messages_uncommitted": 0,
        "messages_unconfirmed": 27,
        "name": "127.0.0.1:54815 -> 127.0.0.1:5672 (1)",
        "node": "rabbit@foobarnode",
        "number": 1,
        "prefetch_count": 0,
        "state": "flow",
        "transactional": False,
        "user": "guest",
        "vhost": "/"
    }
]
