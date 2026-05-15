from neo4j import GraphDatabase
from app.config.settings import settings

class Neo4jService:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(
                settings.NEO4J_USERNAME,
                settings.NEO4J_PASSWORD
            )
        )

    def get_schema_context(self):

        query = """
        MATCH (t:Table)-[:HAS_COLUMN]->(c:Column)
        RETURN t.name AS table, collect(c.name) AS columns
        """

        with self.driver.session() as session:
            result = session.run(query)

            schema = []

            for record in result:
                schema.append({
                    "table": record["table"],
                    "columns": record["columns"]
                })

            return schema