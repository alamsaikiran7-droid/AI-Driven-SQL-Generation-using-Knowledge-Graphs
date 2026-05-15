import sqlparse

FORBIDDEN = ["DROP", "DELETE", "TRUNCATE"]

def validate_sql(query):

    parsed = sqlparse.parse(query)

    if not parsed:
        return False

    upper_query = query.upper()

    for keyword in FORBIDDEN:
        if keyword in upper_query:
            return False

    return True