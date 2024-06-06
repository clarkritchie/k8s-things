#! /bin/sh

# docker kill user-hasher # && docker rm user-hasher
docker build -t k8s-things/user-hasher -f Dockerfile.dev .
docker run --entrypoint /entrypoint.sh \
  -p8000:8000 \
  -e USER_SALT=TESTSALT \
  -e APP_VERSION=localhost \
  k8s-things/user-hasher

# docker run -p8000:8000 --name user-hasher -e USER_SALT=TESTSALT user-hasher

#