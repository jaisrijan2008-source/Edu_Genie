from gemini_client import generate_text
from prompts import SUMMARY_PROMPT


def summarize_text(content: str) -> str:
    content = content.strip()

    if not content:
        raise ValueError("Please enter content to summarize.")

    prompt = SUMMARY_PROMPT.format(content=content)

    return generate_text(prompt)