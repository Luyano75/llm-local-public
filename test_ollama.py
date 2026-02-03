import requests
import json
import os

# Load configuration from environment variables
OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'localhost')
OLLAMA_PORT = os.getenv('OLLAMA_PORT', '11434')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'phi3:mini')

def test_ollama():
    prompt = "Translate this to French: Hello world"
    url = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"
    
    payload = {
        'model': OLLAMA_MODEL,
        'prompt': prompt,
        'stream': False
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print(response.json()['response'])
    except Exception as e:
        print(f"Error connecting to Ollama: {e}")

if __name__ == "__main__":
    test_ollama()