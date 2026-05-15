from app.services.recommendation_service import recommend_loan_product


def generate_recommendations(scored_customers):

    recommendations = []

    for customer in scored_customers:

        product = recommend_loan_product(
            customer,
            customer["conversion_score"]
        )

        recommendations.append({
            **customer,
            "recommended_product": product
        })

    return recommendations