from backend.utils import query_llama_together
import re

def generate_challenges(content, api_key):
    prompt = f"""Generate 3 open-ended questions from the document.
Avoid generic phrasing or answers. Each must contain a question mark.

DOCUMENT:
{content[:3000]}
"""
    raw = query_llama_together(prompt, api_key)
    lines = [l.strip() for l in raw.split("\n") if "?" in l]
    return lines[:3]

def evaluate_answers(content, questions, answers, api_key):
    results = []
    for q, a in zip(questions, answers):
        if not a.strip():
            results.append("❗ No answer provided.")
            continue
        prompt = f"""DOCUMENT:
{content[:3000]}

QUESTION: {q}
ANSWER: {a}

Evaluate and justify based on the document content.
"""
        results.append(query_llama_together(prompt, api_key))
    return results