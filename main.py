
import streamlit as st
import pandas as pd

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
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])


df = pd.read_csv("data/data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[source Code](https://pythonhow.com)")
