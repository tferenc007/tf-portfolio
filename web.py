
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
 


st.title("The Best Company")
content= """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(content)
st.header("Our Team")

col1, col1_empty, col2, col2_empty, col3 = st.columns([1.5, 0.5, 1.5,0.5,1.5])



df = pd.read_csv("data/data_app2.csv", sep=",")
with col1:
    for index, row in df[:3].iterrows():
        content = row['first name'].capitalize() + " " + row['last name'].capitalize()
        st.subheader(content)
        st.write( row['role'])
        st.image("images_app2/" + row["image"])

with col2:
    for index, row in df[4:7].iterrows():
        content = row['first name'].capitalize() + " " + row['last name'].capitalize()
        st.subheader(content)
        st.write( row['role'])
        st.image("images_app2/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        content = row['first name'].capitalize() + " " + row['last name'].capitalize()
        st.subheader(content)
        st.write( row['role'])
        st.image("images_app2/" + row["image"])