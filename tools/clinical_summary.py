import json
from pydantic import BaseModel, Field
from typing import List, Optional
from utils.gemini_client import generate_structured_clinical_insight
from prompts import CLINICAL_SUMMARY_SYSTEM_PROMPT

class ClinicalContext(BaseModel):
    medications: Optional[List[str]] = Field(default_factory=list, description="List of patient medications")
    allergies: Optional[List[str]] = Field(default_factory=list, description="List of patient allergies")
    history: Optional[List[str]] = Field(default_factory=list, description="Relevant medical history if provided")

class ClinicalSummaryResponse(BaseModel):
    summary: str = Field(description="A professional, 1-2 sentence clinical overview of the patient's presentation.")
    key_symptoms: List[str] = Field(description="A list of the primary symptoms extracted from the input.")
    context: ClinicalContext = Field(description="Structured context including meds, allergies, and history.")

def generate_clinical_summary(raw_patient_input: str) -> str:
    """
    Transforms messy patient input into a structured clinical overview.
    """
    print(f"Processing clinical summary for input: {raw_patient_input[:50]}...")
    
    # This now returns a safe Python dictionary
    result_dict = generate_structured_clinical_insight(
        system_instruction=CLINICAL_SUMMARY_SYSTEM_PROMPT,
        user_prompt=raw_patient_input,
        response_schema=ClinicalSummaryResponse
    )
    
    # MCP expects a string output, so we format the dictionary nicely
    return json.dumps(result_dict, indent=2)