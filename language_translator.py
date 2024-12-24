import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Now we can instantiate our model object and generate chat completions:
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# We can chain our model with a prompt template like so:    
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)


st.title('Testing out AI this Python is ____')
input_text=st.text_input("Write the sentence in english and it will be translated in telugu")



# chain = prompt | llm
output_parser=StrOutputParser()

chain=prompt|llm|output_parser  

if input_text:
    st.write(chain.invoke(
    {
        "input_language": "English",
        "output_language": "telugu",
        "input": input_text, 
        #"input": "I love programming.",
    }
))
