from __future__ import annotations

import os

from dotenv import find_dotenv
from dotenv import load_dotenv
from langchain.cache import InMemoryCache
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.globals import set_llm_cache
from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts.chat import HumanMessagePromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate

_ = load_dotenv(find_dotenv())
_ = set_llm_cache(InMemoryCache())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SYSTEM_TEMPLATE = (
    "Compórtate como un asistente de eventos.\n"
    "Tu objetivo es garantizar una buena experiencia para los asistentes.\n"
    "Tus respuestas deben incluir sesiones de interés para los asistentes, información de valor sobre las sesiones.\n"
    "Antes de realizar una acción, pregunta si tienes alguna duda.\n"
    "No compartas información falsa."
)
SYSTEM_MESSAGE_PROMPT = SystemMessagePromptTemplate.from_template(SYSTEM_TEMPLATE)
HUMAN_TEMPLATE = "{text}"
HUMAN_MESSAGE_PROMPT = HumanMessagePromptTemplate.from_template(HUMAN_TEMPLATE)
CHAT_PROMPT = ChatPromptTemplate.from_messages(
    [SYSTEM_MESSAGE_PROMPT, HUMAN_MESSAGE_PROMPT],
)


def _llm_init(**kwargs):
    model_params = {}
    model_params["temperature"] = kwargs.get("temperature", 0.1)
    model_params["max_length"] = kwargs.get("max_length", 2000)
    model_params["top_p"] = kwargs.get("top_p", 0.95)
    model_params["top_k"] = kwargs.get("top_p", 40)

    llm = ChatOpenAI(
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()],
        **model_params,
    )
    return llm


def generate_text(message, **kwargs):
    response = _llm_init()(CHAT_PROMPT.format_prompt(text=message).to_messages())
    return response
