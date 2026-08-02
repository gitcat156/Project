import streamlit as st
import random # 

st.set_page_config(page_title="Portfolio", layout="wide")
col1, col2, = st.columns([1, 2.5])

with col1:
    st.title("Portfolio")

with col2:
    st.markdown("lorem si")

st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["History", "Project", "Experience", "Social"])

with tab1:
    st.write("Started coding in 2024")
with tab2:
    with st.container(border=True):
        st.markdown("#### Pong Game")
        st.link_button("Project Link", "https://github.com/")
with tab3:
    st.title("Programming language")
    st.markdown("- Python")
    st.write("- C")
    st.write("- C++")
with tab4:
    st.link_button("Instagram", "https://www.instagram.com/?hl=en")
    st.link_button("Youtube", "https://youtube.com/")
    st.link_button("Discord", "https://discord.com/")