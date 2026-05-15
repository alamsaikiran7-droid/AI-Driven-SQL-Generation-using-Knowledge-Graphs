from app.database.mysql.db import engine
from sqlalchemy import text

try:

    with engine.connect() as conn:

        result = conn.execute(
            text("SELECT 1")
        )

        print("MySQL Connected Successfully")

except Exception as e:
    print("Connection Failed")
    print(e)