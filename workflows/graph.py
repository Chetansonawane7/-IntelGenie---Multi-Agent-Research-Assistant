from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableConfig
from typing import TypedDict, List, Any
from agents.researcher import researcher_agent
from agents.summarizer import summarizer_agent
from agents.recommender import recommender_agent
from utils.formatting import generate_docx_report

# ✅ Define the schema
class GraphState(TypedDict):
    query: str
    files: List[str]  # or UploadedFile if you're using Streamlit
    findings: str
    summary: str
    recommendations: str
    full: str
    docx: Any  # Use Any because it's a BytesIO stream

# ✅ Agent steps

def run_research(state: GraphState) -> GraphState:
    query, files = state['query'], state['files']
    findings = researcher_agent(query, files)
    return {**state, "findings": findings}

def run_summarizer(state: GraphState) -> GraphState:
    summary = summarizer_agent(state["findings"])
    return {**state, "summary": summary}

def run_recommender(state: GraphState) -> GraphState:
    reco = recommender_agent(state["summary"])
    return {**state, "recommendations": reco}

def generate_output(state: GraphState) -> GraphState:
    final_report = f"### Summary\n{state['summary']}\n\n### Recommendations\n{state['recommendations']}"
    docx_binary = generate_docx_report(state['query'], state['summary'], state['recommendations'])

    return {
        **state,  # Keep all existing fields
        "full": final_report,
        "docx": docx_binary,
    }

# ✅ LangGraph flow
def run_graph(query: str, files: List[Any]):
    builder = StateGraph(GraphState)

    builder.add_node("research", run_research)
    builder.add_node("summarize", run_summarizer)
    builder.add_node("recommend", run_recommender)
    builder.add_node("output", generate_output)

    builder.set_entry_point("research")
    builder.add_edge("research", "summarize")
    builder.add_edge("summarize", "recommend")
    builder.add_edge("recommend", "output")

    builder.set_finish_point("output")  # ✅ Ensure graph returns final result

    graph = builder.compile()
    initial_state = {"query": query, "files": files}
    return graph.invoke(initial_state)


