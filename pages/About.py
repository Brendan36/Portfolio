import base64
import streamlit as st
import pandas as pd
from streamlit import empty

st.set_page_config(layout="wide")

st.title("Hi, I’m Brendan!")
# st.write("Hi, I’m Brendan!\n")
col1, col2 = st.columns(2)
with col1:
    st.image('images/blue smiley.jpg')
with col2:
    content = """
    An endlessly curious, hands-on imaginative creator who loves to tinker with Python and R 
    to uncover deeper insights through data.\n
    
    My growing passion for animal welfare, environmental stewardship, and human rights, 
    has inspired me to develop tools that will be designed to illuminate the subtle links 
    between our everyday habits and their global ripple effects.\n
    My goal is to help us recognize how even small actions can influence the world around us... 
    these same actions which are either helping it thrive or contributing to its decline.\n
    
    By sharpening our self-awareness, we can better understand how individual choices add up and, 
    more importantly, what steps we can take to inspire positive change. 
    I’m eager for these tools to become a starting point for meaningful transformation
    —but that can only happen when people put them to use.\n
   
    If you have ideas or feature suggestions, I’d love to hear from you!\n
    """
    st.write(content)






# content2 = """
#     Here are a few of my current projects:
#     """
# st.header(content2)
#
df = pd.read_csv('portfolio_data.csv', sep=';')  # read the csv file
# # st.table(df)
#
# col5, empty_col, col6 = st.columns([1.5, 0.1, 1.5])
# with col5:
#     for i, row in df[:10].iterrows():
#         st.subheader("", divider='rainbow')
#         st.subheader(row['title'], divider='rainbow')
#         st.write(row['description'])
#         st.image("images/" + row['image'])
#         st.write(f"[Source Code]({row['url']})")
#
# with col6:
#     for i, row in df[10:20].iterrows():
#         st.subheader("", divider='rainbow')
#
#         st.subheader(row['title'], divider='rainbow')
#         st.write(row['description'])
#         st.image("images/" + row['image'])
#         st.write(f"[Source Code]({row['url']})")
#
#

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
# with col3:
#     st.subheader("Did You Know..?")
#     st.info(dyk2)
#
# with col4:
#     st.subheader("Did You Know..?")
#     st.info(dyk1)

# audio_file_path = "C:/Users/Dell/PycharmProjects/app2-portfolio/We Deserve To Dream.mp3"
# with open(audio_file_path, "rb") as f:
#     audio_bytes = f.read()
#     audio_base64 = base64.b64encode(audio_bytes).decode()
#
# audio_player_base64 = f"""
#     <audio autoplay loop controls>
#         <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
#     </audio>
# """
# st.markdown(audio_player_base64, unsafe_allow_html=True)
# st.write("**Artist: Xavier Rudd - We Deserve to Dream**")

mission_statement = """
    Mission
    """
st.header(mission_statement, divider='rainbow')

blurb = """
    To inspire global collaboration so that we can all broaden our understanding of, and fuel the shifts that matter most.\n

    Let’s create a better world together!\n

    I intend to work with you to build **| be |** a suite of applications that will be able to:\n

    1. Debunk the correlation between actual impact of the continuous commercialization of natural resources on the world and "sustainable" practices.\n
    2. Improve our understanding of the success stories of collectives and individuals who have extensively researched viable alternatives and have them implemented.\n
    3. Provide insights into the financial results of industries involved and by virtue, their impact while shining light on the environmental cost.\n
    4. Enable peer-to-peer collaboration and resource pooling while educating communities for support to empower new initiatives using sustainable alternatives to better the future. \n
    5. Demonstrate the power of collective action so we can easily quantify our impact and see the changes we are making in our world while enabling the mechanism so we all have a say in our own future in pursuit of a better world utilizing the power of collective kindness.\n
    """
#     **You might ask why... and my reason is that I've come to realise that we cannot rely on the current capitalism driven global industries to do right by us... It's simply not profitable for them.**
st.write(blurb)


content3 = """
    | be | think-tank items
    """
st.subheader("", divider='rainbow')
st.header(content3)
for i, row in df[20:].iterrows():
    st.subheader("", divider='rainbow')
    st.subheader(row['title'])
    st.write(row['description'])
    st.image("images/" + row['image'])
st.subheader("", divider='rainbow')