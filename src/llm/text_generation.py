from __future__ import annotations

import os

import streamlit as st
from dotenv import find_dotenv
from dotenv import load_dotenv
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    st.secrets.openai.api_key,
)
TEMPLATE = (
    "Compórtate como un asistente de eventos.\n"
    "Tu objetivo es garantizar una buena experiencia para los participantes del evento.\n"
    "Tus respuestas deben incluir sesiones de interés e información de valor para los participantes\n"
    "Antes de realizar una acción, pregunta si tienes alguna duda.\n"
    "No compartas información falsa.\n"
    "\n"
    "{history}\n"
    "Participante: {question}\n"
    "AI: "
)
PROMPT_TEMPLATE = PromptTemplate(
    template=TEMPLATE,
    input_variables=["history", "question"],
)


def _llm_init(**kwargs):
    model_params = {}
    model_params["temperature"] = kwargs.get("temperature", 0.1)
    model_params["top_p"] = kwargs.get("top_p", 0.95)

    llm = OpenAI(
        openai_api_key=OPENAI_API_KEY,
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()],
        **model_params,
    )
    return llm


def generate_text(prompt, **kwargs):
    llm_chain = LLMChain(prompt=PROMPT_TEMPLATE, llm=_llm_init())
    response = llm_chain.stream(prompt)
    return response
