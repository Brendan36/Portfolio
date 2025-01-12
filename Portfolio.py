import streamlit as st
import pandas as pd
from streamlit import empty

st.set_page_config(layout="wide")

# st.title("Hi, I’m Brendan!")
# # st.write("Hi, I’m Brendan!\n")
# col1, col2 = st.columns(2)
# with col1:
#     st.image('images/blue smiley.jpg')
# with col2:
#     content = """
#     An endlessly curious, hands-on creator who considers himself to be imaginative and loves to tinker with Python and R
#     to uncover deeper insights through data.\n
#
#     My growing passion for animal welfare, environmental stewardship, and human rights,
#     has inspired me to continuously develop tools designed to illuminate the subtle links between our
#     everyday habits and their global ripple effects.\n
#     My goal is to help us recognize how even small actions can influence the world around us...
#     these same actions which are either helping it thrive or contributing to its decline.\n
#
#     By sharpening our self-awareness, we can better understand how individual choices add up and,
#     more importantly, what steps we can take to inspire positive change.
#     I’m eager for these tools to become a starting point for meaningful transformation
#     —but that can only happen when people put them to use.\n
#
#     If you have ideas, improvements, or new feature suggestions, I’d love to hear from you!\n
#     """
#     st.write(content)
#
# mission_statement = """
#     Mission Statement
#     """
# st.header(mission_statement, divider='rainbow')
#
# blurb = """
#     To inspire global collaboration so that we can all broaden our understanding of, and fuel the shifts that matter most.\n
#
#     Let’s create a better world together!\n
#
#     I intend to work with you to build **be**, an application that will be able to:\n
#
#     1. Debunk the correlation between "sustainability" and the actual impact of the continuous commercialization of natural resources on the world.\n
#     2. Improve our understanding of the success stories of collectives and individuals who have extensively researched viable alternatives and have them implemented.\n
#     3. Provide insights into the financial results of industries involved and by virtue, their impact while shining light on the environmental cost... \n
#     4. Enable peer-to-peer collaboration and resource pooling to empower new community driven sustainable alternatives for the future. \n
#     5. Demonstrate the power of collective action so we can easily quantify our collective impact and see the changes we are making in our world.\n
#     **You might ask why... and my reason is that I've come to realise that we cannot rely on the current capitalism driven global industries to do right by us... It's simply not profitable for them.**
#
#     """
# st.write(blurb)
#
#

st.title("Projects")

# content2 = """
#     Some of my current projects:
#     """
# st.header(content2)

df = pd.read_csv('portfolio_data.csv', sep=';')  # read the csv file
# st.table(df)

col5, empty_col, col6 = st.columns([1.5, 0.1, 1.5])
with col5:
    for i, row in df[:10].iterrows():
        st.subheader("", divider='rainbow')
        st.subheader(row['title'], divider='rainbow')
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col6:
    for i, row in df[10:20].iterrows():
        st.subheader("", divider='rainbow')

        st.subheader(row['title'], divider='rainbow')
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")


# content3 = """
#     Here are some of the ideas I have in mind for future projects:
#     """
# st.header(content3)
# for i, row in df[20:].iterrows():
#     st.subheader("", divider='rainbow')
#     st.subheader(row['title'])
#     st.write(row['description'])
#     st.image("images/" + row['image'])
# st.subheader("", divider='rainbow')



