from prompts import CLINICAL_RISK_SYSTEM_PROMPT
from schemas import ClinicalRiskResponse
from utils.gemini_client import generate_structured_clinical_insight

def explain_clinical_risk(patient_summary_string: str) -> dict:
    """
    Identifies non-diagnostic risk signals from patient information and explains them.
    """
    print(f"Processing clinical risk for: {patient_summary_string[:50]}...")
    
    return generate_structured_clinical_insight(
        system_instruction=CLINICAL_RISK_SYSTEM_PROMPT,
        user_prompt=patient_summary_string,
        response_schema=ClinicalRiskResponse,
    )