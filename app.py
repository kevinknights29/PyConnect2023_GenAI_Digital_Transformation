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
temperature = 0.1
top_p = 0.95

msgs = StreamlitChatMessageHistory(key="langchain_messages")
memory = ConversationBufferMemory(
    memory_key="history",
    chat_memory=msgs,
    return_messages=True,
)

vectorstore = ingestion.pipeline()
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=text_generation._llm_init(temperature=temperature, top_p=top_p),
    retriever=vectorstore.as_retriever(),
)

st.set_page_config(
    page_title=config.config()["app"]["page_title"],
    page_icon=config.config()["app"]["page_icon"],
)
st.title(config.config()["app"]["title"])
st.header(config.config()["app"]["header"])
st.subheader(config.config()["app"]["subheader"])
st.sidebar.success(config.config()["app"]["sidebar"])

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

expander = st.expander("See Model Arguments")
expander.write(
    (
        "Temperature: is a parameter that influences the language model's output, determining whether the output"
        " is more random and creative or more predictable."
    ),
)
temperature = expander.slider(
    label="temperature",
    min_value=0.1,
    max_value=1.0,
    step=0.05,
    value=temperature,
)
expander.write(
    (
        "Top P: is a parameter that influences the language model's output, by only considering the possibilities"
        " that equal or exceed this value."
    ),
)
top_p = expander.slider(
    label="top_p",
    min_value=0.1,
    max_value=1.0,
    step=0.05,
    value=top_p,
)
