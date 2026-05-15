from fastapi import APIRouter
from app.tools.customer_tool import fetch_high_value_customers

router = APIRouter()

@router.post("/analyze-customers")
def analyze_customers():

    customers = fetch_high_value_customers()

    return {
        "customers_found": len(customers)
    }