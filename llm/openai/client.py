import os

import requests

from llm.openai.models import (
    ChatMessage,
    ChatFunction,
    CreateChatResponse,
    CreateChatRequest,
)


class Client:
    def __init__(self) -> None:
        self.create_chat_url = "https://api.openai.com/v1/chat/completions"

    def create_chat(
        self, model: str, messages: list[ChatMessage], functions: list[ChatFunction]
    ) -> CreateChatResponse:
        chat_req = CreateChatRequest(
            model=model, messages=messages, functions=functions
        )

        if not (token := os.getenv("OPENAI_API_KEY")):
            raise Exception("No token found")

        headers = {
            "content-type": "application/json",
            "Authorization": "Bearer " + token,
        }

        json = chat_req.model_dump_json(exclude_unset=True)
        resp = requests.post(
            self.create_chat_url,
            headers=headers,
            data=json,
        )

        foo = resp.json()

        return CreateChatResponse(**resp.json())
