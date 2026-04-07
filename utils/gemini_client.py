import json
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment.")

MODEL_ID = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite-preview")

client = genai.Client(api_key=api_key)


def generate_structured_clinical_insight(
    system_instruction: str,
    user_prompt: str,
    response_schema,
) -> dict:
    """
    Call Gemini and request a structured JSON response.
    Returns a Python dictionary safely.
    """
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json",
                response_schema=response_schema,
                temperature=0.2,
            ),
        )

        if not response.text:
            return {"error": "Empty response from Gemini."}

        return json.loads(response.text)

    except json.JSONDecodeError as e:
        return {
            "error": "Gemini returned invalid JSON.",
            "details": str(e),
        }
    except Exception as e:
        return {
            "error": "Gemini API call failed.",
            "details": str(e),
        }