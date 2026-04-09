import json
import os
from typing import Any, Type

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import ValidationError

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment.")

MODEL_ID = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite-preview")

client = genai.Client(api_key=api_key)


def _validate_with_pydantic(response_schema: Type, data: dict) -> dict:
    """
    Validate Gemini JSON against a Pydantic schema and return a clean dict.

    Supports both:
    - Pydantic v2: model_validate / model_dump
    - Pydantic v1: parse_obj / dict
    """
    try:
        if hasattr(response_schema, "model_validate"):  # Pydantic v2
            validated = response_schema.model_validate(data)
            return validated.model_dump()
        else:  # Pydantic v1 fallback
            validated = response_schema.parse_obj(data)
            return validated.dict()
    except ValidationError as e:
        return {
            "error": "Schema validation failed.",
            "details": e.errors(),
            "raw_response": data,
        }


def generate_structured_clinical_insight(
    system_instruction: str,
    user_prompt: str,
    response_schema: Type,
) -> dict:
    """
    Call Gemini, request structured JSON, and validate the result
    against the supplied Pydantic schema before returning it.
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

        try:
            parsed_json = json.loads(response.text)
        except json.JSONDecodeError as e:
            return {
                "error": "Gemini returned invalid JSON.",
                "details": str(e),
                "raw_text": response.text,
            }

        validated_result = _validate_with_pydantic(response_schema, parsed_json)
        return validated_result

    except Exception as e:
        return {
            "error": "Gemini API call failed.",
            "details": str(e),
        }