from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found. Please check your .env file.")
    st.stop()

llm = ChatGroq(model="openai/gpt-oss-20b", api_key=api_key, temperature=0)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant. Explain technical concepts in simple language and keep answers concise.",
        ),
        MessagesPlaceholder(variable_name="history"),
    ]
)

chain = prompt | llm
st.title("AI Chatbot")


# New Chat button
def generate_response():
    for chunk in chain.stream({"history": st.session_state.messages}):
        yield chunk.content


if st.button("New Chat"):
    st.session_state.messages = []
    st.rerun()


# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
for message in st.session_state.messages:

    if message.type == "human":
        with st.chat_message("user"):
            st.write(message.content)

    elif message.type == "ai":
        with st.chat_message("assistant"):
            st.write(message.content)
user_input = st.chat_input("Ask me anything...")

if user_input and user_input.strip():
    if len(user_input) > 5000:
        st.warning("Message is too long. Maximum 5000 characters allowed.")
    else:
        human_message = HumanMessage(content=user_input)
     
        st.session_state.messages.append(human_message)
        with st.chat_message("user"):
            st.write(user_input)
        try:
            with st.chat_message("assistant"):
                response_text = st.write_stream(generate_response())

            st.session_state.messages.append(AIMessage(content=response_text))
        except Exception as e:
            st.session_state.messages.pop()
            st.error("Unable to generate a response. Please try again.")
            print(f"LLM Error: {e}")
