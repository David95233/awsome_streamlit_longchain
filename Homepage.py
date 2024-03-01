import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# Initialize the ChatOpenAI object
chat = None

if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""
else:
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])
    
st.set_page_config(page_title="Welcome to ASL", layout="wide")

st.title("Welcome to ASL")

if chat:
    with st.container():
        st.header("Chat with ChatGPT")
        prompt = st.text_input("Prompt", value="", max_chars=None, type='default')
        asked = st.button("Ask")
        if asked:
            chat([HumanMessage(content=prompt)])
else:
    with st.container():
        st.warning("Please set your OpenAI API key in the settings page.")
            


    
    