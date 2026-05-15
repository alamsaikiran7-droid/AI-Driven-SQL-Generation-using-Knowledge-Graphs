from app.services.sql_validator import validate_sql

def validation_node(state):

    valid = validate_sql(state["sql_query"])

    state["validated"] = valid

    return state