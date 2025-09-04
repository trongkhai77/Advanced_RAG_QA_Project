# Advanced RAG Q&A Project

A FastAPI-based Retrieval Augmented Generation (RAG) system with modular architecture, featuring multiple search tools and LangChain agent integration.

## System Requirements

### Hardware

- Minimum **16GB RAM** (recommended **32GB** for large models)
- At least **50GB free disk space**
- CPU: **8+ cores recommended**
- GPU: **NVIDIA with CUDA** (recommended for acceleration)

### Software

- **Python 3.8+** (recommended 3.10+)
- **Docker & Docker Compose**
- **Git**
- **Jupyter Notebook/Lab**

### Additional Components

- Vector database: **FAISS**
- Embedding models: **Cohere**
- LLM providers: **Cohere**
- Web framework: **FastAPI**
- Agent framework: **LangChain**

---

## Installation & Setup

### 1. Set up virtual environment and activate it

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file:

```env
COHERE_API_KEY=your_cohere_api_key
VECTOR_DB_PATH=./vector_store
```

### 4. Set up pre-commit hooks (mandatory)

```bash
pre-commit install
```

### 5. Start the FastAPI server

```bash
# Run FastAPI server with hot reload
python run.py

# Alternative: Direct uvicorn command
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The server will start on `http://localhost:8000` with:

- API documentation at `/docs`
- Alternative docs at `/redoc`

### 6. Available API Endpoints

- `POST /api/v1/query` - Process queries asynchronously
- `POST /api/v1/query/sync` - Process queries synchronously
- `GET /api/v1/health` - Health check with tool availability
- `GET /api/v1/tools` - List available tools with status

---

## Code Formatting and Quality

This project uses **Black** for code formatting and **pre-commit** hooks for code quality checks.

### Using Black

Format your Python code:

```bash
black .
```

### Using Pre-commit

Pre-commit hooks will automatically run on each commit to ensure code quality:

- **YAML validation** - checks YAML file syntax
- **End of file fixer** - ensures files end with newlines
- **Trailing whitespace removal** - removes trailing whitespace
- **Black formatting** - automatically formats Python code

To run pre-commit hooks manually:

```bash
pre-commit run --all-files
```

---

## Architecture Overview

This FastAPI application features a modular RAG system with:

### Core Components

- **FastAPI Application**: Main web server with CORS middleware and OpenAPI docs
- **Agent System**: LangChain-based agents with Cohere LLM integration
- **Tool Architecture**: Modular tools for Wikipedia, ArXiv, and document retrieval
- **Service Layer**: Query processing and agent executor management

### Available Tools

- **Wikipedia Search**: Academic and general knowledge queries
- **ArXiv Search**: Scientific paper and research queries
- **Document Retriever**: LangSmith-based document retrieval

### Key Technologies

- **FastAPI**: High-performance web framework with automatic API documentation
- **LangChain**: Agent framework for tool integration and workflow management
- **Cohere**: LLM provider for chat completions and embeddings
- **FAISS**: Vector database for efficient similarity search
