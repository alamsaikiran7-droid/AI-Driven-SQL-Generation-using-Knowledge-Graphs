from sqlalchemy import text
from app.database.mysql.db import engine

def execute_query(query):

    with engine.connect() as conn:

        result = conn.execute(text(query))

        rows = result.fetchall()

        return [dict(row._mapping) for row in rows]