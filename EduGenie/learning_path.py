from gemini_client import generate_text
from prompts import LEARNING_PATH_PROMPT


def generate_learning_path(topic: str) -> str:
    topic = topic.strip()

    if not topic:
        raise ValueError("Please enter a topic.")

    prompt = LEARNING_PATH_PROMPT.format(topic=topic)

    return generate_text(prompt)