#!/bin/bash

docker build -t zbio/llama2:base . -f docker/Dockerfile.base

docker build -t zbio/llama2:13b . -f docker/Dockerfile.13b