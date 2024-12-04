import streamlit as st
from chatbot import get_answer

# Streamlit app
st.title("College FAQ Chatbot")
st.write("Ask questions about our college!")

# Input from user
user_question = st.text_input("Enter your question:")

# Display answer
if user_question:
    answer = get_answer(user_question)
    st.write("Answer:", answer)
