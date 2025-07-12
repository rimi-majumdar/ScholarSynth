from backend.utils import query_llama_together

def answer_question(content, question, api_key):
    if not question.strip():
        return "❗ No question provided."

    if not content.strip():
        return "❌ Document content is empty or not loaded."

    prompt = f"""You are an academic assistant. Use the following document to answer the user’s question.

Please provide a well-explained, evidence-based answer. Quote or reference the document briefly when necessary. Keep the answer concise and clear.

DOCUMENT:
{content[:3000]}

QUESTION:
{question}
"""
    return query_llama_together(prompt, api_key)
