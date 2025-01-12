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

# Display the form

# st.header("IMO...", divider='rainbow')
# st.write("**MOST** commercial industries are not sustainable - Do you want to help us see past cute and often misleading labels?")
# st.write("**PEOPLE** should have access to alternative options - Do you intend to enable those options?")
# st.write("**ARE** we really doing the best we can? - Do you want to help us realise what we are doing?")
# st.write(
#     "**IGNORANT** is what we are if, we blindly trust and support commercial industries (many of them only perpetuate the problems) - Do you want to finance the destruction of the planet?")
# st.write("**TO** become sustainable, we need to inspire others to take action through doing it ourselves - Do you want to maintain your blanket of cognitive ambivalence?")
# st.write("**CHANGE** is the only realistic option we have left - it's only too late when we're dead... - Do you want to wait?")
# st.write("**IN REALITY** we need to stop supporting industries that are intentionally misleading us - I want create and easier way to know that - Do you want to know?")
#
# st.subheader("What do you intend to do?", divider='rainbow')
# col3, empty_col, col4 = st.columns([1.5, 0.1, 1.5])
#
# dyk1 = """
#     A commercially packed 1.5kg chicken requires 5kg of feed.\n
#     KFC's Thai restaurant chain serves approximately 800,000 pieces of fried chicken daily, or 292 million pieces per year. \n
#     (assuming 8pieces = 1 chicken) - That's equivalent to 100,000 chickens per day or 3,000,000 chickens per year. \n
#     assuming 1 chicken = 1.5 kg of meat\n
#     it takes 550,000kg of feed (550 ton) to produce the 100,000 (150 ton) chickens that are sold daily.\n
#     \n
#     400,000kg of feed = 400 tons of produce which was lost in the conversion process.\n
#     \n
#     **Is this sustainable?**
#
#     """
#
# dyk2 = """
#     To produce 1 kg of beef: 13–15 kg of feed (forage + grain) is required.\n
#     15,000 liters of water (for feed production, drinking water, and processing).\n
#     -> **! That's 15,000 liters of water for 1 kg of beef !** <-   **WHY DO WE SUPPORT THIS?**\n
#
#     FYI: These numbers are based on the Average Feed Requirements for rearing cattle:\n
#
#     We've assumed that 8 kg of feed per 1 kg of live weight gain for a typical beef cattle.
#     Since only 60% of live weight translates to edible meat, the adjusted FCR is approximately:\n
#     8kg feed / 0.6 (meat yield factor) = 13.33kg feed for 1kg beef.
#     \n
#     **Is this sustainable?**
#     """
#
#
# with col3:
#     st.subheader("Did You Know..?")
#     st.info(dyk2)
#
# with col4:
#     st.subheader("Did You Know..?")
#     st.info(dyk1)

