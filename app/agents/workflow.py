from langgraph.graph import StateGraph, END

from app.agents.state import CRMState
from app.agents.reasoning import add_reasoning_step

from app.agents.planner import identify_intent

from app.tools.customer_tool import fetch_high_value_customers
from app.tools.scoring_tool import rank_customers
from app.tools.recommendation_tool import generate_recommendations
from app.tools.message_tool import (
    create_outreach_messages
)
from app.tools.customer_intelligence_tool import (
    enrich_customer_profiles
)
def planner_node(state: CRMState):

    execution_plan = identify_intent(
        state["user_query"]
    )

    return {
        "execution_plan": execution_plan,
        "reasoning_steps": execution_plan[
            "reasoning"
        ]
    }


def customer_retrieval_node(
    state: CRMState
):

    customers = fetch_high_value_customers(
        state["execution_plan"][
            "campaign_intent"
        ]
    )

    serialized_customers = []

    for customer in customers:

        serialized_customers.append({
        "name": customer.name,

        "salary": customer.salary,

        "credit_score": customer.credit_score,

        "account_balance": customer.account_balance,

        "age": customer.age,

        "employment_type": customer.employment_type,

        "city": customer.city,

        "relationship_years": customer.relationship_years,

        "monthly_avg_transactions":
            customer.monthly_avg_transactions,

        "last_loan_status":
            customer.last_loan_status
    })

    return {
        "customers": serialized_customers
    }
def scoring_node(state: CRMState):

    ranked_customers = rank_customers(
        state["customers"]
    )

    return {
        "scored_customers": ranked_customers
    }


def recommendation_node(
    state: CRMState
):

    recommendations = (
        generate_recommendations(
            state["scored_customers"]
        )
    )

    return {
        "recommendations": recommendations
    }

def outreach_generation_node(
    state: CRMState
):

    outreach_messages = (
        create_outreach_messages(
            state["recommendations"]
        )
    )

    return {
        "outreach_messages": outreach_messages
    }

def customer_intelligence_node(
    state: CRMState
):

    enriched_customers = (
        enrich_customer_profiles(
            state["customers"]
        )
    )

    return {
        "customers": enriched_customers
    }

def response_node(state: CRMState):

    return {
        "final_response": {
            "query": state["user_query"],

            "execution_plan": state[
                "execution_plan"
            ],

            "reasoning_steps": state[
                "reasoning_steps"
            ],

            "high_potential_customers":
                state["outreach_messages"]
        }
    }

workflow = StateGraph(CRMState)

workflow.add_node(
    "planner",
    planner_node
)

workflow.add_node(
    "customer_retrieval",
    customer_retrieval_node
)

workflow.add_node(
    "scoring",
    scoring_node
)

workflow.add_node(
    "recommendation",
    recommendation_node
)

workflow.add_node(
    "response",
    response_node
)

workflow.set_entry_point("planner")

workflow.add_edge(
    "planner",
    "customer_retrieval"
)
workflow.add_node(
    "customer_intelligence_agent",
    customer_intelligence_node
)
workflow.add_edge(
    "customer_retrieval",
    "customer_intelligence_agent"
)

workflow.add_edge(
    "customer_intelligence_agent",
    "scoring"
)

workflow.add_edge(
    "scoring",
    "recommendation"
)

workflow.add_edge(
    "recommendation",
    "response"
)
workflow.add_node(
    "outreach_generation_agent",
    outreach_generation_node
)
workflow.add_edge(
    "recommendation",
    "outreach_generation_agent"
)

workflow.add_edge(
    "outreach_generation_agent",
    "response"
)


workflow.add_edge(
    "response",
    END
)

crm_workflow = workflow.compile()

from pathlib import Path


def save_workflow_diagram():

    diagram_path = Path(
        "diagrams/langgraph_workflow.png"
    )

    diagram_path.parent.mkdir(
        exist_ok=True
    )

    png_graph = crm_workflow.get_graph().draw_mermaid_png()

    with open(diagram_path, "wb") as file:
        file.write(png_graph)

    print(
        f"Workflow diagram saved to {diagram_path}"
    )


if __name__ == "__main__":

    save_workflow_diagram()