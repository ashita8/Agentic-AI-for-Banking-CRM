from app.services.customer_service import get_high_value_customers

def fetch_high_value_customers(
    minimum_salary: int,
    minimum_credit_score: int
):

    return get_high_value_customers(
        minimum_salary,
        minimum_credit_score
    )