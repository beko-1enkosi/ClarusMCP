import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from tools.clinical_summary import generate_clinical_summary

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


@app.get("/")
def root():
    return {
        "message": "ClarusMCP is running",
        "available_tools": [
            "generate_clinical_summary",
        ],
    }


@app.post("/tools/generate-clinical-summary")
def clinical_summary_endpoint(payload: ClinicalSummaryRequest):
    result = generate_clinical_summary(payload.raw_patient_input)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result)

    return result


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8000))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)