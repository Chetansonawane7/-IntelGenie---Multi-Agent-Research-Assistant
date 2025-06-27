# agents/recommender.py

import os
from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOllama


llm = ChatOllama(model="llama3")

# Prompt Template for strategic recommendations
reco_prompt = PromptTemplate(
    input_variables=["summary"],
    template="""
    Based on the following executive summary, provide strategic business insights, recommendations, or potential risks and opportunities. Format in bullet points:

    {summary}

    Recommendations:
    """
)

reco_chain = LLMChain(llm=llm, prompt=reco_prompt)

def recommender_agent(summary):
    return reco_chain.run(summary=summary)
