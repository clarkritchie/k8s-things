#!/usr/bin/env bash

docker build -t hello-world-python:latest .
docker tag hello-world-python:latest clarkdritchie/hello-world-python:latest
docker push clarkdritchie/hello-world-python:latest
