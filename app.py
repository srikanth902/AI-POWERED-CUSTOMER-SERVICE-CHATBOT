import streamlit as st
from model.chatbot_model import generate_response

st.set_page_config(page_title="AI Customer Service Chatbot")
st.title("🤖 AI-Powered Customer Service Chatbot")

user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Thinking..."):
        reply = generate_response(user_input)
        st.markdown(f"**Bot:** {reply}")
