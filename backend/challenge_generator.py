from backend.utils import query_llama_together
import re

def generate_challenges(content, api_key):
    prompt = f"""From the document below, generate exactly 3 open-ended comprehension questions.
Avoid generic instructions or list headers. Do not include answers.
Each question should be a full sentence ending in a question mark. 
Avoid "Here are...", "The following..." and similar patterns.

DOCUMENT:
{content[:3000]}
"""
    raw = query_llama_together(prompt, api_key)

    # Extract lines that look like real questions
    lines = [l.strip() for l in raw.split("\n") if "?" in l]
    
    # Remove numbered/bullet markers
    cleaned = []
    for line in lines:
        line = re.sub(r'^[0-9\-\•\)\.]+[\s]*', '', line)
        if line and "?" in line:
            cleaned.append(line)
        if len(cleaned) == 3:
            break

    return cleaned

def evaluate_answers(content, questions, answers, api_key):
    results = []
    for q, a in zip(questions, answers):
        if not a.strip():
            results.append("❗ No answer provided.")
            continue

        prompt = f"""You are evaluating a student's open-ended answer based on the provided document.

DOCUMENT:
{content[:3000]}

QUESTION: {q}
STUDENT ANSWER: {a}

Evaluate this answer based solely on the document. Be specific and justify your feedback clearly.
If the answer is incorrect or incomplete, explain why. Avoid generic phrases like "partially correct".
"""
        results.append(query_llama_together(prompt, api_key))
    return results
