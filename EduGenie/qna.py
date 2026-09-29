from gemini_client import generate_text
from prompts import QA_PROMPT


def answer_question(question: str) -> str:
    question = question.strip()

    if not question:
        raise ValueError("Please enter a question.")

    prompt = QA_PROMPT.format(question=question)

    return generate_text(prompt)