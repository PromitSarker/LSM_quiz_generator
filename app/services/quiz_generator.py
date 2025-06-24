from app.core.config import settings
from app.schemas.quiz import Quiz
import json
import httpx

api_key = settings.GROQ_API_KEY
api_url = settings.GROQ_API_URL  # <-- fix this line
model = settings.LLM_MODEL

async def generate_quiz_from_text(text: str) -> Quiz | None:
    """
    Generates a quiz from the given text using an LLM, based on the entire content.
    """
    system_prompt = """You are an expert quiz maker specializing in OSHA (Occupational Safety and Health Administration) standards.
Your task is to create a quiz based *only* on the text provided by the user.
Read the following text carefully. Based *exclusively* on this text, generate exactly 6 multiple-choice questions in the **same language** as the input text.
Not only What, Why, How, but also creative questions. Avoid duplicate questions or overlapping answer options.

The output must be a single JSON object.
This object must have a key named "quiz".
The "quiz" object must contain:
1. A "title" key with a string value suitable for the quiz (in the same language as the input text). show output in the same language as the input text.
2. A "questions" key, which is a list of 6 question objects.

Each object in the "questions" list must have the following exact keys:
- "question_text": The string of the question.
- "options": A list of 4 strings.
- "correct_answer": A string containing the correct answer.

Do not include any other keys. Do not include explanations.
"""

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
            "temperature": 0.4,
            "max_tokens": 2048,
            "response_format": {"type": "json_object"},
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(api_url, headers=headers, json=payload)
            response.raise_for_status()
            chat_completion = response.json()
        
        quiz_data = json.loads(chat_completion["choices"][0]["message"]["content"])
        return Quiz(**quiz_data['quiz'])

    except Exception as e:
        print(f"Error generating quiz: {e}")
        return None