# Quick Start Guide

Build your first AI-powered backend in under 5 minutes! This guide walks you through creating a complete chatbot API with RAG (Retrieval Augmented Generation).

## What You'll Build

A chatbot API that can:
- Answer questions using GPT-4
- Search through your documents for context
- Store conversation history
- Run in Docker containers

**Time required:** 5 minutes  
**Prerequisites:** One Click AI Spark installed ([Installation Guide](installation.md))

---

## Step 1: Generate Your Project (30 seconds)

Open your terminal and run:

### Windows (PowerShell)

```powershell
one-click-ai generate --name my-chatbot --features llm,rag --output ./my-chatbot
```

### Ubuntu/macOS

```bash
one-click-ai generate --name my-chatbot --features llm,rag --output ./my-chatbot
```

**What this does:**
- `--name my-chatbot` - Names your project
- `--features llm,rag` - Adds LLM (GPT) and RAG (document search)
- `--output ./my-chatbot` - Creates project in current directory

**Expected output:**
```
🚀 Generating project: my-chatbot
✓ Created project structure
✓ Generated API endpoints
✓ Configured LLM integration
✓ Set up RAG pipeline
✓ Added Docker configuration
✓ Created tests

✅ Project generated successfully!
📁 Location: ./my-chatbot
```

---

## Step 2: Navigate to Project (5 seconds)

```bash
cd my-chatbot
```

---

## Step 3: Explore the Project Structure (1 minute)

Let's see what was generated:

```
my-chatbot/
├── src/
│   ├── main.py              # Application entry point
│   ├── config.py            # Configuration settings
│   ├── api/
│   │   └── v1/
│   │       ├── chat.py      # Chat endpoints
│   │       └── documents.py # Document upload endpoints
│   ├── core/
│   │   ├── ai/
│   │   │   └── llm.py       # LLM integration (GPT-4, Claude)
│   │   └── rag/
│   │       ├── embeddings.py # Text embeddings
│   │       ├── retriever.py  # Document retrieval
│   │       └── pipeline.py   # RAG pipeline
│   └── db/
│       └── session.py        # Database connection
├── docker/
│   ├── Dockerfile           # Container definition
│   └── docker-compose.yml   # Multi-container setup
├── tests/
│   ├── test_chat.py         # API tests
│   └── test_rag.py          # RAG tests
├── .env.example             # Environment variables template
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

---

## Step 4: Configure Environment Variables (1 minute)

### Copy the template

**Windows:**
```powershell
Copy-Item .env.example .env
```

**Ubuntu/macOS:**
```bash
cp .env.example .env
```

### Add your API keys

Open `.env` in any text editor and add your keys:

```bash
# OpenAI (for GPT-4)
OPENAI_API_KEY=sk-your-key-here

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/chatbot

# Application
APP_NAME=my-chatbot
DEBUG=true
```

**Where to get API keys:**
- **OpenAI**: Sign up at [platform.openai.com](https://platform.openai.com/signup)
  - Go to API Keys → Create new key
  - Free tier: $5 credit
- **Alternative**: Use Anthropic Claude at [console.anthropic.com](https://console.anthropic.com)

---

## Step 5: Install Dependencies (1 minute)

### Create virtual environment (recommended)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Ubuntu/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install packages

```bash
pip install -r requirements.txt
```

**Expected output:**
```
Collecting fastapi...
Collecting openai...
Collecting langchain...
... (many packages)
Successfully installed fastapi-0.109.0 openai-1.10.0 ...
```

---

## Step 6: Start the Server (30 seconds)

```bash
python src/main.py
```

**Expected output:**
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**🎉 Your API is now running!**

---

## Step 7: Test Your Chatbot (1 minute)

### Option A: Using the Interactive Docs (Easiest)

1. Open your browser to: http://127.0.0.1:8000/docs
2. You'll see Swagger UI with all your endpoints
3. Click on `POST /api/v1/chat/message`
4. Click "Try it out"
5. Enter this JSON:
   ```json
   {
     "message": "What is Python?",
     "conversation_id": "test-123"
   }
   ```
6. Click "Execute"

**Expected response:**
```json
{
  "message": "Python is a high-level, interpreted programming language...",
  "conversation_id": "test-123",
  "sources": []
}
```

### Option B: Using cURL (Command Line)

**Windows (PowerShell):**
```powershell
$body = @{
    message = "What is Python?"
    conversation_id = "test-123"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/chat/message" -Method POST -Body $body -ContentType "application/json"
```

**Ubuntu/macOS:**
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/chat/message" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is Python?",
    "conversation_id": "test-123"
  }'
```

### Option C: Using Python

Create a file `test_api.py`:

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/api/v1/chat/message",
    json={
        "message": "What is Python?",
        "conversation_id": "test-123"
    }
)

print(response.json())
```

Run it:
```bash
python test_api.py
```

---

## Step 8: Test RAG (Document Search)

### Upload a document

Create a test file `document.txt`:
```
Python is a high-level programming language created by Guido van Rossum in 1991.
It emphasizes code readability and simplicity.
```

### Upload via API

**Windows (PowerShell):**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/documents/upload" -Method POST -InFile "document.txt"
```

**Ubuntu/macOS:**
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/documents/upload" \
  -F "file=@document.txt"
```

### Ask a question about your document

```bash
# Now ask a question - it will use your document!
curl -X POST "http://127.0.0.1:8000/api/v1/chat/message" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Who created Python?",
    "conversation_id": "test-123"
  }'
```

**Response will include:**
```json
{
  "message": "According to your document, Python was created by Guido van Rossum in 1991.",
  "conversation_id": "test-123",
  "sources": ["document.txt"]
}
```

---

## Understanding What You Built

### The LLM Component

Located in `src/core/ai/llm.py`:

```python
class LLMService:
    """Handles communication with OpenAI/Claude"""
    
    async def generate_response(self, prompt: str) -> str:
        # Sends your question to GPT-4
        # Returns the AI's response
```

### The RAG Pipeline

Located in `src/core/rag/pipeline.py`:

```python
class RAGPipeline:
    """Retrieval Augmented Generation"""
    
    async def query(self, question: str) -> dict:
        # 1. Converts question to embeddings
        # 2. Searches your documents
        # 3. Sends relevant context + question to LLM
        # 4. Returns answer with sources
```

### The API Endpoints

Located in `src/api/v1/chat.py`:

```python
@router.post("/message")
async def chat_message(request: ChatRequest):
    # 1. Receives your message
    # 2. Retrieves relevant documents
    # 3. Generates AI response
    # 4. Stores in conversation history
    # 5. Returns response
```

---

## Next Steps

### Level 1: Explore More Features

```bash
# Generate project with more features
one-click-ai generate \
  --name advanced-bot \
  --features llm,rag,voice,emotion \
  --output ./advanced-bot
```

**New features:**
- `voice` - Speech-to-text and text-to-speech
- `emotion` - Detect emotions in text

### Level 2: Customize Your Bot

Edit `src/config.py` to change:
- LLM model (GPT-3.5, GPT-4, Claude)
- Temperature (creativity level)
- Max tokens (response length)
- System prompts (bot personality)

Example:
```python
# src/config.py
LLM_MODEL = "gpt-4"
LLM_TEMPERATURE = 0.7  # 0 = factual, 1 = creative
MAX_TOKENS = 500
SYSTEM_PROMPT = "You are a helpful coding assistant."
```

### Level 3: Deploy with Docker

```bash
# Build container
docker build -t my-chatbot .

# Run container
docker run -p 8000:8000 --env-file .env my-chatbot
```

### Level 4: Run Tests

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_chat.py

# Run with coverage
pytest --cov=src
```

---

## Common Workflows

### Adding More Documents

```bash
# Upload PDF
curl -X POST "http://127.0.0.1:8000/api/v1/documents/upload" \
  -F "file=@manual.pdf"

# Upload multiple files
curl -X POST "http://127.0.0.1:8000/api/v1/documents/upload" \
  -F "file=@doc1.txt" \
  -F "file=@doc2.pdf"
```

### Clearing Conversation History

```bash
curl -X DELETE "http://127.0.0.1:8000/api/v1/chat/conversation/test-123"
```

### Monitoring Logs

The server logs show all activity:
```
INFO:     127.0.0.1:52844 - "POST /api/v1/chat/message HTTP/1.1" 200 OK
INFO:     Processing message: What is Python?
INFO:     Retrieved 2 relevant documents
INFO:     Generated response in 1.23s
```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'fastapi'"

**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### "OpenAI API key not found"

**Solution:** Check your `.env` file has:
```bash
OPENAI_API_KEY=sk-your-actual-key-here
```

### "Address already in use"

**Solution:** Port 8000 is busy. Use different port:
```bash
python src/main.py --port 8001
```

Or kill the existing process:

**Windows:**
```powershell
Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess | Stop-Process
```

**Ubuntu/macOS:**
```bash
lsof -ti:8000 | xargs kill
```

### "Database connection failed"

**Solution:** Update `.env` with correct database URL, or use SQLite for testing:
```bash
DATABASE_URL=sqlite:///./chatbot.db
```

---

## What to Learn Next

Now that you have a working chatbot, explore:

1. **[Features Guide](features.md)** - Learn about all 15+ AI features
2. **[Examples](examples.md)** - More real-world projects
3. **[Advanced Guide](advanced.md)** - Production deployment, scaling
4. **[API Reference](api.md)** - Complete command documentation

---

## Real-World Example: Building a Support Bot

Let's extend your chatbot into a customer support bot:

### 1. Upload your knowledge base

```bash
# Upload FAQs, manuals, policies
curl -X POST "http://127.0.0.1:8000/api/v1/documents/upload" \
  -F "file=@faq.pdf" \
  -F "file=@user_manual.pdf" \
  -F "file=@refund_policy.txt"
```

### 2. Customize the system prompt

Edit `src/config.py`:
```python
SYSTEM_PROMPT = """You are a helpful customer support agent.
- Be polite and professional
- Use information from the knowledge base
- If you don't know, say so and offer to escalate
- Include relevant document sources in your answer
"""
```

### 3. Add conversation memory

The bot already tracks conversations by `conversation_id`. Each customer gets their own ID:

```python
# Customer A's conversation
response = requests.post("http://127.0.0.1:8000/api/v1/chat/message", json={
    "message": "How do I reset my password?",
    "conversation_id": "customer-12345"
})

# Follow-up - bot remembers context
response = requests.post("http://127.0.0.1:8000/api/v1/chat/message", json={
    "message": "What if I don't receive the email?",
    "conversation_id": "customer-12345"  # Same ID = same conversation
})
```

### 4. Test the bot

```bash
# Customer question
curl -X POST "http://127.0.0.1:8000/api/v1/chat/message" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is your refund policy?",
    "conversation_id": "customer-789"
  }'

# Bot responds with info from refund_policy.txt
```

**🎉 You now have a working support bot!**

---

## Congratulations! 🎉

You've built and tested your first AI-powered backend in under 5 minutes!

**What you accomplished:**
- ✅ Generated a complete FastAPI project
- ✅ Integrated LLM (GPT-4)
- ✅ Implemented RAG for document search
- ✅ Tested chat and document upload
- ✅ Understood the architecture

**Ready for more?** Continue to:
- **[Features Guide](features.md)** - Explore all 15+ features
- **[Examples](examples.md)** - More project ideas
- **[Advanced Guide](advanced.md)** - Deploy to production

