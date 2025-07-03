import streamlit as st
import requests

st.set_page_config(page_title="TailorTalk AI Assistant", layout="centered")

st.title(" TailorTalk Booking Assistant")
st.write("Your AI-powered calendar assistant. Ask me to schedule a meeting!")

#  Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

backend_url = "http://localhost:8000/chat"  #  Replace with live URL on deployment

#  Chat input box
user_input = st.chat_input("Say something like 'Book a meeting tomorrow at 4PM'...")

if user_input:
    st.session_state.messages.append(("user", user_input))

    with st.spinner("Thinking..."):
        try:
            res = requests.post(backend_url, json={"message": user_input})
            bot_reply = res.json().get("reply", "Something went wrong.")
        except:
            bot_reply = " Backend not reachable. Please check connection."

    st.session_state.messages.append(("bot", bot_reply))

#  Display the conversation
for sender, msg in st.session_state.messages:
    if sender == "user":
        with st.chat_message("user"):
            st.markdown(msg)
    else:
        with st.chat_message("assistant"):
            st.markdown(msg)
