import streamlit as st
from workflows.graph import run_graph
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOllama

def extract_title_from_llm(query):
    prompt = PromptTemplate(
        input_variables=["query"],
        template="""
        Given the following research question, generate a short and meaningful 2-4 word title suitable for a report filename. 
        Use underscores instead of spaces. Make it readable and relevant.

        Question: {query}
        Title:"""
    )

    llm = ChatOllama(model="llama3", temperature=0.3)
    chain = LLMChain(prompt=prompt, llm=llm)
    return chain.run(query).strip().replace(" ", "_")



st.set_page_config(page_title="IntelGenie", layout="wide")
st.title("🧠 IntelGenie - Multi-Agent Research Assistant")

query = st.text_input("🔍 Enter your research query")
uploaded_files = st.file_uploader("📎 Upload supporting PDFs (optional)", type=["pdf"], accept_multiple_files=True)

if st.button("🚀 Run Agents") and query:
    with st.spinner("Thinking..."):
        report = run_graph(query, uploaded_files)

        st.subheader("📄 Executive Summary")
        st.write(report.get('summary', '⚠️ Summary missing'))

        st.write(f"Returned keys: {list(report.keys())}")  # ✅ Debug log

        # ✅ Ensure DOCX exists
        if "docx" in report:
            with open("debug_report.docx", "wb") as f:
                f.write(report['docx'].getvalue())

            title = extract_title_from_llm(query)

            st.download_button(
                label="📥 Download Report (.docx)",
                data=report['docx'].getvalue(),
                file_name=f"{title}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        else:
            st.warning("⚠️ DOCX report not generated.")
