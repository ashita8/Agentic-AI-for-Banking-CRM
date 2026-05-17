# Agentic AI for Banking CRM

AI-powered conversational CRM copilot for banking relationship managers built using FastAPI, LangGraph, Groq LLM, and modular agentic workflows.

This project helps relationship managers identify high-potential banking customers, estimate conversion likelihood, recommend suitable financial products, and generate personalized outreach messages using transaction intelligence and LLM-powered reasoning.

---

# Problem Statement

Relationship Managers (RMs) often spend significant time manually:

* analyzing customer profiles
* identifying high-value prospects
* understanding transaction behavior
* recommending suitable financial products
* creating personalized customer outreach

This project automates that workflow using an Agentic AI system capable of:

* understanding conversational CRM requests
* decomposing tasks dynamically
* orchestrating multiple tools and services
* analyzing customer + transaction intelligence
* generating personalized AI outreach

---

# Key Features

## Conversational AI CRM Copilot

The system accepts natural language requests such as:

```text
Find high-value customers likely to convert for a personal loan this month and generate personalized WhatsApp outreach.
```

The AI agent dynamically:

* identifies campaign intent
* generates execution plan
* orchestrates workflow execution
* retrieves relevant customer data
* analyzes transaction intelligence
* estimates conversion probability
* recommends products
* generates personalized outreach messages

---

# Expected Capabilities Covered

| Capability                             | Status |
| -------------------------------------- | ------ |
| Retrieve customer and transaction data | ✅      |
| Identify high-value customers          | ✅      |
| Estimate conversion likelihood         | ✅      |
| Recommend suitable products            | ✅      |
| Generate personalized outreach         | ✅      |
| Structured reasoning flow              | ✅      |
| Tool orchestration                     | ✅      |
| Stateful workflow execution            | ✅      |
| Modular architecture                   | ✅      |

---

# Tech Stack

## Backend

* FastAPI
* LangGraph
* LangChain
* Groq LLM
* SQLAlchemy
* SQLite
* Pydantic

## Frontend

* React
* TailwindCSS
* shadcn/ui
* Framer Motion

## AI / LLM

* Groq API
* llama-3.3-70b-versatile

---

# High-Level Architecture

```text
                      User Query
                           ↓
                Conversational AI Agent
                           ↓
                  Intent Analysis Agent
                           ↓
                Customer Retrieval Agent
                           ↓
               Transaction Analysis Agent
                           ↓
              Customer Intelligence Agent
                           ↓
               Conversion Scoring Agent
                           ↓
             Product Recommendation Agent
                           ↓
               Outreach Generation Agent
                           ↓
               Response Generation Agent
                           ↓
                 Final CRM Response
```

---

# Agentic Workflow

The project uses LangGraph for stateful orchestration.

Each node in the workflow performs a specific responsibility.

## Workflow Nodes

### 1. Intent Analysis Agent

Responsible for:

* understanding user intent
* identifying campaign type
* generating execution plan
* generating reasoning steps

Example:

```text
Personal Loan Campaign
Wealth Management Campaign
Credit Card Upgrade Campaign
```

---

### 2. Customer Retrieval Agent

Retrieves:

* customer profiles
* financial metadata
* relationship information

Filters:

* salary
* credit score
* account balance
* relationship duration

---

### 3. Transaction Analysis Agent

Analyzes:

* salary credit patterns
* EMI repayment activity
* investment behavior
* spending trends
* transaction frequency

Generates:

```json
{
  "salary_credit_frequency": 4,
  "investment_activity": 5,
  "emi_payment_count": 2,
  "total_debit_spend": 850000
}
```

---

### 4. Customer Intelligence Agent

Enriches customer profiles using:

* transaction behavior
* financial activity
* banking relationship strength
* repayment history

Generates customer insights such as:

```text
- strong credit profile
- active transaction behavior
- long-standing banking relationship
- positive repayment history
```

---

### 5. Conversion Scoring Agent

Uses heuristic-based scoring.

Factors include:

| Signal                    | Weight |
| ------------------------- | ------ |
| High salary               | +30    |
| Strong credit score       | +30    |
| High balance              | +20    |
| Active banking behavior   | +10    |
| Long banking relationship | +10    |

Final customers are ranked using conversion scores.

---

### 6. Product Recommendation Agent

Recommends products dynamically.

Examples:

| Customer Type          | Recommendation        |
| ---------------------- | --------------------- |
| High-income salaried   | Premium Personal Loan |
| Affluent investor      | Wealth Advisory       |
| High-spending customer | Premium Credit Card   |

---

### 7. Outreach Generation Agent

Uses Groq LLM to generate:

* personalized WhatsApp messages
* customer-aware outreach
* financial-context personalization

Example:

```text
Hi Rahul, based on your strong repayment history and active banking relationship with us, you may be eligible for a pre-approved premium personal loan tailored for working professionals.
```

---

# State Management

The project uses centralized workflow state.

Example:

```python
class CRMState(TypedDict):

    user_query: str

    execution_plan: Dict[str, Any]

    reasoning_steps: List[str]

    customers: List[Dict[str, Any]]

    scored_customers: List[Dict[str, Any]]

    recommendations: List[Dict[str, Any]]

    outreach_messages: List[Dict[str, Any]]

    final_response: Dict[str, Any]
```

This enables:

* stateful orchestration
* modular workflow execution
* explainability
* traceability

---

# Folder Structure

```text
banking-agentic-crm/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── config/
│   │   ├── database/
│   │   ├── prompts/
│   │   ├── services/
│   │   ├── tools/
│   │   └── main.py
│   │
│   ├── diagrams/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── package.json
│
└── README.md
```

---

# API Endpoint

## Analyze Customers

### Endpoint

```http
POST /analyze-customers
```

### Request

```json
{
  "query": "Find high-value customers likely to convert for personal loans this month and generate personalized WhatsApp outreach"
}
```

---

# Example Response

```json
{
  "query": "Find high-value customers likely to convert for personal loans",

  "execution_plan": {
    "campaign_intent": "Personal Loan Campaign",
    "target_customer_segment": "High-income salaried professionals"
  },

  "reasoning_steps": [
    "Analyzed customer financial profiles",
    "Identified strong repayment behavior",
    "Estimated conversion likelihood"
  ],

  "high_potential_customers": [
    {
      "name": "Rahul Sharma",
      "conversion_score": 92,
      "recommended_product": "Premium Personal Loan",
      "personalized_message": "Hi Rahul, based on your strong banking relationship and repayment history..."
    }
  ]
}
```

---

# Setup Instructions

## Clone Repository

```bash
git clone <repository-url>
```

---

# Backend Setup

## Navigate to backend

```bash
cd backend
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

---

# Seed Database

```bash
python -m app.database.seed
```

---

# Run Backend

```bash
uvicorn app.main:app --reload
```

API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

## Navigate to frontend

```bash
cd frontend
```

## Install Dependencies

```bash
npm install
```

## Run Frontend

```bash
npm run dev
```

---

# Demo Use Cases

## Use Case 1 — Personal Loan Campaign

### Query

```text
Find high-value customers likely to convert for a personal loan this month and generate personalized outreach.
```

### Demonstrates

* conversion scoring
* customer filtering
* personalized outreach

---

## Use Case 2 — Wealth Management Campaign

### Query

```text
Identify affluent customers with strong investment activity who may be interested in wealth management products and generate personalized outreach.
```

### Demonstrates

* investment intelligence
* transaction analysis
* premium customer segmentation

---

## Use Case 3 — Credit Card Upgrade Campaign

### Query

```text
Find customers with high monthly spending patterns suitable for premium credit card upgrades and generate personalized campaigns.
```

### Demonstrates

* transaction intelligence
* spending behavior analysis
* lifestyle-based recommendations

---

# Workflow Visualization

Workflow diagrams are automatically generated using LangGraph.

Generate diagram:

```bash
python -m app.agents.workflow
```

Diagram output:

```text
diagrams/langgraph_workflow.png
```

---

# Design Decisions

## Why LangGraph?

Chosen because:

* supports stateful orchestration
* modular node-based execution
* ideal for agentic systems
* enables workflow visualization
* easier debugging and extensibility

---

## Why Heuristic Scoring Instead of ML?

Chosen because:

* faster prototyping
* easier explainability
* transparent business logic
* simpler evaluation workflow
* suitable for assignment scope

---

## Why Groq?

Chosen because:

* fast inference speed
* free developer tier
* strong LLM performance
* easy LangChain integration

---

# Tradeoffs

| Decision              | Tradeoff                                                    |
| --------------------- | ----------------------------------------------------------- |
| Heuristic scoring     | Simpler but less adaptive than ML                           |
| SQLite                | Lightweight but not horizontally scalable                   |
| Synthetic data        | Good for demo but not real banking production data          |
| Single workflow graph | Easier orchestration but limited multi-agent specialization |

---

# Future Improvements

Potential future enhancements:

* real-time streaming workflows
* multi-agent orchestration
* vector memory for long conversations
* CRM integration (Salesforce/Dynamics)
* advanced ML conversion prediction
* customer churn prediction
* multilingual outreach generation
* campaign analytics dashboard
* human approval workflow before outreach

---

# Screenshots

Add:

* frontend dashboard
* workflow visualization
* Swagger API
* customer recommendation cards
* WhatsApp outreach UI

---

# Author

Built as part of an Agentic AI Banking CRM assignment focused on:

* agentic reasoning
* workflow orchestration
* transaction intelligence
* personalized AI outreach
* modular AI system design
