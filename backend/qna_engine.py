from backend.utils import query_llama_together
def answer_question(content, question, api_key):
    prompt = f"""Use the document to answer the question. Include relevant citations.

DOCUMENT:
{content[:3000]}

QUESTION: {question}
"""
    return query_llama_together(prompt, api_key)