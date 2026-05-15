def add_reasoning_step(state, step: str):

    state["reasoning_steps"].append(step)

    return state