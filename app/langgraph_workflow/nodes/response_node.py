from app.services.response_service import generate_response

def response_node(state):

    response = generate_response(
        state["question"],
        state["sql_result"]
    )

    state["final_response"] = response

    return state