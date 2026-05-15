from app.services.recommendation_service import recommend_loan_product

def generate_recommendations(ranked_customers):

    recommendations = []

    for item in ranked_customers:

        product = recommend_loan_product(
            item,
            item["score"]
        )

        recommendations.append({
            **item,
            "recommended_product": product
        })

    return recommendations