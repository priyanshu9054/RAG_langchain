import langchain_community
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_API_KEY']="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"

## Prompt Template

prompt =  ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistance. PLease help user with his queries."),
    ("user", "Question:{question}")
    
])

st.title("Langchain DEMO with LLAMA2")
input_text=st.text_input("Search the topic u want")

## LLMS

llm = Ollama(model="llama2") # base_url = "http://localhost:11434"
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
