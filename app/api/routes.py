from fastapi import APIRouter

from app.schema.request_schema import CustomerAnalysisRequest

from app.agents.state import CRMState
from app.agents.planner import identify_intent

router = APIRouter()


@router.post("/analyze-customers")
def analyze_customers(request: CustomerAnalysisRequest):

    intent = identify_intent(request.query)

    state: CRMState = {
        "user_query": request.query,
        "identified_intent": intent,
        "reasoning_steps": [],
        "customers": [],
        "scored_customers": [],
        "recommendations": [],
        "outreach_messages": [],
        "final_response": {}
    }

    return {
        "message": "Agent workflow initialized",
        "identified_intent": intent,
        "state": state
    }