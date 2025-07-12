from backend.utils import query_llama_together

def generate_summary(content, api_key):
    if not content.strip():
        return "❌ No content found in document."

    prompt = f"""You are a research summarizer. Read the following document and produce a concise, academic summary of up to 150 words. Capture the key purpose, ideas, or findings without copying full sentences directly.

DOCUMENT:
{content[:3000]}
"""
    return query_llama_together(prompt, api_key)
