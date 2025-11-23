from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key = st.secrets.get("OPENAI_API_KEY", None)

if api_key is None:
    # Local development: fallback to .env
    from dotenv import load_dotenv
    load_dotenv()
    import os
    api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def ask_llm(prompt, model="gpt-4.1-mini"):

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
