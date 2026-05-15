from app.services.scoring_service import calculate_conversion_score


def rank_customers(customers):

    ranked = []

    for customer in customers:

        score = calculate_conversion_score(customer)

        ranked.append({
            **customer,
            "conversion_score": score
        })

    return sorted(
        ranked,
        key=lambda x: x["conversion_score"],
        reverse=True
    )