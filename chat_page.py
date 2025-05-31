import streamlit as st
from transformers_client import query_transformers

def chat_page():
    st.title("💬 Simple Finance & Economics Chatbot for 65+")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages using st.chat_message
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Get user input with chat input widget
    if prompt := st.chat_input("Ask me anything about finance or economics in simple terms..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display the user's message instantly
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate bot response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("⏳ Thinking...")

            response = query_transformers(prompt)
            message_placeholder.markdown(response)

            # Save bot response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
