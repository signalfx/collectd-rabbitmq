#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR

printf "Running tests against python2.7\n"
docker-compose run --rm test
status=$?

docker-compose down

printf $status

if [ "$status" != "0" ]; then exit $status; fi

printf "\nRunning tests against python2.6"
docker-compose run --rm test26
status=$?

docker-compose down

printf $status

exit $status
