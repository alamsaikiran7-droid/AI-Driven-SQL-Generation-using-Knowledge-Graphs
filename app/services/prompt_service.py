def build_sql_prompt(question, schema):

    return f"""
    You are an expert SQL generator.

    Database Schema:
    {schema}

    Convert the user question into SQL.

    Question:
    {question}

    Return only SQL query.
    """