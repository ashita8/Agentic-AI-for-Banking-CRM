def generate_customer_insights(
    customer
):

    insights = []

    if customer["salary"] > 150000:
        insights.append(
            "high monthly income"
        )

    if customer["credit_score"] > 750:
        insights.append(
            "strong credit profile"
        )

    if customer[
        "relationship_years"
    ] > 5:
        insights.append(
            "long-standing banking relationship"
        )

    if customer[
        "monthly_avg_transactions"
    ] > 80:
        insights.append(
            "active transaction behavior"
        )

    if customer[
        "last_loan_status"
    ] == "Closed Successfully":
        insights.append(
            "positive previous loan repayment history"
        )

    return insights