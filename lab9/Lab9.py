import streamlit as st

st.set_page_config(page_title="Simple Chatbot", page_icon="💬")
st.title("Simple Chatbot")
st.caption("A rule-based demo chatbot. It does not call an external AI service.")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Type your message...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    lower = prompt.lower()
    if "python" in lower:
        reply = "Python is a popular programming language for automation, AI, and data science."
    elif "streamlit" in lower:
        reply = "Streamlit is a Python framework for building interactive data apps."
    elif any(word in lower for word in ["hello", "hi", "hey"]):
        reply = "Hello! What would you like to learn today?"
    elif "help" in lower:
        reply = "Try asking about Python, Streamlit, or say hello."
    else:
        reply = f"You said: “{prompt}”. I am a demo chatbot and use simple rules to reply."
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
