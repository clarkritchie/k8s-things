#!/usr/bin/env bash

FROM=${1:-"local"}
IMAGE="hello-world-python:latest"
if [[ ${FROM} == "remote" ]]; then
    IMAGE="clarkdritchie/${IMAGE}"
fi

docker run --rm -p 9000:6000 -e FOO=baz ${IMAGE}