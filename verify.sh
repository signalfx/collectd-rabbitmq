#!/bin/bash
flake8 rabbitmq.py metric_info.py
if [ "$?" -ne 0 ]; then
    exit 1;
fi
py.test test_rabbitmq.py
if [ "$?" -ne 0 ]; then
    exit 1;
fi
