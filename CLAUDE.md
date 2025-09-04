# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Environment Setup

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up pre-commit hooks (mandatory)
pre-commit install
```

### Running the Application

```bash
# Run FastAPI server with hot reload
python run.py

# Alternative: Direct uvicorn command
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Code Quality

```bash
# Format code with Black
black .

# Run pre-commit hooks manually
pre-commit run --all-files
```

### Testing and Linting

- No specific test commands found in codebase
- Pre-commit hooks handle code formatting and basic validation

## Architecture Overview

This is a FastAPI-based RAG (Retrieval Augmented Generation) system with a modular architecture:

### Core Components

**FastAPI Application** (`app/main.py`):

- Main FastAPI app with CORS middleware and exception handling
- Runs on port 8000 with auto-reload in development
- Provides OpenAPI docs at `/docs` and `/redoc`

**Agent System** (`app/agents/`):

- `agent.py`: Core Agent class using LangChain with Cohere LLM
- `executor.py`: Agent executor for running agent workflows
- Uses OpenAI tools agent pattern with multiple tools

**Tools Architecture** (`app/tools/`):

- `base.py`: Abstract base class for all tools
- `wikipedia.py`: Wikipedia search tool
- `arxiv.py`: ArXiv academic paper search tool
- `retriever.py`: LangSmith document retrieval tool

**Service Layer** (`app/services/`):

- `query_service.py`: Main service for processing user queries
- Handles both sync and async query processing
- Manages agent executor lifecycle

### Configuration

**Settings** (`app/config.py`):

- Uses Pydantic Settings with `.env` file support
- Key settings: Cohere API key, model settings, embedding config
- Tool-specific configurations (Wikipedia, ArXiv limits)

**Required Environment Variables**:

```
COHERE_API_KEY=your_cohere_api_key
VECTOR_DB_PATH=./vector_store
```

### API Endpoints

- `POST /api/v1/query` - Process queries asynchronously
- `POST /api/v1/query/sync` - Process queries synchronously
- `GET /api/v1/health` - Health check with tool availability
- `GET /api/v1/tools` - List available tools with status

### Key Integration Points

- **LangChain**: Agent framework with tool integration
- **Cohere**: LLM provider for chat and embeddings
- **FAISS**: Vector database for embeddings
- **FastAPI**: Web framework with automatic API documentation

### Code Quality Standards

- **Black** formatting (automatically applied via pre-commit)
- Pre-commit hooks enforce YAML validation, whitespace cleanup
- Pydantic models for request/response validation
- Structured logging throughout application
