from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

api_key = st.secrets.get("OPENAI_API_KEY")
project_id = st.secrets.get("OPENAI_PROJECT")

if api_key or project_id is None:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    project_id = os.getenv("OPENAI_PROJECT")

client = OpenAI(api_key=api_key,project=project_id)

def ask_llm(prompt, model="gpt-4.1-mini"):

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
