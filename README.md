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
git clone https://github.com/atulkashyap404/RAG-Projects.git
cd "RAG-Projects/Project 05 Advanced RAG Q&A Project"
```

### 2. Create virtual environment  
Using **venv**:  
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies  
```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, create one by analyzing imports in `agents.ipynb`.  

### 4. Configure environment variables  
Create a `.env` file:  
```env
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
VECTOR_DB_PATH=./vector_store
```

### 5. Launch Jupyter Notebook  
```bash
jupyter notebook agents.ipynb
```

---

## 🔎 Testing the Setup  

1. Open `agents.ipynb` and run cells step by step.  
2. Ingest and index sample documents (PDF/text).  
3. Run Q&A queries against the indexed data.  
4. Validate results from the LLM.  

---

## 🧰 Docker (Optional)  

Build and run with Docker:  
```bash
docker build -t advanced-rag .
docker run -it --env-file .env -p 8888:8888 advanced-rag
```

---

## ✅ Deployment Checklist  

- [ ] Python/Docker environment configured  
- [ ] Dependencies installed without conflicts  
- [ ] `.env` file created with API keys  
- [ ] Notebook runs without errors  
- [ ] Sample documents indexed successfully  
- [ ] Q&A queries executed successfully  
- [ ] Vector database operational  

---

## 📚 References  
- [LangChain Documentation](https://python.langchain.com/docs/)  
- [RAG-Projects Repository](https://github.com/atulkashyap404/RAG-Projects)  

---

## 🏁 Definition of Done  
- All team members can run the RAG system locally  
- Full setup and troubleshooting documentation available  
- Q&A works correctly with sample data  
- Performance benchmarks established  
- Code and security reviews completed  
