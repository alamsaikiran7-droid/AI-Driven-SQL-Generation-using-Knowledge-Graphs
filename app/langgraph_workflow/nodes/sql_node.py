from app.services.sql_generator import generate_sql

def sql_node(state):

    sql = generate_sql(
        state["question"],
        state["schema"]
    )

    state["sql_query"] = sql

    return state