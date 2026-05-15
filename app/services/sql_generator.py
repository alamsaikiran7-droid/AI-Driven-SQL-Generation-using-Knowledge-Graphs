from app.services.llm_service import ask_llm
from app.services.prompt_service import build_sql_prompt

def generate_sql(question, schema):

    prompt = build_sql_prompt(question, schema)

    sql = ask_llm(prompt)

    return sql