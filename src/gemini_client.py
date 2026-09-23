import os

import streamlit as st
from google import genai

MODEL_NAME = "gemini-3.6-flash"


@st.cache_resource
def get_client():
    # Local development: Streamlit secrets.
    # Cloud Run: Secret Manager exposes GEMINI_API_KEY as an environment variable.
    api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Configure it in "
            ".streamlit/secrets.toml locally or Google Cloud Secret Manager on Cloud Run."
        )

    return genai.Client(api_key=api_key)


def improve_email(prompt: str) -> str:
    client = get_client()
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    return (response.text or "").strip()
