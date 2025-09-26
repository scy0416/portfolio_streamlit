import streamlit as st
st.set_page_config(page_title="송찬영의 포트폴리오")

pg = st.navigation([
    "home.py",
    "github.py",
    "blog.py",
    "project.py"
], position="top")
pg.run()