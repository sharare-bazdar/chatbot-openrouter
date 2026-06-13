import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

MODEL = "openai/gpt-oss-20b:free"

st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("پیامت رو بنویس..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = client.chat.completions.create(
        model=MODEL,
        messages=st.session_state.messages
    )

    answer = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
