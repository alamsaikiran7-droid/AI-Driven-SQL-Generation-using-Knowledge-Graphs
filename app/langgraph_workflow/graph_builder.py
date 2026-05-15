from langgraph.graph import StateGraph, END

from app.langgraph_workflow.state import GraphState

from app.langgraph_workflow.nodes.schema_node import schema_node
from app.langgraph_workflow.nodes.sql_node import sql_node
from app.langgraph_workflow.nodes.validation_node import validation_node
from app.langgraph_workflow.nodes.execution_node import execution_node
from app.langgraph_workflow.nodes.response_node import response_node

def build_graph():

    workflow = StateGraph(GraphState)

    workflow.add_node("schema", schema_node)
    workflow.add_node("sql", sql_node)
    workflow.add_node("validate", validation_node)
    workflow.add_node("execute", execution_node)
    workflow.add_node("response", response_node)

    workflow.set_entry_point("schema")

    workflow.add_edge("schema", "sql")
    workflow.add_edge("sql", "validate")
    workflow.add_edge("validate", "execute")
    workflow.add_edge("execute", "response")
    workflow.add_edge("response", END)

    return workflow.compile()