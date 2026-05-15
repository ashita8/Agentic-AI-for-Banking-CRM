from app.services.customer_service import get_high_value_customers


def fetch_high_value_customers(intent: str):

    if intent == "PERSONAL_LOAN_CAMPAIGN":

        minimum_salary = 100000
        minimum_credit_score = 720

    elif intent == "INVESTMENT_CAMPAIGN":

        minimum_salary = 200000
        minimum_credit_score = 750

    else:

        minimum_salary = 80000
        minimum_credit_score = 700

    return get_high_value_customers(
        minimum_salary,
        minimum_credit_score
    )