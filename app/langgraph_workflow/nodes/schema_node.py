from app.services.neo4j_servive import Neo4jService

neo4j_service = Neo4jService()

def schema_node(state):

    schema = neo4j_service.get_schema_context()

    state["schema"] = schema

    return state