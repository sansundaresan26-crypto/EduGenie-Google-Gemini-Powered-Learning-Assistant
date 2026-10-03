from gemini_client import generate_text


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational question-answering assistant.
Answer the student's question clearly and concisely.
Give the direct answer first, then a short explanation.
For academic questions, include an example when useful.
If the question depends on missing context, say what assumption you made.

Student question:
{question}
"""
    return generate_text(prompt, temperature=0.3, max_output_tokens=1000)
