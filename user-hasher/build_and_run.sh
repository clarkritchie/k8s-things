#! /bin/sh

docker kill user_hasher
docker rm user_hasher
docker build -t dexcom-inc/user-hasher . && \
docker run -d -p8000:8000 --name user_hasher -e USER_SALT=TESTSALT dexcom-inc/user-hasher
