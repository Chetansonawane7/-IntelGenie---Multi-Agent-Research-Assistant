# agents/summarizer.py

import os
from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOllama


llm = ChatOllama(
    model="llama3"
)

# Prompt Template for summarization
summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
    You are a helpful assistant. Summarize the following content into a clear, concise executive summary for a business audience:

    {text}

    Summary:
    """
)

summarizer_chain = LLMChain(llm=llm, prompt=summary_prompt)

def summarizer_agent(findings):
    return summarizer_chain.run(text=findings)
