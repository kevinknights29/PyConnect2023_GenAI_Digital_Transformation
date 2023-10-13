from __future__ import annotations

import os

import streamlit as st
import weaviate
from dotenv import find_dotenv
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Weaviate

from src.utils import config
from src.utils import constants
from src.utils import files


_ = load_dotenv(find_dotenv())
WEAVIATE_API_KEY = os.getenv(
    "WEAVIATE_API_KEY",
    st.secrets.weviate.api_key,
)
OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    st.secrets.openai.api_key,
)
TEXT_INPUT_DIR = os.path.join(
    constants.APP_FOLDER,
    config.config()["text"]["input_dir"],
)


def pipeline():
    loader = TextLoader(files.find_file(TEXT_INPUT_DIR, pattern="*.txt"))
    documents = loader.load()
    text_splitter = CharacterTextSplitter(
        chunk_size=config.config()["text"]["chunk_size"],
        chunk_overlap=config.config()["text"]["chunk_overlap"],
    )
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(
        openai_api_key=OPENAI_API_KEY,
        model=config.config()["vectordb"]["openai"]["embeddings"]["model"],
    )

    client = weaviate.Client(
        url=config.config()["vectordb"]["weviate"]["url"],
        auth_client_secret=weaviate.AuthApiKey(WEAVIATE_API_KEY),
    )
    vectorstore = Weaviate.from_documents(
        docs,
        embeddings,
        client=client,
        by_text=False,
    )
    return vectorstore


if __name__ == "__main__":
    pipeline()
