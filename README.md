# 🏥 ClarusMCP — Clinical AI Superpowers (MCP Server)

[![Watch the Demo](https://img.shields.io/badge/Watch_Demo-Devpost-blue?style=for-the-badge)](YOUR_DEVPOST_OR_YOUTUBE_LINK_HERE)

ClarusMCP is a healthcare-focused Model Context Protocol (MCP) server that provides reusable AI-powered tools for clinical workflows.

It transforms messy patient input into structured, safe, and explainable outputs by combining:
- 🧠 **Generative AI** (Gemini 3.1 Flash Lite)
- 🔧 **MCP Tools** (Modular clinical superpowers)
- 🤖 **A2A Agents** (Orchestration via the Prompt Opinion platform)

---

## 🚀 What We Built

ClarusMCP exposes three core clinical tools to any connected AI agent:

### 🧾 1. Clinical Summary
Transforms raw patient text into structured clinical insights:
- Symptom extraction
- Medications & allergies detection
- Visit reason summarization

### 💊 2. Medication Explainer
Explains medications in simple, patient-friendly language:
- Purpose & generic names
- Typical usage
- Common side effects
- Crucial safety notes

### ⚠️ 3. Clinical Risk Insights
Identifies conservative, non-diagnostic risk signals:
- Highlights potential clinical concerns
- Explains contributing factors
- Suggests safe, general follow-up actions

---

## 🧠 Why This Matters

Healthcare AI often struggles with the **"last mile" problem**:
> *Turning raw AI outputs into structured, usable, and safe clinical insights.*

ClarusMCP solves this by:
- Enforcing strict structured outputs using Pydantic schemas.
- Ensuring safe, non-diagnostic reasoning through rigorous prompt engineering.
- Enabling instant reuse across any agent ecosystem via the Model Context Protocol.

---

## 🏗️ A## System Architecture (MCP + A2A Integration)


```text
User Input
   ↓
Prompt Opinion Agent (A2A)
   ↓
ClarusMCP (MCP Server via ngrok)
   ↓
Python Tools (Clinical Logic & Schemas)
   ↓
Google Gemini API (LLM)
   ↓
Structured JSON Output
   ↓
Agent formats final response
```

---

## 🧩 Tech Stack
* **Python:** Core backend logic
* **FastMCP:** Model Context Protocol SDK for tool discovery and streaming
* **FastAPI:** Local REST API testing and debugging
* **Google GenAI SDK:** AI model integration
* **Pydantic:** Strict JSON schema validation
* **ngrok:** Public exposure and tunneling
* **Prompt Opinion:** Agent orchestration and UI

---


## ⚙️ Setup Instructions

**1. Clone the repo**

```bash
git clone https://github.com/beko-1enkosi/ClarusMCP.git
cd ClarusMCP
```

**2. Create a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate # Linux/MacOS
venv\Scripts\activate    # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment**

Create a `.env` file in the root directory:

```code snippet
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-3.1-flash-lite-preview
PORT=8000
```

**5. Run the MCP server**

```bash
python3 mcp_server.py
```

**6. Expose the server (New Terminal)**

While the MCP server is running, open a second terminal window and create a secure tunnel:

```bash
ngrok http 8000 --host-header="localhost:8000"
```

**7. Connect to Prompt Opinion**

In the Prompt Opinion MCP Server configuration, use your ngrok URL and append `/mcp`:

```bash
https://your-ngrok-url.ngrok-free.app/mcp
```

---

## 💡 Usage Example (How to Prompt)

This example demonstrates how ClarusMCP processes real-world messy patient input end-to-end.

**Step 1: Setup the Context**

Use a synthetic patient in Prompt Opinion:
* **Name:** Marcus Vance
* **Age/Gender:** 45-year-old Male

**Step 2: The Prompt**


> *"I am a 45-year-old male. I've been feeling really dizzy and nauseous for the last 48 hours. I currently take Metformin and occasionally use Ibuprofen for back pain. I'm allergic to latex."*

**Step 3: The Orchestration (What Happens Next)**

The agent orchestrates:

1. Clinical summary extraction
2. Medication explanation
3. Risk signal analysis

**Step 4: The Output**

A clean, structured clinical overview with safety disclaimers.

---

## 🔐 Safety & Compliance
* No diagnosis
* No treatment recommendations
* Conservative language enforced
* Explicit disclaimers included
* Designed for educational/demo use only

---

## ⚠️ Disclaimer

This project is for educational and demonstration purposes only. It does not provide medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional.

---

## 👩‍💻 Author

Built by **Thobeka Nkosi**

WeThinkCode Software Engineering Student