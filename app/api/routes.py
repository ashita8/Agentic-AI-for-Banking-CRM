from fastapi import APIRouter

from app.schema.request_schema import CustomerAnalysisRequest

from app.tools.customer_tool import fetch_high_value_customers
from app.tools.scoring_tool import rank_customers
from app.tools.recommendation_tool import generate_recommendations

router = APIRouter()

@router.post("/analyze-customers")
def analyze_customers(request: CustomerAnalysisRequest):

    customers = fetch_high_value_customers(
        request.minimum_salary,
        request.minimum_credit_score
    )

    ranked = rank_customers(customers)

    recommendations = generate_recommendations(ranked)

    return {
        "rm_query": request.query,
        "customers_found": len(recommendations),
        "results": recommendations[:request.top_k]
    }