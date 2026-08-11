"""
llm/client.py

OpenAI-compatible client.
"""

import json
import requests


SETTINGS_FILE = "llm_settings.json"


def load_settings():

    with open(
        SETTINGS_FILE,
        "r",
        encoding="utf-8",
    ) as handle:

        return json.load(handle)


def ask_llm(
    prompt,
    system_prompt="",
):

    settings = load_settings()

    endpoint = (
        settings["endpoint"]
        .rstrip("/")
    )

    url = (
        endpoint
        + "/chat/completions"
    )

    headers = {
        "Content-Type":
            "application/json",
    }

    api_key = (
        settings
        .get("api_key", "")
        .strip()
    )

    if api_key:

        headers[
            "Authorization"
        ] = (
            f"Bearer {api_key}"
        )

    payload = {

        "model":
            settings["model"],

        "messages": [
            {
                "role": "system",
                "content":
                    system_prompt,
            },
            {
                "role": "user",
                "content":
                    prompt,
            },
        ],

        "temperature":
            settings.get(
                "temperature",
                0.2,
            ),
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=120,
    )

    response.raise_for_status()

    data = response.json()

    return (
        data["choices"][0]
        ["message"]["content"]
    )
