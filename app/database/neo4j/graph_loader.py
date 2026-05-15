from neo4j import GraphDatabase

class GraphLoader:

    def __init__(self, driver):
        self.driver = driver

    def load_schema(self):

        sample_schema = {
            "customers": ["customer_id", "name", "email"],
            "orders": ["order_id", "customer_id", "amount"]
        }

        with self.driver.session() as session:

            for table, columns in sample_schema.items():

                session.run(
                    "MERGE (t:Table {name:$table})",
                    table=table
                )

                for col in columns:

                    session.run(
                        """
                        MATCH (t:Table {name:$table})
                        MERGE (c:Column {name:$col})
                        MERGE (t)-[:HAS_COLUMN]->(c)
                        """,
                        table=table,
                        col=col
                    )