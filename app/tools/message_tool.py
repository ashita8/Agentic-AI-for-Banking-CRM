from app.services.message_service import (
    generate_personalized_message
)


def create_outreach_messages(
    recommendations
):

    outreach_messages = []

    for customer in recommendations[:5]:

        message = generate_personalized_message(
            customer
        )

        outreach_messages.append({
            **customer,
            "personalized_message": message
        })

    return outreach_messages