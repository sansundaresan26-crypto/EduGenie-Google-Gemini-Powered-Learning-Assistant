import json
import re
from typing import Any

from gemini_client import generate_text


def clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def _fallback_quiz() -> list[dict[str, Any]]:
    return [{
        "question": "Quiz generation failed because the AI response was not valid JSON.",
        "options": ["Try again", "Check the API key", "Use a shorter passage", "All of these"],
        "answer": "All of these",
    }]


def generate_quiz(text: str) -> list[dict[str, Any]]:
    prompt = f"""
Create exactly 3 multiple-choice questions from the educational text below.
Each question must have exactly 4 options and one correct answer.
Return ONLY valid JSON, with no Markdown and no extra text.
Schema:
[
  {{
    "question": "string",
    "options": ["string", "string", "string", "string"],
    "answer": "one exact option string"
  }}
]

Educational text:
{text}
"""
    raw = generate_text(prompt, temperature=0.2, max_output_tokens=1400)
    cleaned = clean_json_block(raw)
    try:
        data = json.loads(cleaned)
        if not isinstance(data, list) or len(data) != 3:
            raise ValueError("Expected exactly 3 questions.")
        for item in data:
            if (
                not isinstance(item, dict)
                or not isinstance(item.get("question"), str)
                or not isinstance(item.get("options"), list)
                or len(item["options"]) != 4
                or item.get("answer") not in item["options"]
            ):
                raise ValueError("Invalid quiz schema.")
        return data
    except Exception as exc:
        raise RuntimeError(f"Quiz generation/parsing failed: {exc}")
