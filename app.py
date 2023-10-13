from __future__ import annotations

import os

import openai
import streamlit as st
from dotenv import find_dotenv
from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory

from src.llm import text_generation
from src.utils import config
from src.vectordb import ingestion

_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    st.secrets.openai.api_key,
)
openai.api_key = OPENAI_API_KEY

msgs = StreamlitChatMessageHistory(key="langchain_messages")
memory = ConversationBufferMemory(
    memory_key="history",
    chat_memory=msgs,
    return_messages=True,
)

vectorstore = ingestion.pipeline()
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=text_generation._llm_init(),
    retriever=vectorstore.as_retriever(),
)

st.title(config.config()["app"]["title"])
st.header(config.config()["app"]["header"])
st.subheader(config.config()["app"]["subheader"])

if len(msgs.messages) == 0:
    msgs.add_ai_message("\n".join(config.config()["app"]["greeting"]))

for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

if prompt := st.chat_input(config.config()["app"]["instruction"]):
    st.chat_message("human").write(prompt)

    response = qa_chain(
        {
            "chat_history": msgs.messages,
            "question": prompt,
        },
    )
    st.chat_message("ai").write(response["answer"])
