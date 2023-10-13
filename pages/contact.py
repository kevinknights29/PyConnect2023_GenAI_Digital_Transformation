from __future__ import annotations

import streamlit as st

from src.utils import config

st.set_page_config(
    page_title=config.config()["app"]["page_title"],
    page_icon=config.config()["app"]["page_icon"],
)
st.title(config.config()["app"]["contact"]["title"])
