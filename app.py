# import langchain_community
# from langchain_community.llms import Ollama
# from langchian_core.prompts import ChatPromptTemplate
# from langchain_core.outPut_parsers import StrOutputParser
# import streamlit as st
# import os
# from dotenv import load_dotenv

# os.environ['LANGCHAIN_TRACING_V2']="true"
# os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")

# ## Prompt Template

# prompt = ChatPromptTemplate.from_messages([
#     {"role": "system", "content": "You are a helpful assistant. PLease response to the user queries"},
#     {"role": "user", "Question": "{question}"}
# ])

# st.title("Langchain DEMO with LLAMA2")
# input_text=st.text_input("Search the topic u want")

# ## LLMS

# llm = Ollama(model="llama2") # base_url = "http://localhost:11434"
# output_parser = StrOutputParser()
# chain = prompt|llm|output_parser

# if input_text:
#     st.write(chain.invoke({'question': input_text}))

from fastapi import FastAPI  # Note the corrected capitalization
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import os
import uvicorn

llm = Ollama(model="llama2") # base_url = "http://localhost:11434"

# os.environ['OPEN_API_KEY'] = os.getenv('OPEN_API_KEY')

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server",
    path="/Llam2"
)

model = llm

prompt=ChatPromptTemplate.from_template("Provide me an essay about {topic}")
prompt1=ChatPromptTemplate.from_template("Provide me a poem about {topic}")

add_routes(
    app,
    prompt | model,
    path="/essay"
)

add_routes(
    app,
    prompt1 | model,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)





