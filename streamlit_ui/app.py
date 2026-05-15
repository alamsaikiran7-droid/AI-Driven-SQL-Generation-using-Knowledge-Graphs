import streamlit as st
import requests

st.title("AI SQL Generator")

question = st.text_input(
    "Ask Business Question"
)

if st.button("Generate"):

    response = requests.post(
        "http://localhost:8000/ask",
        json={"question": question}
    )

    data = response.json()

    st.subheader("Generated SQL")
    st.code(data["sql_query"])

    st.subheader("AI Response")
    st.write(data["response"])