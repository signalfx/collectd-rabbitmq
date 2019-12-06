#!/bin/bash
set -e
flake8 --max-line-length=120 rabbitmq.py metric_info.py
py.test test_rabbitmq.py
