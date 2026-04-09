import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from tools.clinical_summary import generate_clinical_summary
from tools.medication_explainer import explain_medications
from tools.clinical_risk import explain_clinical_risk

load_dotenv()

app = FastAPI(
    title="ClarusMCP",
    description="Clinical Copilot MCP starter server for structured healthcare AI tools.",
    version="0.1.0",
)


class ClinicalSummaryRequest(BaseModel):
    raw_patient_input: str = Field(
        ...,
        description="Messy or free-form patient input to summarize"
    )

class MedicationExplanationRequest(BaseModel):
    medication_list_string: str = Field(
        ...,
        description="A list of medications (comma separated or raw text) to explain"
    )

class ClinicalRiskRequest(BaseModel):
    patient_summary_string: str = Field(
        ...,
        description="Patient summary or structured data to analyze for risk signals"
    )

@app.get("/")
def root():
    return {
        "message": "ClarusMCP is running",
        "available_tools": [
            "generate_clinical_summary",
            "explain_medications",
            "explain_clinical_risk"
        ],
    }


@app.post("/tools/generate-clinical-summary")
def clinical_summary_endpoint(payload: ClinicalSummaryRequest):
    result = generate_clinical_summary(payload.raw_patient_input)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result)

    return result

@app.post("/tools/explain-medications")
def medication_explainer_endpoint(payload: MedicationExplanationRequest):
    result = explain_medications(payload.medication_list_string)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result)

    return result

@app.post("/tools/explain-clinical-risk")
def clinical_risk_endpoint(payload: ClinicalRiskRequest):
    result = explain_clinical_risk(payload.patient_summary_string)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result)

    return result

if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8000))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)