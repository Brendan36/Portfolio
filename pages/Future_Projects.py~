import streamlit as st
import pandas as pd
from streamlit import empty
import base64


st.set_page_config(layout="wide")

df = pd.read_csv('portfolio_data.csv', sep=';')  # read the csv file

content3 = """
    Future project Ideas:
    """
st.header(content3)
for i, row in df[20:].iterrows():
    st.subheader("", divider='rainbow')
    st.subheader(row['title'])
    st.write(row['description'])
    st.image("images/" + row['image'])
st.subheader("", divider='rainbow')

st.header("IMO...", divider='rainbow')
st.write("**MOST** commercial industries are not sustainable - Do you want to help us see past cute and often misleading labels?")
st.write("**PEOPLE** should have access to alternative options - Do you intend to enable those options?")
st.write("**ARE** we really doing the best we can? - Do you want to help us realise what we are doing?")
st.write(
    "**IGNORANT** is what we are if, we blindly trust and support commercial industries (many of them only perpetuate the problems) - Do you want to finance the destruction of the planet?")
st.write("**TO** become sustainable, we need to inspire others to take action by doing it ourselves - Or do you want to maintain the blanket of cognitive ambivalence?")
st.write("**CHANGE** is the only realistic option we have left - it's only too late when we're dead... - Do you want to wait?")
st.write("**IN REALITY** we need to stop supporting industries that are intentionally misleading us - I want create and easier way to know that - Do you want to know?")

st.subheader("", divider='rainbow')

st.subheader("What will you do?")

# # Audio player section
# st.markdown(
#     """
#     <style>
#         .audio-controls {
#             display: flex;
#             justify-content: center;
#             margin-top: 10px;
#         }
#         .audio-button {
#             background-color: #008CBA;
#             color: white;
#             border: none;
#             padding: 10px 20px;
#             cursor: pointer;
#             font-size: 16px;
#             margin: 5px;
#             border-radius: 5px;
#         }
#         .audio-button:hover {
#             background-color: #006f8e;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
#
# # JavaScript and HTML for audio control
# audio_player_html = f"""
#     <div class="audio-controls">
#         <audio id="audio-player" autoplay loop>
#             <source src="file:///{'C:/Users/Dell/PycharmProjects/app2-portfolio/We Deserve To Dream.mp3'}" type="audio/mpeg">
#             Your browser does not support the audio element.
#         </audio>
#         <button class="audio-button" onclick="document.getElementById('audio-player').pause()">Mute</button>
#         <button class="audio-button" onclick="document.getElementById('audio-player').play()">Unmute</button>
#         <button class="audio-button" onclick="document.getElementById('audio-player').currentTime = 0; document.getElementById('audio-player').play()">Restart</button>
#     </div>
# """
# st.markdown(audio_player_html, unsafe_allow_html=True)

audio_file_path = "C:/Users/Dell/PycharmProjects/app2-portfolio/We Deserve To Dream.mp3"
with open(audio_file_path, "rb") as f:
    audio_bytes = f.read()
    audio_base64 = base64.b64encode(audio_bytes).decode()

audio_player_base64 = f"""
    <audio autoplay loop controls>
        <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
    </audio>
"""
st.markdown(audio_player_base64, unsafe_allow_html=True)
st.write("**Artist: Xavier Rudd - We Deserve to Dream**")

# Random Facts

# st.subheader("Did you know?")
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

# col3, empty_col, col4 = st.columns([1.5, 0.1, 1.5])
# with col3:
#     st.subheader("Did You Know..?")
#     st.info(dyk2)
#
# with col4:
#     st.subheader("Did You Know..?")
#     st.info(dyk1)

