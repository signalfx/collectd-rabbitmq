#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR

docker-compose run --rm -T test
status=$?

docker-compose stop -t0

exit $status
