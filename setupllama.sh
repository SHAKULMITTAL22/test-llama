#!/bin/bash

git clone https://github.com/SHAKULMITTAL22/test-llama

cd test-llama

bash pre-req.sh

bash make-13b.sh

sudo docker run -e HUGGINGFACE_TOKEN=$HUGGINGFACE_TOKEN --gpus all --network host  --rm -it -p 5000:5000 zbio/llama2:13b