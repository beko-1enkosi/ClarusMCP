from typing import Any

from mcp.server.fastmcp import FastMCP

from tools.clinical_summary import generate_clinical_summary
from tools.medication_explainer import explain_medications
from tools.clinical_risk import explain_clinical_risk

# FastMCP handles MCP protocol compliance, tool discovery, and routing.
# json_response=True helps return structured JSON cleanly.
mcp = FastMCP(
    "ClarusMCP Core",
    json_response=True,
)


@mcp.tool()
def generate_clinical_summary_tool(raw_patient_input: str) -> dict[str, Any]:
    """
    Generate a structured clinical summary from messy or free-form patient text.

    Args:
        raw_patient_input: Raw patient description, symptoms, medications,
        allergies, and relevant history in free text.
    """
    return generate_clinical_summary(raw_patient_input)


@mcp.tool()
def explain_medications_tool(medication_list_string: str) -> dict[str, Any]:
    """
    Explain medications in plain, patient-friendly language.

    Args:
        medication_list_string: Raw or comma-separated medication list.
    """
    return explain_medications(medication_list_string)


@mcp.tool()
def explain_clinical_risk_tool(patient_summary_string: str) -> dict[str, Any]:
    """
    Identify conservative, non-diagnostic clinical risk signals from patient information.

    Args:
        patient_summary_string: Patient summary or structured clinical text to analyze.
    """
    return explain_clinical_risk(patient_summary_string)


if __name__ == "__main__":
    # Runs a remote MCP server over Streamable HTTP.
    # By default, clients connect to /mcp on the chosen host/port.
    mcp.run(transport="streamable-http")