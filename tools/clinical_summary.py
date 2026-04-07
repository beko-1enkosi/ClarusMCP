from prompts import CLINICAL_SUMMARY_SYSTEM_PROMPT
from schemas import ClinicalSummaryResponse
from utils.gemini_client import generate_structured_clinical_insight


def generate_clinical_summary(raw_patient_input: str) -> dict:
    """
    Transforms messy patient input into a structured clinical overview.
    """
    return generate_structured_clinical_insight(
        system_instruction=CLINICAL_SUMMARY_SYSTEM_PROMPT,
        user_prompt=raw_patient_input,
        response_schema=ClinicalSummaryResponse,
    )