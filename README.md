# AI Codebase Agent

AI Codebase Agent is a multi-agent RAG platform that transforms GitHub repositories into searchable knowledge bases. It enables developers to explore, understand, and query large codebases using semantic search, vector embeddings, and self-hosted LLMs.

## Features

- GitHub repository ingestion and analysis
- Automatic code parsing and chunking
- Semantic code embeddings generation
- Vector search using ChromaDB
- Natural language codebase search
- Repository-aware question answering
- Multi-agent architecture for ingestion, retrieval, and reasoning
- Self-hosted LLM inference using Ollama

## Tech Stack

- LangGraph
- ChromaDB
- Ollama
- FastAPI
- Sentence Transformers
- GitPython
- Python

## Architecture

```text
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
```

## Project Structure

```text
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
```

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/<your-username>/AI-Codebase-Agent.git
cd AI-Codebase-Agent/Backend
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Ingest a Repository

```python
from app.agents.ingestion_agent import clone_repository

clone_repository(
    "https://github.com/langchain-ai/langchain"
)
```

### Generate Embeddings

```python
from app.agents.parsing_agent import parse_repository
from app.agents.embedding_agent import embed_chunks

chunks = parse_repository(
    "repos/langchain"
)

embedded_chunks = embed_chunks(chunks)
```

### Store in ChromaDB

```python
from app.agents.vector_store_agent import store_chunks

store_chunks(embedded_chunks)
```

### Search the Codebase

```python
from app.agents.vector_store_agent import search_chunks

results = search_chunks(
    "How does AgentExecutor work?"
)

print(results)
```

### Ask Questions About the Repository

```python
from app.agents.qa_agent import answer_question

response = answer_question(
    "Explain how AgentExecutor works."
)

print(response)
```

## Example Queries

- How does AgentExecutor work?
- Explain the prompt template architecture.
- How are chat models implemented?
- Which files handle tool execution?
- Describe the repository architecture.
- Where is memory management implemented?

## Future Enhancements

- Architecture visualization agent
- Repository dependency graph generation
- Multi-repository support
- Automated documentation generation
- Pull request review agent
- Knowledge graph integration
- Advanced LangGraph orchestration

## Resume Highlights

- Built a multi-agent AI platform using LangGraph, ChromaDB, and self-hosted LLMs for repository intelligence and code understanding.
- Engineered an end-to-end RAG pipeline that ingests GitHub repositories, generates semantic embeddings, and enables natural-language code search.
- Developed repository-aware AI agents capable of answering implementation and architecture questions using contextual source-code retrieval.

## License

MIT License

---

Built to help developers understand large codebases faster using AI.
