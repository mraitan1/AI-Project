import streamlit as st
from dotenv import load_dotenv
from router import route

load_dotenv()

if "history" not in st.session_state:
    st.session_state.history = []

st.title("AI PYTHON TUTOR")


#Display chat history
for msg in st.session_state.history:
    role = "You" if msg["role"] == "user" else "Tutor"

    if "```" in msg["content"]:
        parts = msg["content"].split("```")
        st.markdown(f"**{role}:**")
        for i, part in enumerate(parts):
            if i % 2 == 1:
                st.code(part, language="python")
            else:
                st.markdown(part)
    else:
        st.markdown(f"**{role}:** {msg['content']}")

#Allows enter key and 'Submit' button to work
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_area(
        "What Python related question do you have?",
        key="input_box",
    )
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip():
    # Process message
    st.session_state.history.append({"role": "user", "content": user_input})
    answer = route(user_input)
    st.session_state.history.append({"role": "assistant", "content": answer})

    # Refreshes page
    st.rerun()