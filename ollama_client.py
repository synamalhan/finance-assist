# ollama_client.py

import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"  # make sure Ollama is running

def query_ollama(prompt):
    headers = {"Content-Type": "application/json"}
    payload = {
        "prompt": f"Explain this in simple terms suitable for someone aged 65+ use terms that are not technical, provide explanations for everything: {prompt}",
        "model": "mistral",  # or llama2, mixtral, etc.
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json().get("response", "").strip()
        else:
            return f"⚠️ Model error: {response.status_code}"
    except Exception as e:
        return f"⚠️ Could not connect to Ollama: {e}"
