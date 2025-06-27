# 🧠 IntelGenie - Multi-Agent Research Assistant

IntelGenie is a LangGraph + LLaMA-powered research assistant that automates research, summarization, and strategic recommendations into a downloadable `.docx` report — all running locally.

## 🚀 Features
- Multi-agent pipeline: Research → Summarize → Recommend
- Uses Ollama's LLaMA 3 — no API key needed
- Outputs clean Word reports with cover page
- Smart LLM-generated report filenames

## 🛠️ Technologies
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Streamlit](https://streamlit.io)
- [Ollama](https://ollama.com/)
- Python 3.10+

📁 Final Project Directory: IntelGenie/
bash
Copy code
IntelGenie/
├── app.py                        # Streamlit frontend + report download
├── .env.example                 # Environment variable template (NO SECRETS)
├── requirements.txt             # Python dependencies
├── README.md                    # Project overview and usage instructions
│
├── workflows/                   # LangGraph pipeline logic
│   └── graph.py
│
├── agents/                      # Individual agents for each task
│   ├── researcher.py
│   ├── summarizer.py
│   └── recommender.py
│
├── utils/                       # Supporting utilities (DOCX formatting, etc.)
│   └── formatting.py
│
├── assets/                      # Optional: demo screenshots, sample reports
│   ├── demo_screenshot.png
│   └── sample_report.docx
│
└── LICENSE                      # (optional) MIT or Apache license

## 📦 Installation
```bash
git clone https://github.com/Chetansonawane7/-IntelGenie---Multi-Agent-Research-Assistant.git
cd IntelGenie
pip install -r requirements.txt
```

Start Ollama if not running
```bash
Ollama run llama3
```

Start the App:
```bash
streamlit run app.py
```

📁 Example Output
Query	Filename
"How does AI impact healthcare?"	AI_in_Healthcare_IntelGenie_Report.docx

📄 License
MIT

👤 Built by Your Name

yaml
Copy
Edit

---

### 📦 2. `requirements.txt`

Use this as a base:

streamlit
langchain
langgraph
langchain-community
langchain-core
python-dotenv
duckduckgo-search
pypdf
faiss-cpu
sentence-transformers
python-docx

go
Copy
Edit

Add:
```bash
pip freeze > requirements.txt
```
Then remove your local-only or version-specific junk lines.


🔒 3. .env.example
env
Copy
Edit
# If you ever use OpenAI or HuggingFace
OPENAI_API_KEY=your_key_here
