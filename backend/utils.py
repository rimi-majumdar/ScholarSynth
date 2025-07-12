import requests

def query_llama_together(prompt, api_key):
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 512,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=body, timeout=60)
        response.raise_for_status()
        data = response.json()

        # Extract response safely
        return data.get("choices", [{}])[0].get("message", {}).get("content", "[No response from model]")

    except Exception as e:
        return f"❌ Error querying LLaMA model: {str(e)}"
