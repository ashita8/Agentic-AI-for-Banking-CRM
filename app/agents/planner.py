def identify_intent(query: str) -> str:

    query = query.lower()

    if "personal loan" in query:
        return "PERSONAL_LOAN_CAMPAIGN"

    if "investment" in query:
        return "INVESTMENT_CAMPAIGN"

    return "GENERAL_CUSTOMER_ANALYSIS"