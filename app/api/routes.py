from fastapi import APIRouter

from app.schema.request_schema import CustomerAnalysisRequest

from app.agents.workflow import crm_workflow

router = APIRouter()


@router.post("/analyze-customers")
def analyze_customers(request: CustomerAnalysisRequest):

    initial_state = {
        "user_query": request.query,
        "identified_intent": "",
        "reasoning_steps": [],
        "customers": [],
        "scored_customers": [],
        "recommendations": [],
        "outreach_messages": [],
        "final_response": {}
    }

    result = crm_workflow.invoke(
        initial_state
    )

    return result["final_response"]