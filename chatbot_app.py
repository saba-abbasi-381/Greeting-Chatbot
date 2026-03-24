import streamlit as st
from chatbot import greeting_chatbot

st.title("Greeting Chatbot")
msg = st.text_input("Please enter a message: ").lower().strip()

if st.button("Send"):
    if msg:
        response = greeting_chatbot(msg)
        st.write(response)
    else:
        st.error("Please enter a message!")