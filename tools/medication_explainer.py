from prompts import MEDICATION_EXPLAINER_SYSTEM_PROMPT
from schemas import MedicationExplainerResponse
from utils.gemini_client import generate_structured_clinical_insight

def explain_medications(medication_list_string: str) -> dict:
    """
    Translates a list of medications into plain, patient-friendly explanations.
    """
    print(f"Processing medication explanation for: {medication_list_string[:50]}...")
    
    return generate_structured_clinical_insight(
        system_instruction=MEDICATION_EXPLAINER_SYSTEM_PROMPT,
        user_prompt=medication_list_string,
        response_schema=MedicationExplainerResponse,
    )