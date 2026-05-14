import streamlit as st
from model import hybrid_rag

st.title("Conversational QA System")

question = st.text_input("Enter your question:")

if question:
    sample = {
        "Question": question,
        "Context": []
    }

    result = hybrid_rag(sample)

    st.subheader("Model Response:")
    st.write(result["prediction"])