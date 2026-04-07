"""
schemas.py — Pydantic output schemas for ClarusMCP tools.

These classes serve two purposes:
1. They are passed to Gemini as response_schema to enforce structured JSON output.
2. They document exactly what each tool returns, making the system easier to maintain.
"""

from typing import List
from pydantic import BaseModel, Field


# ── Tool 1: Clinical Summary ──────────────────────────────────────────────────

class ClinicalContext(BaseModel):
    medications: List[str] = Field(
        default_factory=list,
        description="List of current medications"
    )
    allergies: List[str] = Field(
        default_factory=list,
        description="Known allergies"
    )
    relevant_history: str = Field(
        default="None reported",
        description="Brief relevant medical history or 'None reported'"
    )


class ClinicalSummaryResponse(BaseModel):
    summary: str = Field(
        description="2-3 sentence narrative clinical overview"
    )
    key_symptoms: List[str] = Field(
        default_factory=list,
        description="List of the patient's key symptoms"
    )
    visit_reason: str = Field(
        description="Concise restatement of the chief complaint"
    )
    context: ClinicalContext
    disclaimer: str = Field(
        default=(
            "This summary is AI-generated for educational/demo purposes "
            "and does not constitute medical advice."
        )
    )


# ── Tool 2: Medication Explainer ──────────────────────────────────────────────

class MedicationDetail(BaseModel):
    name: str = Field(description="Medication name as provided")
    generic_name: str = Field(
        description="Generic name if applicable, else same as name"
    )
    purpose: str = Field(
        description="What this medication is typically used for"
    )
    how_used: str = Field(
        description="Typical route and frequency in plain language"
    )
    common_side_effects: List[str] = Field(
        default_factory=list,
        description="2-3 common side effects"
    )
    safety_notes: str = Field(
        description="One key safety tip, e.g. take with food"
    )


class MedicationExplainerResponse(BaseModel):
    medications: List[MedicationDetail] = Field(default_factory=list)
    disclaimer: str = Field(
        default=(
            "These explanations are for general education only. "
            "Always follow your prescriber's instructions and consult "
            "a pharmacist or doctor with questions about your specific medications."
        )
    )


# ── Tool 3: Clinical Risk Insights ────────────────────────────────────────────

class RiskFlag(BaseModel):
    signal: str = Field(description="Concise name of the risk signal")
    severity: str = Field(
        description="One of: low, moderate, high"
    )
    explanation: str = Field(
        description="Why this is flagged in plain language"
    )
    contributing_factors: List[str] = Field(
        default_factory=list,
        description="Factors contributing to this signal"
    )


class ClinicalRiskResponse(BaseModel):
    risk_flags: List[RiskFlag] = Field(default_factory=list)
    overall_note: str = Field(
        description="High-level observation about the patient picture"
    )
    recommended_follow_up: str = Field(
        description="General suggestion for clinician review"
    )
    disclaimer: str = Field(
        default=(
            "These risk signals are AI-generated observations for educational/demo purposes only. "
            "They do not constitute a diagnosis or clinical recommendation. "
            "Always consult a qualified healthcare professional."
        )
    )