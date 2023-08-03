from flask import Flask, request, jsonify
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from huggingface_hub._login import _login
import os
import torch
import time

app = Flask(__name__)

token = os.environ.get('HUGGINGFACE_TOKEN')

# Check if the token is available
if token is not None:
    _login(token=token, add_to_git_credential=False)
else:
    print("Token not found in environment variable.")

# Load model
start_load = time.time()
model_name = "meta-llama/Llama-2-13b-chat-hf"
model = AutoModelForCausalLM.from_pretrained(model_name)
end_load = time.time()

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create pipeline
gen = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

@app.route("/generate", methods=["POST"])
def generate_response():
    data = request.json
    user_input = data["input"]
    temperature = data["temperature"]
    max_new_tokens = data["tokens"]

    # Generate response
    start_gen = time.time()
    response = gen(
        user_input,
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        num_return_sequences=1,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.2,
        length_penalty=1.0,
    )
    end_gen = time.time()

    # Extract the generated text from the response
    generated_text = response[0]['generated_text']

    # Print the response
    print("Generated response:", generated_text)

    # Calculate the timings
    load_time = end_load - start_load
    gen_time = end_gen - start_gen

    return jsonify({"response": generated_text, "load_time": load_time, "gen_time": gen_time})

if __name__ == "__main__":
    app.run()