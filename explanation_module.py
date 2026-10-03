import os
from gemini_client import generate_text

# The reference architecture describes LaMini-Flan-T5-783M for this module.
# LOCAL_EXPLAINER=lamini can be enabled if the optional local-model dependencies
# are installed. The default is Gemini so the project is lightweight and easy
# to run on a normal student laptop.

LOCAL_EXPLAINER = os.getenv("LOCAL_EXPLAINER", "gemini").lower()


def explain_topic(topic: str) -> str:
    if LOCAL_EXPLAINER == "lamini":
        try:
            from transformers import pipeline
            model = pipeline(
                "text2text-generation",
                model="MBZUAI/LaMini-Flan-T5-783M",
                max_new_tokens=300,
            )
            prompt = (
                "Explain this educational topic simply for a beginner. "
                "Use short sections and one simple example. Topic: " + topic
            )
            return model(prompt)[0]["generated_text"]
        except Exception:
            # Safe fallback keeps the application usable if the optional
            # local model cannot be loaded.
            pass

    prompt = f"""
You are EduGenie, a patient educational assistant.
Explain the following topic to a beginner.
Use simple language, short headings, bullet points, and one easy example.
Do not invent facts. If the topic is ambiguous, state the assumption.

Topic:
{topic}
"""
    return generate_text(prompt, temperature=0.3, max_output_tokens=900)
