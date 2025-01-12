import streamlit as st
import pandas as pd
import time
from send_mail import send_email

# Set the web page layout to wide
st.set_page_config(layout="wide")

# Page title and main header
st.title("Contact Me")
st.subheader("""
I look forward to hearing suggestions from you.
""")
st.write("""
If you'd like to reach out to me, please fill out the form below.
""")

df = pd.read_csv("topics.csv")

# Define the form
with st.form(key="contact_form"):
    guest_name = st.text_input("Name")
    email = st.text_input("Email")
    topic = st.selectbox("Please select a topic that you would like to discuss.", df["topic"])
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        # Send the email
        send_email(f"Subject: {topic.title()}\n\nFrom {guest_name}\nEmail address: {email}\n\n{message}")
        st.success("Thank you for your message! I'll get back to you as soon as I can.")
        time.sleep(3)  # Wait for 3 seconds
        st.rerun()  # Refresh the page to reset the form

