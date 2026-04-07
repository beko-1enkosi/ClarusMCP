import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from the .env file
load_dotenv()

# Initialize the Gemini client using the API key from the environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment.")

client = genai.Client(api_key=api_key)

# We'll use the model recommended by Prompt Opinion
MODEL_ID = "gemini-3.1-flash-lite-preview"

def generate_structured_clinical_insight(system_instruction: str, user_prompt: str, response_schema: type) -> str:
    """
    Sends a prompt to Gemini and enforces a specific JSON output structure.
    This is critical for MCP tools, as the returning data must be predictable.
    """
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json",
                response_schema=response_schema,
                temperature=0.2, # Keep it low for more deterministic, clinical outputs
            ),
        )
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "{}"