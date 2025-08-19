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

### 1. Clone the repository  
```bash
git clone https://github.com/trongkhai77/Advanced_RAG_QA_Project.git
```

### 2. Install dependencies  
```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, create one by analyzing imports in `agents.ipynb`.  

### 3. Configure environment variables  
Create a `.env` file:  
```env
COHERE_API_KEY=your_cohere_api_key
VECTOR_DB_PATH=./vector_store
```

### 4. Launch Jupyter Notebook  
```bash
jupyter notebook agents.ipynb
```

---

## Testing the Setup  

1. Open `agents.ipynb` and run cells step by step.  
2. Ingest and index sample documents (PDF/text).  
3. Run Q&A queries against the indexed data.  
4. Validate results from the LLM.  

---

## References  
- [LangChain Documentation](https://python.langchain.com/docs/)  
- [RAG-Projects Repository](https://github.com/atulkashyap404/RAG-Projects)  
