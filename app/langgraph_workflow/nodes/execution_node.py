from app.services.mysql_service import execute_query

def execution_node(state):

    if state["validated"]:

        result = execute_query(state["sql_query"])

        state["sql_result"] = result

    else:
        state["sql_result"] = "Invalid SQL"

    return state