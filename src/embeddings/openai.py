from __future__ import annotations

import os

import streamlit as st
from dotenv import find_dotenv
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings

from src.utils import config

_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    st.secrets.openai.api_key,
)


def embedding_function():
    return OpenAIEmbeddings(
        openai_api_key=OPENAI_API_KEY,
        model=config.config()["vectordb"]["openai"]["embeddings"]["model"],
    )
