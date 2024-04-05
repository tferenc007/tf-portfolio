import streamlit as st
from send_email import send_email

st.header("Contact US")

with st.form(key="email_key"):
    user_email = st.text_input("your email address")
    row_message = st.text_area("Your message")
    message = f"""
Subject: new email from {user_email}
From: {user_email}
{row_message}
"""
    button = st.form_submit_button()
    if button:
        print ("I was pressed!")
        send_email(message)
        st.info("Your email was sent successfully")