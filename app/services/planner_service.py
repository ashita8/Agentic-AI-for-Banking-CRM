import json

from langchain_groq import ChatGroq

from app.config.settings import (
    GROQ_API_KEY,
    MODEL_NAME
)

from app.prompts.planner_prompt import (
    PLANNER_PROMPT
)

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME
)


def generate_execution_plan(query: str):

    prompt = PLANNER_PROMPT.format(
        query=query
    )

    response = llm.invoke(prompt)

    content = response.content

    cleaned = content.replace(
        "```json",
        ""
    ).replace(
        "```",
        ""
    ).strip()

    return json.loads(cleaned)