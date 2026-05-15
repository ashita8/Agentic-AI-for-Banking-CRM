from langgraph.graph import StateGraph, END

from app.agents.state import CRMState
from app.agents.reasoning import add_reasoning_step

from app.agents.planner import identify_intent

from app.tools.customer_tool import fetch_high_value_customers
from app.tools.scoring_tool import rank_customers
from app.tools.recommendation_tool import generate_recommendations


def planner_node(state: CRMState):

    execution_plan = identify_intent(
        state["user_query"]
    )

    state["execution_plan"] = execution_plan

    state["reasoning_steps"] = execution_plan[
        "reasoning"
    ]

    return state


def customer_retrieval_node(state: CRMState):

    customers = fetch_high_value_customers(
    state["execution_plan"]["campaign_intent"]
    )

    serialized_customers = []

    for customer in customers:

        serialized_customers.append({
            "name": customer.name,
            "salary": customer.salary,
            "credit_score": customer.credit_score,
            "account_balance": customer.account_balance,
            "age": customer.age
        })

    state["customers"] = serialized_customers

    add_reasoning_step(
        state,
        f"Retrieved {len(serialized_customers)} high-value customer profiles"
    )

    return state


def scoring_node(state: CRMState):

    ranked_customers = rank_customers(
        state["customers"]
    )

    state["scored_customers"] = ranked_customers

    add_reasoning_step(
        state,
        "Calculated conversion likelihood scores using heuristic analysis"
    )

    return state


def recommendation_node(state: CRMState):

    recommendations = generate_recommendations(
        state["scored_customers"]
    )

    state["recommendations"] = recommendations

    add_reasoning_step(
        state,
        "Generated product recommendations based on customer financial profiles"
    )

    return state


def response_node(state: CRMState):

    state["final_response"] = {
        "query": state["user_query"],

        "identified_intent": state["execution_plan"]["campaign_intent"],

        "reasoning_steps": state["reasoning_steps"],

        "high_potential_customers": state["recommendations"][:5]
    }

    return state

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

workflow.add_edge(
    "customer_retrieval",
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

workflow.add_edge(
    "response",
    END
)

crm_workflow = workflow.compile()