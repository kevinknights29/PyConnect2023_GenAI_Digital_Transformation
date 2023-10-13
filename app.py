from __future__ import annotations

import os

import openai
import streamlit as st
from dotenv import find_dotenv
from dotenv import load_dotenv
from langchain.chains import ChatVectorDBChain
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory

from src.llm import text_generation
from src.vectordb import ingestion

_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

msgs = StreamlitChatMessageHistory(key="langchain_messages")
memory = ConversationBufferMemory(memory_key="history", chat_memory=msgs)

vectorstore = ingestion.pipeline()
qa_chain = ChatVectorDBChain.from_llm(
    llm=text_generation._llm_init(),
    vectorstore=vectorstore,
)

st.title("ChatGPT-like clone")

if len(msgs.messages) == 0:
    msgs.add_ai_message("Hola, bienvenido!")

for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

if prompt := st.chat_input("Inserta tu mensaje aqui:"):
    st.chat_message("Participante").write(prompt)

    response = qa_chain(
        {
            "chat_history": msgs.messages,
            "question": prompt,
        },
    )
    st.chat_message("AI").write(response["answer"])
