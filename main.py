
import streamlit as st

st.set_page_config(layout="wide")
 
col1, col2 = st.columns(2)

with col1:
    st.image("images/my_photo.jpg")

with col2:
    st.title("Tomasz Ferenc")
    content = """
    Hi, I am Tomek! I am a Bi developer with deep knowledge about data engenerig, analitycal enginering
    Ritht now I'm learning python to wider my knowledge. 
    """
    st.info(content)