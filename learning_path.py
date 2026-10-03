from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a personalized learning path for the topic below.
Assume the learner is a beginner.
Organize it from Beginner -> Intermediate -> Advanced.
For each stage include:
- concepts to learn
- a small practice task
- suggested resource types (video/article/book/documentation)
- a simple checkpoint

Do not invent specific URLs. Keep the plan realistic and concise.

Topic:
{topic}
"""
    return generate_text(prompt, temperature=0.35, max_output_tokens=1400)
