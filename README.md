# Advanced RAG Q&A Project  

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
- Vector database: **ChromaDB** or **FAISS**  
- Embedding models: **Cohere**
- LLM providers: **Cohere**  

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


### 4. Set up pre-commit hooks (optional but recommended)
```bash
pre-commit install
```

### 5. Launch Jupyter Notebook  

### 4. Run python script

```bash
python agents.py
```

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

## Testing the Setup  

1. Open `agents.py` and run cells step by step.  
2. Ingest and index sample documents (PDF/text).  
3. Run Q&A queries against the indexed data.  
4. Validate results from the LLM.  
