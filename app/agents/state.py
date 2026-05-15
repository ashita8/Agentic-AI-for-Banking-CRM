from typing import TypedDict, List, Dict, Any


class CRMState(TypedDict):

    user_query: str

    identified_intent: str

    reasoning_steps: List[str]

    customers: List[Dict[str, Any]]

    scored_customers: List[Dict[str, Any]]

    recommendations: List[Dict[str, Any]]

    outreach_messages: List[Dict[str, Any]]

    final_response: Dict[str, Any]