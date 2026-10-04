# Features Guide

One Click AI Spark supports 25+ AI features across multiple categories. This guide explains each feature, when to use it, and real-world use cases.

## Table of Contents

- [Core AI Features](#core-ai-features)
- [Multimodal AI](#multimodal-ai)
- [Machine Learning](#machine-learning)
- [Infrastructure & DevOps](#infrastructure--devops)
- [Advanced Features](#advanced-features)
- [Feature Combinations](#feature-combinations)

---

## Core AI Features

### 1. LLM (Large Language Models)

**What it does:** Integrates GPT-4, Claude, Gemini, and other AI models for text generation, chat, and completion.

**Use cases:**
- Chatbots and virtual assistants
- Content generation (articles, emails, code)
- Text summarization and translation
- Question answering
- Code generation and debugging

**Providers supported:**
- OpenAI (GPT-3.5, GPT-4, GPT-4 Turbo)
- Anthropic (Claude 3 Opus, Sonnet, Haiku)
- Google (Gemini Pro, Ultra)
- Groq (Fast inference)
- Mistral, DeepSeek, Meta Llama
- Ollama (self-hosted)

**Example command:**
```bash
one-click-ai generate --name my-chatbot --features llm --llm-provider openai
```

**Generated files:**
- `src/core/ai/llm.py` - LLM service wrapper
- `src/api/v1/chat.py` - Chat endpoints
- `src/config.py` - Model configuration

**Configuration:**
```python
# .env
OPENAI_API_KEY=sk-your-key
LLM_MODEL=gpt-4
LLM_TEMPERATURE=0.7
MAX_TOKENS=2000
```

---

### 2. RAG (Retrieval Augmented Generation)

**What it does:** Allows AI to search your documents and use them as context for answers.

**Use cases:**
- Internal knowledge bases
- Document Q&A systems
- Customer support with company docs
- Research paper analysis
- Legal document review

**How it works:**
1. Uploads documents (PDF, TXT, DOCX)
2. Converts to embeddings (vector representations)
3. Stores in vector database
4. Retrieves relevant chunks when asked
5. Sends to LLM with context

**Vector stores supported:**
- FAISS (local, fast)
- Pinecone (cloud, scalable)
- Qdrant (open-source)
- Weaviate, Chroma, Milvus
- PostgreSQL with pgvector
- LanceDB

**Example command:**
```bash
one-click-ai generate --name doc-qa --features llm,rag --vector-store pinecone
```

**Generated files:**
- `src/core/rag/embeddings.py` - Text embedding service
- `src/core/rag/retriever.py` - Document retrieval
- `src/core/rag/pipeline.py` - RAG orchestration
- `src/api/v1/documents.py` - Document upload API

**Configuration:**
```python
# .env
OPENAI_API_KEY=sk-your-key
PINECONE_API_KEY=your-key
PINECONE_ENVIRONMENT=us-east-1
EMBEDDING_MODEL=text-embedding-3-small
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

---

### 3. Voice (Speech-to-Text & Text-to-Speech)

**What it does:** Converts speech to text and text to speech for voice applications.

**Use cases:**
- Voice assistants
- Call center automation
- Voice note transcription
- Accessibility features
- Voice-controlled apps

**STT (Speech-to-Text) providers:**
- OpenAI Whisper (high accuracy)
- Google Speech-to-Text
- Deepgram (real-time)
- AssemblyAI (advanced features)
- Azure Speech

**TTS (Text-to-Speech) providers:**
- ElevenLabs (ultra-realistic)
- OpenAI TTS
- Google Text-to-Speech
- Azure Neural TTS
- Coqui TTS (open-source)

**Example command:**
```bash
one-click-ai generate --name voice-app --features llm,voice --stt-provider openai --tts-provider elevenlabs
```

**Generated files:**
- `src/core/multimodal/stt.py` - Speech recognition
- `src/core/multimodal/tts.py` - Speech synthesis
- `src/api/v1/voice.py` - Voice endpoints

**API example:**
```python
# Upload audio file
response = requests.post(
    "http://localhost:8000/api/v1/voice/transcribe",
    files={"audio": open("recording.mp3", "rb")}
)
# Returns: {"text": "Hello, how can I help you?"}

# Generate speech
response = requests.post(
    "http://localhost:8000/api/v1/voice/synthesize",
    json={"text": "Hello! How can I help you today?"}
)
# Returns audio file
```

---

### 4. Voice-to-Voice

**What it does:** Real-time conversational AI that listens, thinks, and responds with voice.

**Use cases:**
- Voice assistants (Alexa/Siri-like)
- Phone support bots
- Language learning tutors
- Voice-based customer service
- Hands-free applications

**How it works:**
1. User speaks → STT converts to text
2. Text sent to LLM for processing
3. LLM response → TTS converts to speech
4. Audio streamed back to user

**Example command:**
```bash
one-click-ai generate --name voice-assistant --features llm,voice,voice-to-voice
```

**Generated files:**
- `src/core/multimodal/voice_pipeline.py` - End-to-end pipeline
- `src/api/v1/voice_chat.py` - Voice chat WebSocket

**Real-time WebSocket API:**
```javascript
const ws = new WebSocket('ws://localhost:8000/api/v1/voice/chat');

ws.onopen = () => {
  // Send audio chunks
  ws.send(audioBlob);
};

ws.onmessage = (event) => {
  // Receive AI audio response
  playAudio(event.data);
};
```

---

### 5. Vision (Image & Video Analysis)

**What it does:** Analyzes images and videos for object detection, classification, OCR, and more.

**Use cases:**
- Product recognition
- Content moderation
- Medical image analysis
- Document scanning (OCR)
- Surveillance and security
- Quality control in manufacturing

**Providers:**
- OpenAI Vision (GPT-4V)
- Google Vision AI
- AWS Rekognition
- Azure Computer Vision
- Anthropic Claude 3 (vision)
- Ultralytics (YOLO)

**Example command:**
```bash
one-click-ai generate --name vision-app --features vision --vision-provider openai
```

**Generated files:**
- `src/cv/inference.py` - Vision model inference
- `src/api/v1/vision.py` - Vision endpoints

**API example:**
```python
# Analyze image
response = requests.post(
    "http://localhost:8000/api/v1/vision/analyze",
    files={"image": open("photo.jpg", "rb")},
    data={"prompt": "What objects are in this image?"}
)
# Returns: {"description": "A cat sitting on a laptop", "objects": ["cat", "laptop"]}
```

---

### 6. Emotion Detection

**What it does:** Detects emotions in text, voice, or video for sentiment analysis.

**Use cases:**
- Customer feedback analysis
- Mental health monitoring
- Call center quality assurance
- Social media sentiment
- User experience research

**Providers:**
- Hume AI (voice + video emotions)
- Azure Emotion API
- Affectiva

**Example command:**
```bash
one-click-ai generate --name emotion-app --features llm,emotion --emotion-provider hume
```

**API example:**
```python
# Analyze text emotion
response = requests.post(
    "http://localhost:8000/api/v1/emotion/analyze",
    json={"text": "I'm so frustrated with this service!"}
)
# Returns: {"emotion": "anger", "confidence": 0.87, "valence": -0.6}

# Analyze voice emotion
response = requests.post(
    "http://localhost:8000/api/v1/emotion/voice",
    files={"audio": open("call.mp3", "rb")}
)
# Returns: {"emotions": [{"emotion": "frustration", "timestamp": 2.3, "confidence": 0.82}]}
```

---

### 7. Web Search

**What it does:** Integrates real-time web search into your AI for up-to-date information.

**Use cases:**
- Research assistants
- News aggregation
- Real-time fact-checking
- Market research
- Competitor analysis

**Providers:**
- Tavily (AI-optimized search)
- SerpAPI (Google results)
- Brave Search
- Perplexity AI
- DuckDuckGo

**Example command:**
```bash
one-click-ai generate --name search-bot --features llm,search --search-provider tavily
```

**API example:**
```python
response = requests.post(
    "http://localhost:8000/api/v1/chat/message",
    json={
        "message": "What are the latest AI news today?",
        "use_search": True
    }
)
# AI will search the web and answer with current information
```

---

### 8. AI Agents

**What it does:** Multi-step reasoning agents that use tools to accomplish complex tasks.

**Use cases:**
- Task automation
- Data analysis workflows
- Research assistants
- Code generation and debugging
- Multi-step problem solving

**How it works:**
1. Agent receives goal
2. Plans steps to achieve goal
3. Executes tools (search, calculator, code, API calls)
4. Iterates until goal is met

**Example command:**
```bash
one-click-ai generate --name agent-app --features llm,agents,search,rag
```

**Generated files:**
- `src/core/agents/planner.py` - Planning logic
- `src/core/agents/executor.py` - Tool execution
- `src/core/agents/tools.py` - Available tools

**Example:**
```python
# Ask agent to research and summarize
response = requests.post(
    "http://localhost:8000/api/v1/agent/task",
    json={
        "goal": "Research the top 3 AI trends in 2024 and create a summary report",
        "tools": ["web_search", "document_writer"]
    }
)
# Agent will:
# 1. Search web for AI trends
# 2. Analyze results
# 3. Write formatted report
```

---

### 9. Memory System

**What it does:** Gives AI short-term and long-term memory across conversations.

**Use cases:**
- Personalized chatbots
- Multi-session conversations
- User preference learning
- Context retention
- Progressive disclosure

**Memory types:**
- **Short-term**: Current conversation context
- **Long-term**: User preferences, history, facts
- **Semantic**: Key concepts and relationships
- **Episodic**: Specific events and interactions

**Example command:**
```bash
one-click-ai generate --name memory-bot --features llm,memory --session-backend redis
```

**How it works:**
```python
# First conversation
POST /api/v1/chat/message
{
  "message": "My name is Alice and I love Python",
  "user_id": "user-123"
}

# Later conversation (different day)
POST /api/v1/chat/message
{
  "message": "What's my name?",
  "user_id": "user-123"
}
# Response: "Your name is Alice, and I remember you love Python!"
```

---

## Multimodal AI

### 10. Computer Vision

**What it does:** Advanced CV tasks like object detection, segmentation, face recognition, OCR.

**Use cases:**
- Security systems (face recognition)
- Inventory management (object counting)
- Document digitization (OCR)
- Quality inspection
- Medical imaging

**Frameworks:**
- YOLO (object detection)
- SAM2 (segmentation)
- OCR engines (Tesseract, PaddleOCR)
- Face detection (MediaPipe, Dlib)
- Image generation (Stable Diffusion)

**Example command:**
```bash
one-click-ai generate --name cv-app --features computer_vision --cv-frameworks yolo,sam,ocr
```

**Generated files:**
- `src/cv/yolo_detector.py` - YOLO detection
- `src/cv/sam_segmenter.py` - SAM2 segmentation
- `src/cv/ocr_engine.py` - OCR processing
- `src/cv/face_detector.py` - Face detection

**API examples:**
```python
# Object detection
response = requests.post(
    "http://localhost:8000/api/v1/cv/detect",
    files={"image": open("street.jpg", "rb")}
)
# Returns: {"objects": [{"class": "car", "confidence": 0.95, "bbox": [x, y, w, h]}]}

# OCR
response = requests.post(
    "http://localhost:8000/api/v1/cv/ocr",
    files={"image": open("document.jpg", "rb")}
)
# Returns: {"text": "Extracted text from document..."}
```

---

### 11. ML Training

**What it does:** Train custom machine learning models on your data.

**Use cases:**
- Custom text classification
- Predictive analytics
- Recommendation systems
- Time series forecasting
- Anomaly detection

**Frameworks:**
- PyTorch
- TensorFlow
- scikit-learn
- XGBoost
- LightGBM
- JAX

**Example command:**
```bash
one-click-ai generate --name ml-app --features ml_training --ml-frameworks pytorch,xgboost
```

**Generated files:**
- `src/ml/trainer.py` - Training pipeline
- `src/ml/models.py` - Model definitions
- `src/ml/preprocessor.py` - Data preprocessing
- `src/api/v1/training.py` - Training endpoints

**Training workflow:**
```python
# 1. Upload training data
response = requests.post(
    "http://localhost:8000/api/v1/ml/upload_data",
    files={"data": open("training_data.csv", "rb")}
)

# 2. Start training
response = requests.post(
    "http://localhost:8000/api/v1/ml/train",
    json={
        "model_type": "classifier",
        "target_column": "label",
        "epochs": 10
    }
)

# 3. Make predictions
response = requests.post(
    "http://localhost:8000/api/v1/ml/predict",
    json={"features": [1.2, 3.4, 5.6]}
)
```

---

### 12. Edge AI

**What it does:** Optimizes AI models for edge devices (phones, IoT, embedded systems).

**Use cases:**
- Mobile apps with on-device AI
- IoT devices
- Raspberry Pi projects
- Offline AI applications
- Low-latency inference

**Runtimes:**
- ONNX (cross-platform)
- TensorRT (NVIDIA GPUs)
- OpenVINO (Intel CPUs/GPUs)
- TensorFlow Lite (mobile)
- CoreML (iOS/macOS)

**Example command:**
```bash
one-click-ai generate --name edge-app --features edge_ai --edge-runtimes onnx,tensorrt
```

**Generated files:**
- `src/edge/converter.py` - Model conversion
- `src/edge/optimizer.py` - Quantization, pruning
- `src/edge/runtime.py` - Inference engine

**Optimization workflow:**
```python
# Convert PyTorch model to ONNX
response = requests.post(
    "http://localhost:8000/api/v1/edge/convert",
    json={
        "model_path": "models/my_model.pth",
        "format": "onnx",
        "quantization": "int8"
    }
)
# Returns optimized model 5-10x smaller and faster
```

---

## Infrastructure & DevOps

### 13. Docker

**What it does:** Containerizes your application for consistent deployment anywhere.

**Generated files:**
- `Dockerfile` - Production container
- `Dockerfile.dev` - Development container
- `docker-compose.yml` - Multi-service orchestration
- `docker-compose.dev.yml` - Dev environment
- `nginx.conf` - Reverse proxy config
- `entrypoint.sh` - Container startup script

**Commands:**
```bash
# Development
docker-compose -f docker-compose.dev.yml up

# Production
docker-compose up -d

# Build
docker build -t my-app .

# Run
docker run -p 8000:8000 --env-file .env my-app
```

---

### 14. CI/CD (GitHub Actions)

**What it does:** Automates testing and deployment on every code push.

**Generated workflows:**
- `.github/workflows/test.yml` - Run tests
- `.github/workflows/lint.yml` - Code quality checks
- `.github/workflows/deploy.yml` - Auto-deploy to production

**What happens on push:**
1. Runs tests (pytest)
2. Checks code style (black, flake8)
3. Builds Docker image
4. Deploys to production (if main branch)

---

### 15. Infrastructure as Code (IaC)

**What it does:** Automates cloud infrastructure setup.

**Generated files:**
- `iac/terraform/` - AWS/GCP/Azure infrastructure
- `iac/ansible/` - Server configuration

**Resources created:**
- EC2/VM instances
- Load balancers
- Databases (RDS/Cloud SQL)
- S3/Storage buckets
- VPCs and security groups

**Commands:**
```bash
# Initialize
cd iac/terraform
terraform init

# Plan changes
terraform plan

# Apply
terraform apply
```

---

### 16. Monitoring

**What it does:** Tracks application health, performance, and errors.

**Tools:**
- **Prometheus** - Metrics collection
- **Grafana** - Dashboards
- **Sentry** - Error tracking

**Generated files:**
- `monitoring/prometheus.yml` - Metrics config
- `monitoring/grafana_dashboard.json` - Dashboard
- `monitoring/alerts.yml` - Alert rules

**Metrics tracked:**
- Request rate and latency
- Error rates
- LLM token usage
- Database connections
- Memory/CPU usage

**Access dashboards:**
- Grafana: http://localhost:3000
- Prometheus: http://localhost:9090

---

## Advanced Features

### 17. Guardrails & Safety

**What it does:** Protects your AI from harmful content and misuse.

**Protection layers:**
- Content filtering (hate speech, violence)
- PII detection and removal (emails, SSN, credit cards)
- Prompt injection detection
- Jailbreak prevention
- Rate limiting
- Audit logging

**Example command:**
```bash
one-click-ai generate --name safe-bot --features llm,guardrails
```

**Generated files:**
- `src/guardrails/content_filter.py`
- `src/guardrails/pii_detector.py`
- `src/guardrails/prompt_validator.py`
- `src/guardrails/audit_logger.py`

---

### 18. Analytics (Text-to-SQL)

**What it does:** Natural language queries for your database.

**Use cases:**
- Business intelligence dashboards
- Data analysis without SQL knowledge
- Automated reporting
- Self-service analytics

**Example command:**
```bash
one-click-ai generate --name analytics-app --features llm,analytics
```

**API example:**
```python
response = requests.post(
    "http://localhost:8000/api/v1/analytics/query",
    json={"question": "What were our top 5 products last month?"}
)
# Returns: SQL query + results
```

---

### 19. Multi-tenancy

**What it does:** Isolates data for multiple customers/organizations.

**Use cases:**
- SaaS applications
- Enterprise deployments
- White-label solutions

**Features:**
- Tenant-isolated databases
- Separate vector stores
- Per-tenant rate limits
- Usage tracking

---

### 20. Fine-tuning

**What it does:** Customize AI models on your data.

**Methods:**
- LoRA (Low-Rank Adaptation)
- QLoRA (Quantized LoRA)
- PEFT (Parameter-Efficient Fine-Tuning)

**Use cases:**
- Domain-specific language (legal, medical)
- Brand voice consistency
- Task-specific optimization

---

## Feature Combinations

### Powerful Combinations

**1. RAG + Agents + Search**
```bash
one-click-ai generate --name research-assistant \
  --features llm,rag,agents,search
```
**Result:** AI that searches web + your docs, plans research, writes reports

**2. Voice + Vision + LLM**
```bash
one-click-ai generate --name multimodal-app \
  --features llm,voice,vision
```
**Result:** AI that sees, hears, and responds (like GPT-4V + voice)

**3. ML + Edge + CV**
```bash
one-click-ai generate --name edge-vision \
  --features ml_training,edge_ai,computer_vision
```
**Result:** Train custom vision models, deploy to edge devices

**4. Full Stack AI Product**
```bash
one-click-ai generate --name ai-saas \
  --features llm,rag,voice,vision,agents,memory,guardrails,analytics,docker,ci_cd,monitoring
```
**Result:** Production-ready AI SaaS with everything

---

## Quick Reference

| Feature | Command Flag | Best For |
|---------|--------------|----------|
| LLM | `llm` | Chat, completion, generation |
| RAG | `rag` | Document Q&A, knowledge bases |
| Voice | `voice` | Speech apps, transcription |
| Voice-to-Voice | `voice_to_voice` | Conversational AI |
| Vision | `vision` | Image/video analysis |
| Emotion | `emotion` | Sentiment analysis |
| Search | `search` | Real-time info, research |
| Agents | `agents` | Complex task automation |
| Memory | `memory` | Personalized experiences |
| Computer Vision | `computer_vision` | Object detection, OCR |
| ML Training | `ml_training` | Custom models |
| Edge AI | `edge_ai` | Mobile, IoT, offline |
| Docker | `docker` | Containerization |
| CI/CD | `ci_cd` | Automation |
| IaC | `iac` | Cloud infrastructure |
| Monitoring | `monitoring` | Observability |
| Guardrails | `guardrails` | Safety, compliance |
| Analytics | `analytics` | Text-to-SQL |
| Multi-tenant | `multi_tenant` | SaaS |
| Fine-tuning | `fine_tuning` | Model customization |

---

## Next Steps

- **[Examples](examples.md)** - See real-world projects using these features
- **[Advanced Guide](advanced.md)** - Production deployment and scaling
- **[API Reference](api.md)** - Complete command documentation

