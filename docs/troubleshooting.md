# Troubleshooting Guide

Common issues and solutions when using One Click AI Spark.

## Table of Contents

- [Installation Issues](#installation-issues)
- [Generation Issues](#generation-issues)
- [Runtime Issues](#runtime-issues)
- [API Issues](#api-issues)
- [LLM & AI Issues](#llm--ai-issues)
- [Database Issues](#database-issues)
- [Docker Issues](#docker-issues)
- [Performance Issues](#performance-issues)

---

## Installation Issues

### "pip: command not found"

**Problem:** pip is not installed or not in PATH

**Solution:**

**Windows:**
```powershell
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

**Ubuntu:**
```bash
sudo apt update
sudo apt install python3-pip
```

**macOS:**
```bash
python3 -m ensurepip --upgrade
```

---

### "one-click-ai: command not found"

**Problem:** Installation succeeded but command not in PATH

**Solution:**

**Windows:**
```powershell
# Find Python Scripts directory
python -c "import sys; print(sys.prefix + '\\Scripts')"

# Add to PATH:
# 1. Search "Environment Variables" in Start Menu
# 2. Edit "Path" variable
# 3. Add the Scripts directory
# 4. Restart terminal
```

**Ubuntu/macOS:**
```bash
# Add to PATH
export PATH="$HOME/.local/bin:$PATH"

# Make permanent
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Alternative:** Use `python -m one_click_ai` instead:
```bash
python -m one_click_ai generate --name my-app --features llm
```

---

### "ModuleNotFoundError: No module named 'one_click_ai'"

**Problem:** Package not installed properly

**Solution:**
```bash
# Uninstall completely
pip uninstall one-click-ai-spark -y

# Clear cache
pip cache purge

# Reinstall
pip install one-click-ai-spark

# Verify
python -c "import one_click_ai; print(one_click_ai.__version__)"
```

---

### SSL Certificate Errors

**Problem:** `[SSL: CERTIFICATE_VERIFY_FAILED]` during installation

**Solution:**

**Windows:**
```powershell
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org one-click-ai-spark
```

**macOS:**
```bash
# Install certificates
/Applications/Python\ 3.11/Install\ Certificates.command

# Or
pip install --upgrade certifi
```

**Ubuntu:**
```bash
sudo apt update
sudo apt install ca-certificates
sudo update-ca-certificates
```

---

## Generation Issues

### "Project already exists"

**Problem:** Output directory not empty

**Solution:**
```bash
# Option 1: Use different directory
one-click-ai generate --name my-app --output ./my-app-v2

# Option 2: Delete existing (CAUTION: deletes all files)
rm -rf ./my-app
one-click-ai generate --name my-app --output ./my-app

# Option 3: Force overwrite (if supported)
one-click-ai generate --name my-app --output ./my-app --force
```

---

### "Invalid feature: xyz"

**Problem:** Typo in feature name or unsupported feature

**Solution:**
```bash
# List all available features
one-click-ai list

# Check spelling
one-click-ai generate --name my-app --features llm,rag  # Correct
# Not: --features lm,RAG  # Wrong
```

**Supported features:**
- `llm`, `rag`, `voice`, `voice_to_voice`, `vision`, `emotion`, `search`
- `agents`, `memory`, `streaming`, `session`
- `ml_training`, `computer_vision`, `edge_ai`, `fine_tuning`
- `mlops`, `aggregator`, `analytics`, `guardrails`
- `multi_tenant`, `ab_testing`, `ollama_serve`
- `docker`, `ci_cd`, `iac`, `monitoring`

---

### "Template rendering error"

**Problem:** Bug in template or missing variable

**Solution:**
```bash
# Check Python version
python --version  # Should be 3.11+

# Update to latest version
pip install --upgrade one-click-ai-spark

# Report bug
# Include: command used, error message, Python version
# GitHub: https://github.com/aktonay/ONE-CLICK-AI-SPARK/issues
```

---

## Runtime Issues

### "ModuleNotFoundError" when running generated project

**Problem:** Dependencies not installed

**Solution:**
```bash
cd my-app

# Install dependencies
pip install -r requirements.txt

# If using conda
conda install --file requirements.txt

# Verify installation
pip list | grep fastapi
pip list | grep openai
```

---

### "Port 8000 already in use"

**Problem:** Another process using the port

**Solution:**

**Windows:**
```powershell
# Find process using port 8000
Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess

# Kill it
Stop-Process -Id <PID>

# Or use different port
python src/main.py --port 8001
```

**Ubuntu/macOS:**
```bash
# Find process
lsof -ti:8000

# Kill it
kill -9 $(lsof -ti:8000)

# Or use different port
python src/main.py --port 8001
```

---

### "Connection refused" when starting server

**Problem:** Server failed to start

**Solution:**
```bash
# Check error logs
python src/main.py

# Common causes:
# 1. Missing .env file
cp .env.example .env

# 2. Invalid environment variables
cat .env  # Check for syntax errors

# 3. Database not running
docker-compose up -d postgres redis

# 4. Import errors
python -c "from src.main import app; print('OK')"
```

---

## API Issues

### "404 Not Found" on API endpoints

**Problem:** Incorrect URL or endpoint not registered

**Solution:**
```bash
# Check available endpoints
# Visit: http://localhost:8000/docs

# Common mistakes:
# ❌ http://localhost:8000/chat
# ✅ http://localhost:8000/api/v1/chat/message

# ❌ http://localhost:8000/api/chat
# ✅ http://localhost:8000/api/v1/chat/message
```

---

### "422 Unprocessable Entity"

**Problem:** Invalid request body

**Solution:**
```bash
# Check API docs for required fields
# Visit: http://localhost:8000/docs

# Example correct request:
curl -X POST "http://localhost:8000/api/v1/chat/message" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Hello",
    "conversation_id": "test-123"
  }'

# Common mistakes:
# ❌ Missing required field
# ❌ Wrong data type (string instead of int)
# ❌ Extra unknown fields
```

---

### "401 Unauthorized"

**Problem:** Missing or invalid API key/token

**Solution:**
```bash
# Check .env file has API key
cat .env | grep OPENAI_API_KEY

# Verify key is valid
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"

# If using authentication, include token
curl -X POST "http://localhost:8000/api/v1/chat/message" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

---

### "429 Too Many Requests"

**Problem:** Rate limit exceeded

**Solution:**
```python
# Implement exponential backoff
import time
from openai import RateLimitError

def call_with_retry(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func()
        except RateLimitError:
            wait_time = 2 ** attempt  # 1s, 2s, 4s
            time.sleep(wait_time)
    raise Exception("Max retries exceeded")

# Increase rate limits in config
# src/config.py
RATE_LIMIT_PER_MINUTE = 100
```

---

### "500 Internal Server Error"

**Problem:** Server crashed or unhandled exception

**Solution:**
```bash
# Check server logs
docker-compose logs -f app

# Or if running directly:
python src/main.py  # Watch terminal output

# Enable debug mode
# .env
DEBUG=true

# Check Sentry (if configured)
# Visit Sentry dashboard for error details
```

---

## LLM & AI Issues

### "OpenAI API key not found"

**Problem:** Environment variable not set

**Solution:**
```bash
# Check .env file exists
ls -la .env

# Check content
cat .env | grep OPENAI_API_KEY

# Should look like:
# OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx

# Not:
# OPENAI_API_KEY = sk-xxx  # No spaces!
# OPENAI_API_KEY='sk-xxx'  # No quotes!

# Restart server after changing .env
```

---

### "Model not found" or "Invalid model"

**Problem:** Using unavailable or wrong model name

**Solution:**
```python
# Check available models
import openai
models = openai.Model.list()
print([m.id for m in models.data])

# Common model names:
# OpenAI: gpt-4, gpt-4-turbo, gpt-3.5-turbo
# Anthropic: claude-3-opus-20240229, claude-3-sonnet-20240229

# Update in config
# src/config.py
LLM_MODEL = "gpt-3.5-turbo"  # Not "gpt-3.5"
```

---

### "Token limit exceeded"

**Problem:** Input + output exceeds model's context window

**Solution:**
```python
# Check token count
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")
tokens = enc.encode(text)
print(f"Token count: {len(tokens)}")

# Model limits:
# gpt-3.5-turbo: 4K tokens
# gpt-4: 8K tokens
# gpt-4-32k: 32K tokens
# gpt-4-turbo: 128K tokens

# Solutions:
# 1. Chunk large documents
# 2. Use larger context model
# 3. Summarize before sending

def chunk_text(text, max_tokens=3000):
    enc = tiktoken.encoding_for_model("gpt-4")
    tokens = enc.encode(text)
    
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = enc.decode(tokens[i:i+max_tokens])
        chunks.append(chunk)
    
    return chunks
```

---

### "Embedding dimension mismatch"

**Problem:** Using different embedding models between indexing and querying

**Solution:**
```python
# Always use same model
# src/config.py
EMBEDDING_MODEL = "text-embedding-3-small"  # 1536 dimensions

# Recreate vector index if you changed models
# src/core/rag/vector_store.py

# Delete old index
vector_store.delete_index()

# Recreate with new embeddings
vector_store.create_index()
documents = load_all_documents()
for doc in documents:
    embeddings = get_embeddings(doc.text)
    vector_store.add(embeddings, doc.metadata)
```

---

### "RAG returns irrelevant results"

**Problem:** Poor retrieval quality

**Solution:**
```python
# 1. Improve chunking
CHUNK_SIZE = 500  # Smaller chunks = more precise
CHUNK_OVERLAP = 100  # Overlap to maintain context

# 2. Adjust retrieval parameters
# src/core/rag/retriever.py
TOP_K = 5  # Retrieve top 5 results
MIN_SIMILARITY = 0.7  # Filter low-quality results

# 3. Use reranking
from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank_results(query: str, documents: list):
    pairs = [[query, doc.text] for doc in documents]
    scores = reranker.predict(pairs)
    
    # Sort by score
    ranked = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )
    return [doc for doc, score in ranked]

# 4. Add metadata filtering
vector_store.search(
    query,
    filter={"category": "technical", "date": {"$gt": "2024-01-01"}}
)
```

---

## Database Issues

### "Connection to database failed"

**Problem:** Database not running or wrong credentials

**Solution:**
```bash
# Check database is running
docker ps | grep postgres

# If not running
docker-compose up -d postgres

# Test connection
psql -h localhost -U your_user -d your_db

# Check .env credentials match
# .env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Common mistakes:
# ❌ DATABASE_URL=postgresql://localhost:5432  # Missing user/db
# ✅ DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
```

---

### "Table does not exist"

**Problem:** Migrations not run

**Solution:**
```bash
# Run migrations
python -m alembic upgrade head

# If migrations folder missing, generate
python -m alembic init alembic
python -m alembic revision --autogenerate -m "Initial"
python -m alembic upgrade head
```

---

### "Too many connections"

**Problem:** Connection pool exhausted

**Solution:**
```python
# Increase pool size
# src/db/session.py
engine = create_engine(
    DATABASE_URL,
    pool_size=20,  # Increase from default 5
    max_overflow=40
)

# Or use connection closing
async with get_db_session() as session:
    # Use session
    pass  # Automatically closed
```

---

## Docker Issues

### "Cannot connect to Docker daemon"

**Problem:** Docker not running

**Solution:**

**Windows:**
```powershell
# Start Docker Desktop
# Check: Docker Desktop icon in system tray

# Or via command
Start-Service docker
```

**Ubuntu:**
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

---

### "Port already allocated"

**Problem:** Host port in use

**Solution:**
```bash
# Change port in docker-compose.yml
services:
  app:
    ports:
      - "8001:8000"  # Changed from 8000:8000

# Or stop conflicting container
docker ps
docker stop <container_id>
```

---

### "No space left on device"

**Problem:** Docker disk space full

**Solution:**
```bash
# Clean up
docker system prune -a --volumes

# Check space
docker system df

# Remove unused images
docker image prune -a

# Remove unused volumes
docker volume prune
```

---

## Performance Issues

### "Slow LLM responses"

**Problem:** High latency

**Solution:**
```python
# 1. Use faster models
LLM_MODEL = "gpt-3.5-turbo"  # Faster than GPT-4

# 2. Reduce max tokens
MAX_TOKENS = 500  # Instead of 2000

# 3. Use streaming
async def stream_response(prompt: str):
    async for chunk in llm.stream(prompt):
        yield chunk

# 4. Cache responses
from functools import lru_cache

@lru_cache(maxsize=1000)
def get_response(prompt: str):
    return llm.generate(prompt)

# 5. Use faster providers
# Groq: 10x faster than OpenAI (for some models)
LLM_PROVIDER = "groq"
```

---

### "High memory usage"

**Problem:** Memory leak or large models

**Solution:**
```python
# 1. Use smaller models
import torch

model = AutoModel.from_pretrained(
    "model-name",
    torch_dtype=torch.float16  # Half precision
)

# 2. Clear cache
import gc
gc.collect()
torch.cuda.empty_cache()

# 3. Limit batch size
BATCH_SIZE = 8  # Instead of 32

# 4. Use quantization
model = AutoModel.from_pretrained(
    "model-name",
    load_in_4bit=True
)
```

---

### "Slow vector search"

**Problem:** Large index or inefficient search

**Solution:**
```python
# 1. Use approximate search (FAISS)
import faiss

index = faiss.IndexIVFFlat(
    quantizer, dimension, nlist=100
)
index.nprobe = 10  # Trade accuracy for speed

# 2. Reduce search space
results = vector_store.search(
    query,
    top_k=5,  # Instead of 50
    filter={"category": "relevant"}  # Pre-filter
)

# 3. Use faster vector store
# FAISS (local) > Qdrant > Pinecone (for < 1M vectors)

# 4. Create index with HNSW (faster search)
index = faiss.IndexHNSWFlat(dimension, M=32)
```

---

## Getting Help

### Still stuck?

1. **Check logs:**
   ```bash
   # Application logs
   docker-compose logs -f
   
   # Python traceback
   python src/main.py  # Watch for errors
   ```

2. **Enable debug mode:**
   ```python
   # .env
   DEBUG=true
   LOG_LEVEL=DEBUG
   ```

3. **Search GitHub issues:**
   - https://github.com/aktonay/ONE-CLICK-AI-SPARK/issues
   - Someone may have had the same issue

4. **Ask for help:**
   - **Discussions:** https://github.com/aktonay/ONE-CLICK-AI-SPARK/discussions
   - **New issue:** https://github.com/aktonay/ONE-CLICK-AI-SPARK/issues/new
   - **Email:** asifkhantonay@gmail.com

**When asking for help, include:**
- Command you ran
- Full error message
- Python version (`python --version`)
- OS (Windows/Ubuntu/macOS)
- Package version (`pip show one-click-ai-spark`)

---

## Next Steps

- **[Getting Started](getting-started.md)** - Basics and prerequisites
- **[Quick Start](quick-start.md)** - Build your first project
- **[Advanced Guide](advanced.md)** - Production deployment

