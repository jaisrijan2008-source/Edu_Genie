from gemini_client import generate_text
from prompts import EXPLAIN_PROMPT


def explain_concept(concept: str) -> str:
    concept = concept.strip()

    if not concept:
        raise ValueError("Please enter a concept to explain.")

    prompt = EXPLAIN_PROMPT.format(concept=concept)

    return generate_text(prompt)