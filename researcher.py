import os
from dotenv import load_dotenv
load_dotenv()

from langchain.tools import DuckDuckGoSearchRun
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="llama3"
)

search = DuckDuckGoSearchRun()

# PDF processing helper
def extract_text_from_pdfs(files):
    texts = []
    for file in files:
        loader = PyPDFLoader(file)
        pages = loader.load()
        texts.extend(pages)
    return texts

def researcher_agent(query, files):
    findings = []

    # Step 1: Web search
    web_results = search.run(query)
    findings.append(f"🔍 Web Search Result:\n{web_results}")

    # Step 2: PDF extraction + RAG
    if files:
        docs = extract_text_from_pdfs(files)
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectordb = FAISS.from_documents(chunks, embeddings)

        retriever = vectordb.as_retriever()
        rel_docs = retriever.get_relevant_documents(query)

        chain = load_qa_chain(llm, chain_type="stuff")
        pdf_answer = chain.run(input_documents=rel_docs, question=query)
        findings.append(f"📄 PDF Insight:\n{pdf_answer}")

    return "\n\n".join(findings)
