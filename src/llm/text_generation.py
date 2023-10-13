from __future__ import annotations

import os

from dotenv import find_dotenv
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TEMPLATE = (
    "Compórtate como un asistente de eventos.\n"
    "Tu objetivo es garantizar una buena experiencia para los asistentes.\n"
    "Tus respuestas deben incluir sesiones de interés para los asistentes, información de valor sobre las sesiones.\n"
    "Antes de realizar una acción, pregunta si tienes alguna duda.\n"
    "No compartas información falsa.\n"
    "\n"
    "Asistente: {question}\n"
    "Respuesta: "
)
PROMPT_TEMPLATE = PromptTemplate(template=TEMPLATE, input_variables=["question"])


def _llm_init(**kwargs):
    model_params = {}
    model_params["temperature"] = kwargs.get("temperature", 0.1)
    model_params["max_length"] = kwargs.get("max_length", 2000)
    model_params["top_p"] = kwargs.get("top_p", 0.95)
    model_params["top_k"] = kwargs.get("top_p", 40)

    llm = OpenAI(
        openai_api_key=OPENAI_API_KEY,
        **model_params,
    )
    return llm


def generate_text(prompt, **kwargs):
    llm_chain = LLMChain(prompt=PROMPT_TEMPLATE, llm=_llm_init())
    response = llm_chain.stream(prompt)
    return response
