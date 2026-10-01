import json
import pathlib
import streamlit as st
import streamlit.components.v1 as components
import data as d

st.set_page_config(page_title=f"{d.NAME} | Portfolio", page_icon="📊", layout="wide",
                   initial_sidebar_state="collapsed")

# Hide Streamlit chrome and let the portfolio fill the whole page
st.markdown(
    """<style>
    #MainMenu, header, footer {visibility: hidden;}
    .stApp {background: #07080f;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {height: 100vh !important; border: 0; width: 100% !important;}
    </style>""",
    unsafe_allow_html=True,
)

keys = ["NAME", "TITLE", "LOCATION", "EMAIL", "GITHUB", "LINKEDIN", "SUMMARY",
        "STATS", "SKILLS", "EXPERIENCE", "PROJECTS", "EDUCATION", "ROLES"]
payload = json.dumps({k: getattr(d, k) for k in keys}).replace("</", "<\\/")
html = pathlib.Path(__file__).with_name("template.html").read_text(encoding="utf-8")
components.html(html.replace("__DATA__", payload), height=900, scrolling=True)