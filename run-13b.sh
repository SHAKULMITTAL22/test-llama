#!/bin/bash

docker run -e HUGGINGFACE_TOKEN=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 --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --rm -it -p 5000:5000 zbio/llama2:13b