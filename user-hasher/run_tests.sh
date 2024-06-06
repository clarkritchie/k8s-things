#!/usr/bin/env bash

# start container in background
docker-compose up --build --detach

TEST_DIR=${1:-/app/tests}

docker exec -i user_hasher pytest -v ${TEST_DIR}

status=$?
if [ $status -ne 0 ]; then
    echo "*****************************************"
    echo "* Houston, there were test failures :-< *"
    echo "*****************************************"
else
    echo "*****************************************"
    echo "*       All tests passed!  Huzzah!      *"
    echo "*****************************************"
fi

# cleanup
docker compose down