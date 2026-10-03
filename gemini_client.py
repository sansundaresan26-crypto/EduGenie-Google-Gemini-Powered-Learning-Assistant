import os
from functools import lru_cache

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


@lru_cache(maxsize=1)
def get_client():
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Gemini API key not configured. Add GEMINI_API_KEY to your .env file."
        )
    return genai.Client(api_key=api_key)


def generate_text(prompt: str, temperature: float = 0.4, max_output_tokens: int = 1200) -> str:
    client = get_client()
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        ),
    )
    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response.")
    return text.strip()
