

git lfs install

git clone https://huggingface.co/meta-llama/Llama-2-13b-chat-hf

mkdir meta-llama

mv Llama-2-13b-chat-hf meta-llama/

git clone https://github.com/soulteary/docker-llama2-chat.git

cd docker-llama2-chat

bash scripts/make-13b.sh

bash scripts/run-13b.sh