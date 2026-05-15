from app.services.customer_intelligence_service import (
    generate_customer_insights
)


def enrich_customer_profiles(
    customers
):

    enriched = []

    for customer in customers:

        insights = (
            generate_customer_insights(
                customer
            )
        )

        enriched.append({
            **customer,
            "customer_insights": insights
        })

    return enriched