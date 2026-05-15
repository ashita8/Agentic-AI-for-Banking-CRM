from fastapi import APIRouter

from app.tools.customer_tool import fetch_high_value_customers
from app.tools.scoring_tool import rank_customers

router = APIRouter()

@router.post("/analyze-customers")
def analyze_customers():

    customers = fetch_high_value_customers()

    ranked = rank_customers(customers)

    return ranked[:10]