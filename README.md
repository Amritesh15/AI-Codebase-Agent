AI Codebase Agent

A multi-agent AI platform that transforms GitHub repositories into searchable knowledge bases using Retrieval-Augmented Generation (RAG), semantic code embeddings, and self-hosted LLMs.

🚀 Features
Clone and analyze any public GitHub repository
Parse and chunk source code automatically
Generate semantic code embeddings
Store and retrieve code context using ChromaDB
Natural-language codebase search
Repository-aware question answering
Multi-agent architecture for ingestion, retrieval, and reasoning
Self-hosted LLM inference using Ollama
🏗️ Architecture
GitHub Repository
        │
        ▼
 Ingestion Agent
        │
        ▼
  Parsing Agent
        │
        ▼
 Chunking Engine
        │
        ▼
 Embedding Agent
        │
        ▼
    ChromaDB
        │
        ▼
 Retrieval Agent
        │
        ▼
    QA Agent
        │
        ▼
     Ollama
        │
        ▼
     Answer
🛠️ Tech Stack
LangGraph
ChromaDB
Ollama
FastAPI
Sentence Transformers
GitPython
Python
📂 Project Structure
Backend/
│
├── app/
│   ├── agents/
│   │   ├── ingestion_agent.py
│   │   ├── parsing_agent.py
│   │   ├── embedding_agent.py
│   │   ├── vector_store_agent.py
│   │   ├── retrieval_agent.py
│   │   └── qa_agent.py
│   │
│   ├── parsers/
│   └── api/
│
├── repos/
├── chroma_db/
├── tests/
└── main.py
⚙️ Installation
Clone Repository
git clone https://github.com/yourusername/AI-Codebase-Agent.git
cd AI-Codebase-Agent/Backend
Create Virtual Environment
python -m venv venv

Activate:

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
📥 Repository Ingestion

Provide a GitHub repository URL:

repo_url = "https://github.com/langchain-ai/langchain"

clone_repository(repo_url)

The system will:

Clone the repository
Parse source files
Create code chunks
Generate embeddings
Store vectors in ChromaDB
🔍 Semantic Search
results = search_chunks(
    "How does AgentExecutor work?"
)

Example output:

agent_executor.py
agents.py
base_agent.py
🤖 Repository Question Answering
response = answer_question(
    "Explain how AgentExecutor works."
)

print(response)

The system retrieves relevant code chunks and generates grounded responses using the repository context.

🎯 Use Cases
Codebase onboarding
Repository exploration
Developer productivity
Architecture understanding
Code search
Documentation generation
AI-powered developer assistants
📈 Future Enhancements
Architecture visualization agent
Repository knowledge graph generation
Multi-repository support
Code dependency analysis
Automated documentation generation
PR review agent
Agentic workflow orchestration with LangGraph
🌟 Key Highlights
Multi-Agent AI Architecture
Retrieval-Augmented Generation (RAG)
Self-Hosted LLM Infrastructure
Semantic Code Search
Repository-Aware Question Answering
Scalable Vector Database Architecture
📄 License

MIT License
