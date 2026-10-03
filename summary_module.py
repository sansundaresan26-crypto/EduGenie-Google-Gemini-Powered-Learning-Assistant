from gemini_client import generate_text


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational passage for quick revision.
Keep the important facts and relationships.
Use a short title, bullet points, and a final one-sentence takeaway.
Do not add information that is not present in the passage.

Passage:
{text}
"""
    return generate_text(prompt, temperature=0.25, max_output_tokens=1000)
