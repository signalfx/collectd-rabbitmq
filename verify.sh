#!/bin/bash
flake8 rabbitmq.py test_rabbitmq.py metric_info.py
py.test test_rabbitmq.py
