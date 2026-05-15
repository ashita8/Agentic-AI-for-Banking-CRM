def calculate_conversion_score(customer: dict):

    score = 0

    if customer["salary"] > 150000:
        score += 30

    if customer["credit_score"] > 750:
        score += 30

    if customer["account_balance"] > 300000:
        score += 20

    if 25 <= customer["age"] <= 45:
        score += 20

    return score