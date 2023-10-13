from __future__ import annotations

import os

import weaviate
from dotenv import find_dotenv
from dotenv import load_dotenv

from src.utils import config

_ = load_dotenv(find_dotenv())
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")


if __name__ == "__main__":
    auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)
    client = weaviate.Client(
        url=config.config()["vectordb"]["weviate"]["url"],
        auth_client_secret=auth_config,
    )
    client.schema.get()
