from app.services.planner_service import (
    generate_execution_plan
)


def identify_intent(query: str):

    return generate_execution_plan(query)