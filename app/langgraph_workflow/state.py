from typing import TypedDict, Any

class GraphState(TypedDict):

    question: str
    schema: Any
    sql_query: str
    validated: bool
    sql_result: Any
    final_response: str