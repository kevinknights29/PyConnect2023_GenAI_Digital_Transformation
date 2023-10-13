from __future__ import annotations

import os

import streamlit as st
import weaviate
from dotenv import find_dotenv
from dotenv import load_dotenv
from langchain.vectorstores.weaviate import Weaviate

from src.embeddings import openai
from src.utils import config

_ = load_dotenv(find_dotenv())
WEAVIATE_API_KEY = os.getenv(
    "WEAVIATE_API_KEY",
    st.secrets.weaviate.api_key,
)


def connect_vectorstore():
    auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)
    client = weaviate.Client(
        url=config.config()["vectordb"]["weviate"]["url"],
        auth_client_secret=auth_config,
    )
    vectorstore = Weaviate(
        client,
        embedding=openai.embedding_function(),
        index_name="LangChain",
        text_key="text",
    )
    return vectorstore


if __name__ == "__main__":
    auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)
    client = weaviate.Client(
        url=config.config()["vectordb"]["weviate"]["url"],
        auth_client_secret=auth_config,
    )
    print(client.schema.get())
