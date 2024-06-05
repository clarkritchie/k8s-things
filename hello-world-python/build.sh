#!/usr/bin/env bash

VERSION_FILE="version.txt"
if [ ! -f "${VERSION_FILE}" ]; then
  echo 1 > "${VERSION_FILE}"
fi
BUILD_NUMBER=$(<"${VERSION_FILE}")
BUILD_NUMBER=$((BUILD_NUMBER+1))
echo "$BUILD_NUMBER" > "${VERSION_FILE}"
echo "Build number incremented to: $BUILD_NUMBER"

docker build -t hello-world-python:${BUILD_NUMBER} .
docker tag hello-world-python:${BUILD_NUMBER} clarkdritchie/hello-world-python:${BUILD_NUMBER}
docker push clarkdritchie/hello-world-python:${BUILD_NUMBER}
