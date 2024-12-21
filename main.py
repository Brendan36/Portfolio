import streamlit as st
import pandas as pd
from streamlit import empty

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image('images/blue smiley.jpg')
with col2:
    st.title("BE")
    content = """
    Hi, I’m Brendan!\n
    I’m an endlessly curious, imaginative hands-on creator who loves to tinker with Python and R 
    to uncover deeper insights through data.\n

    My growing passion for animal welfare, environmental stewardship, and human rights, 
    has inspired me to develop tools designed to illuminate the subtle links between our 
    everyday habits and their global ripple effects.\n
    My goal is to help us recognize how even small actions can influence the world around us... 
    these same actions which are either helping it thrive or contributing to its decline.\n

    By sharpening our self-awareness, we can better understand how individual choices add up and, 
    more importantly, what steps we can take to inspire positive change. 
    I’m eager for these tools to become a starting point for meaningful transformation
    —but that can only happen when people put them to use.\n

    While working together, we can all broaden our understanding and fuel the shifts that matter most.\n
    If you have ideas, improvements, or new feature suggestions, I’d love to hear from you!\n
    
    Let’s create a better world together!\n
    
    I intend to work with you to build TRUST, an application that:\n

    1. Debunks the correlation between "sustainability" and the actual impact of the commercialization of natural resources on the world.\n
    2. Improves our understanding of the success stories of collectives of individuals who have extensively researched viable alternatives.\n
    3. Provides insights into the financial results of industries involved and by virtue, their impact while shining light on the environmental cost... i.e. 3000 people could have eaten for a week by the food that given to 5000 chickens which were fed to 3000 people in 1 day \n
    4. 
    10. Demonstrates the power of collective action to change the world.\n
    
    """
    st.info(content)

content2 = """
    Here are a few of my completed projects:
    """
st.header(content2)

df = pd.read_csv('portfolio_data.csv', sep=';')  # read the csv file
# st.table(df)

col3, empty_col, col4 = st.columns([1.5, 0.1, 1.5])
with col3:
    for i, row in df[:10].iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for i, row in df[10:20].iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")


content3 = """
    Here are some of the ideas I have in mind for future projects:
    """
st.header(content3)
for i, row in df[20:].iterrows():
    st.subheader(row['title'])
    st.write(row['description'])
    st.image("images/" + row['image'])

