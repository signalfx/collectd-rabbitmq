#!/bin/bash

set -e

flake8 rabbitmq.py metric_info.py
pytest rabbitmq_test.py
