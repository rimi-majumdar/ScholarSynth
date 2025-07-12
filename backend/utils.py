import requests
def query_llama_together(prompt, api_key):
    url="https://api.together.xyz/v1/chat/completions"
    body={
        "model":"meta-llama/Llama-3-8b-chat-hf",
        "messages":[{"role":"user","content":prompt}],
        "max_tokens":512,
        "temperature":0.7
    }
    headers={"Authorization":f"Bearer {api_key}","Content-Type":"application/json"}
    r=requests.post(url, headers=headers, json=body, timeout=60)
    return r.json()["choices"][0]["message"]["content"]