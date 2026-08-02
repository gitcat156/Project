import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")
col1, col2, = st.columns([1, 2.5])

with col1:
    st.title("Portfolio")
    st.markdown("Hello World")
with col2:
    st.title("Description")
    st.write("This is a portfolio website")
    st.write("")

st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["History", "Project", "Experience", "Social"])

with tab1:
    st.write("Started coding in 2024")
with tab2:
    col3, col4 = st.columns(2)
    with col3:
        with st.container(border=True):
            st.markdown("#### Pong Game")
            st.link_button("Project Link", "https://github.com/")
    with col4:
        with st.container(border=True):
            st.markdown("#### Game")
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