import json
import re

from gemini_client import generate_text
from prompts import QUIZ_PROMPT


def generate_quiz(topic: str):
    topic = topic.strip()

    if not topic:
        raise ValueError("Please enter a topic for the quiz.")

    prompt = QUIZ_PROMPT.format(topic=topic)
    response = generate_text(prompt)

    cleaned = re.sub(
        r"^```(?:json)?\s*|\s*```$",
        "",
        response.strip(),
        flags=re.IGNORECASE,
    ).strip()

    try:
        quiz = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(
            "Could not parse the quiz response as JSON."
        ) from exc

    if not isinstance(quiz, list) or len(quiz) != 3:
        raise ValueError("The quiz must contain exactly 3 questions.")

    for question in quiz:
        if not isinstance(question, dict):
            raise ValueError("Invalid quiz question format.")

        required = ("question", "options", "answer")

        if not all(key in question for key in required):
            raise ValueError(
                "Each quiz question must contain question, options, and answer."
            )

        if not isinstance(question["options"], list):
            raise ValueError("Quiz options must be a list.")

        if len(question["options"]) != 4:
            raise ValueError(
                "Each quiz question must contain exactly 4 options."
            )

        if question["answer"] not in ["A", "B", "C", "D"]:
            raise ValueError(
                "Each answer must be A, B, C, or D."
            )

    return quiz