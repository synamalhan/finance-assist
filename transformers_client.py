# transformers_client.py

from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

# Load a small model suitable for local use (e.g., TinyLLaMA, Phi, or GPT2)
# For better performance try "mistralai/Mistral-7B-Instruct-v0.1" if you have a good GPU
model_name = "gpt2"  # swap if needed

# Load model and tokenizer (this will download on first run)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# Create a pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def query_transformers(prompt):
    try:
        full_prompt = (
            "Explain this in simple terms suitable for someone aged 65+. "
            "Use non-technical terms and provide examples where possible: " + prompt
        )
        output = generator(full_prompt, max_new_tokens=300, temperature=0.7)[0]["generated_text"]
        return output[len(full_prompt):].strip()
    except Exception as e:
        return f"⚠️ Error running model locally: {e}"
