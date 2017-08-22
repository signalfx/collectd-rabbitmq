#!/bin/bash
set -e
flake8 rabbitmq.py metric_info.py
py.test test_rabbitmq.py
