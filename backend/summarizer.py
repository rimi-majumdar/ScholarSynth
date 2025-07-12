from backend.utils import query_llama_together
def generate_summary(content, api_key):
    prompt = f"Summarize the document in <=150 words.\n\n{content[:3000]}"
    return query_llama_together(prompt, api_key)