from app.services.llm_service import ask_llm

def generate_response(question, result):

    prompt = f"""
    User Question:
    {question}

    SQL Result:
    {result}

    Generate business-friendly response.
    """

    return ask_llm(prompt)