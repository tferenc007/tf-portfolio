import streamlit as st
from send_email import send_email

st.header("Contact US")

with st.form(key="email_key"):
    user_email = st.text_input("your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button()
    if button:
        print ("I was pressed!")
        send_email(message)