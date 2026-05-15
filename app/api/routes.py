from fastapi import APIRouter
from pydantic import BaseModel

from app.langgraph_workflow.graph_builder import build_graph

router = APIRouter()

graph = build_graph()

class QueryRequest(BaseModel):
    question: str

@router.post("/ask")

def ask_question(request: QueryRequest):

    result = graph.invoke({
        "question": request.question
    })

    return {
        "sql_query": result["sql_query"],
        "response": result["final_response"]
    }