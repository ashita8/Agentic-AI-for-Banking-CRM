from langchain_groq import ChatGroq

from app.config.settings import (
    GROQ_API_KEY,
    MODEL_NAME
)

from app.prompts.message_prompts import (
    MESSAGE_PROMPT
)

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME
)


def generate_personalized_message(customer):

    prompt = MESSAGE_PROMPT.format(
    name=customer["name"],
    city=customer["city"],
    employment_type=customer[
        "employment_type"
    ],
    salary=customer["salary"],
    credit_score=customer[
        "credit_score"
    ],
    relationship_years=customer[
        "relationship_years"
    ],
    monthly_avg_transactions=customer[
        "monthly_avg_transactions"
    ],
    last_loan_status=customer[
        "last_loan_status"
    ],
    customer_insights=", ".join(
        customer["customer_insights"]
    ),
    recommended_product=customer[
        "recommended_product"
    ]
)

    response = llm.invoke(prompt)

    return response.content.strip()