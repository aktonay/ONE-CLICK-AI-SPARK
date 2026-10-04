<a name="top"></a>

![One Click AI Spark Banner](https://raw.githubusercontent.com/aktonay/ONE-CLICK-AI/main/banner.svg)

# 🤖 One Click AI Spark 🚀

**One Click AI Spark** is a powerful CLI tool that generates **production-ready AI backend projects** in seconds — powered by FastAPI, with built-in LLM integration, RAG pipelines, voice, vision, emotion detection, AI agents, **ML training (PyTorch, TensorFlow, scikit-learn, XGBoost, LightGBM)**, **computer vision (YOLO, SAM2, OCR, face detection, image generation)**, **edge AI (ONNX, TensorRT, quantization)**, **LLM fine-tuning (LoRA/QLoRA)**, **AI guardrails (PII, content filter, prompt injection)**, **conversational analytics (Text-to-SQL)**, Docker, CI/CD, IaC, and full observability.

[![PyPI version](https://img.shields.io/pypi/v/one-click-ai-spark)](https://pypi.org/project/one-click-ai-spark/)
[![Python versions](https://img.shields.io/pypi/pyversions/one-click-ai-spark)](https://pypi.org/project/one-click-ai-spark/)
[![License](https://img.shields.io/github/license/aktonay/ONE-CLICK-AI)](https://github.com/aktonay/ONE-CLICK-AI/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/aktonay/ONE-CLICK-AI?style=social)](https://github.com/aktonay/ONE-CLICK-AI)

### 🛠️ Technology Stack

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=white)](https://openai.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://docker.com)
[![Terraform](https://img.shields.io/badge/Terraform-7B42BC?logo=terraform&logoColor=white)](https://terraform.io)
[![Ansible](https://img.shields.io/badge/Ansible-EE0000?logo=ansible&logoColor=white)](https://ansible.com)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?logo=prometheus&logoColor=white)](https://prometheus.io)
[![Grafana](https://img.shields.io/badge/Grafana-F46800?logo=grafana&logoColor=white)](https://grafana.com)
[![Redis](https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white)](https://redis.io)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)](https://postgresql.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org)
[![ONNX](https://img.shields.io/badge/ONNX-005CED?logo=onnx&logoColor=white)](https://onnx.ai)
[![Ultralytics](https://img.shields.io/badge/YOLO-111F68?logo=yolo&logoColor=white)](https://ultralytics.com)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co)
[![Ollama](https://img.shields.io/badge/Ollama-000000?logo=ollama&logoColor=white)](https://ollama.com)

⭐ **Star us on GitHub** — your support motivates us a lot! 🙏😊

[![Follow Mohammad Asif Khan](https://img.shields.io/badge/Follow-LinkedIn-0A66C2?logo=linkedin)](https://www.linkedin.com/in/mohammad-asif-khan-tonay-795b641b6)
[![Share on LinkedIn](https://img.shields.io/badge/Share-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/aktonay/ONE-CLICK-AI)

---

> ⚡ **Stop copy-pasting boilerplate. Start building what matters.** ⚡

## 🌟 The Story Behind One Click AI Spark

Every time a new AI project starts, I see the same cycle — developers lose **days** reinventing the same infrastructure:

- **Provider Headaches:** Writing LLM client wrappers for OpenAI, Anthropic, Google, Groq — over and over.
- **RAG Nightmares:** Stitching together document ingestion, chunking, embedding, vector stores, and retrieval from scratch.
- **Multimodal Chaos:** Integrating STT, TTS, vision, and emotion detection with no standard structure.
- **Infrastructure Fatigue:** Manually setting up Dockerfiles, CI/CD pipelines, Terraform configs, Prometheus dashboards — before writing a single line of AI logic.
- **Confidence Gap:** After hours of wiring, nobody is 100% sure the architecture is production-ready.

**One Click AI** was born to eliminate this. It generates a battle-tested, modular AI backend in **seconds** — with every integration wired up, every best practice baked in, and every deployment tool ready to go. No more boilerplate, no more forgotten configs — just one command to start building real AI applications.

## 🚀 What You Get with `ocd-ai`

When you run `ocd-ai init`, you don't just get a folder — you get a **complete AI production environment**:

- **🧠 Multi-Provider LLM:** Pre-configured clients for OpenAI, Anthropic, Google, Groq, Grok, Cohere, Mistral, and Ollama — swap providers with a config change.
- **📚 RAG Pipeline:** Full document ingestion → smart chunking → embedding → vector retrieval → LLM generation pipeline, ready to go.
- **🎤 Voice & Audio:** Whisper/Deepgram STT + OpenAI/ElevenLabs TTS + real-time voice-to-voice conversation.
- **👁️ Vision & Emotion:** Image/video analysis (GPT-4o, Claude, Gemini) + emotion detection (Hume AI + LLM fallback).
- **🤖 AI Agents:** ReAct-style agents with built-in tool use and web search (Tavily, Serper, DuckDuckGo).
- **🧠 Memory:** Short-term (in-context) + long-term (persistent) conversation memory with session management.
- **⚡ Streaming:** SSE + WebSocket streaming for real-time responses.
- **🐳 Docker Ready:** Multi-stage Dockerfiles + docker-compose for dev and production with Nginx reverse proxy.
- **⚙️ CI/CD (GitHub Actions):** Pre-configured workflows for testing, linting, and automated deployment.
- **🏗️ Infrastructure as Code:** Terraform templates for AWS + Ansible playbooks for server configuration.
- **📊 Monitoring & Observability:** Prometheus metrics + Grafana dashboards + alerting rules — all pre-configured.
- **📊 Vector Store Flexibility:** Choose from FAISS, Pinecone, Qdrant, Weaviate, ChromaDB, Milvus, or pgvector.
- **🔒 Standard .gitignore & .env:** Pre-configured environment files with secrets management best practices.
- **🚀 GitHub Integration:** Auto-initializes a git repo and pushes to a new GitHub repository in one go.
- **🔬 ML Training Pipelines:** PyTorch, TensorFlow, scikit-learn, XGBoost, LightGBM — with trainers, predictors, feature engineering, model registry, and experiment tracking (MLflow/W&B).
- **🖼️ Computer Vision:** YOLO (object detection), SAM2 (segmentation), EasyOCR/Tesseract (OCR), face detection/recognition, Stable Diffusion (image generation).
- **⚡ Edge AI Deployment:** ONNX Runtime, TensorRT conversion, INT8 quantization, model optimization, benchmarking.
- **🔧 LLM Fine-Tuning:** LoRA/QLoRA fine-tuning with PEFT + Transformers, merge & export for deployment.
- **🛡️ AI Guardrails:** Content safety (Detoxify), PII detection/anonymization (Presidio), prompt injection defense, audit logging.
- **📊 Conversational Analytics:** Natural language → SQL (Text-to-SQL), auto-chart generation (Plotly), report builder.
- **🏠 Ollama Local Deployment:** Self-hosted LLM inference via Ollama in docker-compose.
- **🚀 One-Command Deploy:** Deploy to AWS ECS, Google Cloud Run, Azure Container Apps, DigitalOcean, Railway, Fly.io, Render, or any VPS — with `ocd-ai deploy`.

## ✨ Feature Matrix

| Feature | Description |
|---------|-------------|
| 🧠 **LLM Chat** | Multi-provider support (OpenAI, Anthropic, Google, Groq, Grok, Cohere, Mistral, Ollama) |
| 📚 **RAG Pipeline** | Document ingestion → chunking → embedding → retrieval → generation |
| 🎤 **Voice (STT/TTS)** | Speech-to-Text (Whisper, Deepgram) + Text-to-Speech (OpenAI, ElevenLabs) |
| 🗣️ **Voice-to-Voice** | Real-time audio conversation pipeline |
| 👁️ **Vision** | Image & video analysis with GPT-4o, Claude, Gemini |
| 😊 **Emotion Detection** | Audio/text emotion analysis (Hume AI + LLM fallback) |
| 🔍 **Web Search** | Internet search (Tavily, Serper, DuckDuckGo) with LLM summarization |
| 🤖 **AI Agents** | ReAct-style agents with tool use |
| 🧠 **Memory** | Short-term + long-term conversation memory |
| ⚡ **Streaming** | SSE + WebSocket streaming responses |
| 🔐 **Sessions** | Persistent session management (Redis-backed) |
| 📊 **Vector Stores** | FAISS, Pinecone, Qdrant, Weaviate, ChromaDB, Milvus, pgvector |
| 🐳 **Docker** | Production + dev Dockerfiles, docker-compose, Nginx |
| 🔄 **CI/CD** | GitHub Actions (test, lint, deploy) |
| 🏗️ **IaC** | Terraform (AWS) + Ansible server configuration |
| 📈 **Monitoring** | Prometheus + Grafana + alerts |
| 🔬 **ML Training** | PyTorch, TensorFlow, scikit-learn, XGBoost, LightGBM pipelines |
| 🖼️ **Computer Vision** | YOLO detection, SAM2 segmentation, OCR, face detection, image generation |
| ⚡ **Edge AI** | ONNX Runtime, TensorRT, INT8 quantization, model benchmarking |
| 🔧 **Fine-Tuning** | LoRA/QLoRA fine-tuning with PEFT + Transformers |
| 🧪 **MLOps** | MLflow + Weights & Biases experiment tracking |
| 🛡️ **Guardrails** | Content filter (Detoxify), PII detection (Presidio), prompt injection defense |
| 📊 **Analytics** | Text-to-SQL, auto-chart generation (Plotly), report builder |
| 🏠 **Ollama** | Local LLM deployment via docker-compose |
| 🎯 **GPU Support** | CUDA-accelerated training, mixed precision (FP16/BF16) |
| 📋 **Audit Logging** | Full AI interaction audit trail for compliance |
| 🚀 **One-Command Deploy** | Deploy to AWS, GCP, Azure, DigitalOcean, Railway, Fly.io, Render, or VPS |

## 📦 Installation

Since **one-click-ai** is a CLI tool, it is recommended to install it globally using `uv`:

```bash
uv tool install one-click-ai
```

If your system doesn't have `uv` yet, follow the [installation guide here](https://docs.astral.sh/uv/getting-started/installation/).

Alternatively, you can use pip:

```bash
pip install one-click-ai
```

## 🚀 Usage

### Initialize a Full AI Project (everything enabled)

```bash
ocd-ai init my-ai-project --all
```

This creates a new folder `my-ai-project` with a complete production-ready AI backend.

### Initialize in the Current Directory

```bash
ocd-ai init .
```

### 🤖 Chatbot (LLM Only)

```bash
ocd-ai init my-chatbot --llm-only --openai --docker
```

### 📚 RAG Application

```bash
ocd-ai init my-rag-app --rag --openai --faiss --docker --ci-cd
```

### 🎤 Voice Assistant

```bash
ocd-ai init my-voice-app --voice --voice-to-voice --openai --streaming --docker
```

### 👁️ Vision + Emotion Analysis

```bash
ocd-ai init my-vision-app --vision --emotion --openai --google --docker
```

### 🤖 AI Agent with Search & Memory

```bash
ocd-ai init my-agent --agents --search --memory --openai --streaming --docker --ci-cd
```

### 🚀 Full Multi-Provider Stack

```bash
ocd-ai init my-enterprise-app \
    --rag --agents --search --memory --streaming --voice --vision --emotion \
    --openai --anthropic --google --groq \
    --faiss --qdrant \
    --postgres --redis \
    --docker --ci-cd --iac --monitoring
```

### 🔬 ML Training Pipeline

```bash
ocd-ai init my-ml-project --ml-training --pytorch --sklearn --xgboost --mlops --docker
```

### 🖼️ Computer Vision

```bash
ocd-ai init my-cv-project --computer-vision --yolo --sam --ocr --face-detection --gpu --docker
```

### 🔧 LLM Fine-Tuning (LoRA/QLoRA)

```bash
ocd-ai init my-finetune --fine-tuning --pytorch --gpu --mlops --docker
```

### ⚡ Edge AI Deployment

```bash
ocd-ai init my-edge-project --edge-ai --onnx --tensorrt --quantization --docker
```

### 🛡️ AI Guardrails

```bash
ocd-ai init my-safe-ai --guardrails --openai --rag --docker
```

### 📊 Conversational Analytics

```bash
ocd-ai init my-analytics --analytics --openai --docker
```

### 🖼️ Image Generation

```bash
ocd-ai init my-image-gen --computer-vision --image-gen --gpu --docker
```

### 🚀 One-Command Deploy

Every generated project includes a `deploy.py` and `deploy.sh` that supports **8 deployment platforms** out of the box:

```bash
# Deploy to any platform (interactive wizard if no platform specified)
ocd-ai deploy

# Direct deploy to a specific platform
ocd-ai deploy aws           # AWS ECS (Fargate)
ocd-ai deploy gcp           # Google Cloud Run
ocd-ai deploy azure         # Azure Container Apps
ocd-ai deploy digitalocean  # DigitalOcean App Platform
ocd-ai deploy railway       # Railway
ocd-ai deploy fly           # Fly.io
ocd-ai deploy render        # Render
ocd-ai deploy vps           # Any VPS via SSH + Docker

# Build & push Docker image before deploying
ocd-ai deploy aws --build --push
```

## 🎛️ CLI Flags

### Feature Flags

| Flag | Description |
|------|-------------|
| `--all` | Enable every feature, provider, vector store, database, and infrastructure option |
| `--llm-only` | Just LLM chat (no RAG, voice, vision, etc.) |
| `--rag` | RAG pipeline (ingestion, chunking, embedding, retrieval, generation) |
| `--voice` | Speech-to-Text + Text-to-Speech |
| `--voice-to-voice` | Voice conversation (implies `--voice` + `--streaming`) |
| `--vision` | Image/video analysis |
| `--emotion` | Emotion detection (audio + text) |
| `--search` | Web search with LLM summarization |
| `--agents` | ReAct-style AI agents with tool use |
| `--memory` | Short-term + long-term conversation memory |
| `--streaming` | SSE + WebSocket streaming |
| `--session` | Redis-backed session management |

### LLM Providers

| Flag | Provider |
|------|----------|
| `--openai` | OpenAI (GPT-4o, GPT-4, GPT-3.5) |
| `--anthropic` | Anthropic (Claude 3.5, Claude 3) |
| `--google` | Google (Gemini Pro, Gemini Flash) |
| `--groq` | Groq (Llama, Mixtral — ultra-fast inference) |
| `--grok` | xAI Grok |
| `--cohere` | Cohere (Command R+) |
| `--mistral` | Mistral AI (Mistral Large, Mixtral) |
| `--ollama` | Ollama (local models — Llama, Mistral, etc.) |
| `--all-providers` | Enable all providers |

### Vector Stores

| Flag | Store |
|------|-------|
| `--faiss` | Facebook AI Similarity Search (local, fast) |
| `--pinecone` | Pinecone (managed, scalable) |
| `--qdrant` | Qdrant (open-source, feature-rich) |
| `--weaviate` | Weaviate (hybrid search) |
| `--chroma` | ChromaDB (lightweight, embedded) |
| `--milvus` | Milvus (distributed, GPU-accelerated) |
| `--pgvector` | pgvector (PostgreSQL extension) |

### Databases

| Flag | Database |
|------|----------|
| `--postgres` | PostgreSQL (primary relational database) |
| `--mongodb` | MongoDB (document store) |
| `--redis` | Redis (caching, sessions, pub/sub) |
| `--all-databases` | Enable all databases |

### Infrastructure

| Flag | Description |
|------|-------------|
| `--docker` | Dockerfiles + docker-compose (dev & prod) + Nginx |
| `--ci-cd` | GitHub Actions workflows (test, lint, deploy) |
| `--iac` | Terraform (AWS) + Ansible server configuration |
| `--monitoring` | Prometheus + Grafana + alerting rules |

### ML / Training

| Flag | Description |
|------|-------------|
| `--ml-training` | Full ML training pipeline (trainer, predictor, data loader, model registry) |
| `--pytorch` | PyTorch models (MLP, CNN, LSTM, Transformer) |
| `--tensorflow` | TensorFlow/Keras models |
| `--sklearn` | scikit-learn pipelines (Random Forest, SVM, Gradient Boosting, auto-select) |
| `--xgboost` | XGBoost gradient boosting |
| `--lightgbm` | LightGBM gradient boosting |
| `--fine-tuning` | LLM fine-tuning with LoRA/QLoRA (PEFT + Transformers) |
| `--gpu` | Enable CUDA/GPU, mixed precision (FP16/BF16) |
| `--mlops` | MLflow + Weights & Biases experiment tracking |

### Computer Vision

| Flag | Description |
|------|-------------|
| `--computer-vision` | Computer vision module (inference, pre/post-processing) |
| `--yolo` | YOLOv8/v11 object detection (Ultralytics) |
| `--sam` | SAM2 image segmentation (Segment Anything) |
| `--ocr` | OCR text extraction (EasyOCR + Tesseract) |
| `--face-detection` | Face detection & recognition (face-recognition + MediaPipe) |
| `--image-gen` | Text-to-image generation (Stable Diffusion / Diffusers) |

### Edge AI

| Flag | Description |
|------|-------------|
| `--edge-ai` | Edge AI deployment module |
| `--onnx` | ONNX model conversion + ONNX Runtime inference |
| `--tensorrt` | TensorRT model optimization (NVIDIA) |
| `--quantization` | INT8 quantization (ONNX + HuggingFace Optimum) |

### Advanced Features

| Flag | Description |
|------|-------------|
| `--aggregator` | AI API aggregator pattern (multi-provider routing) |
| `--analytics` | Conversational analytics (Text-to-SQL + charts + reports) |
| `--guardrails` | AI safety (content filter, PII detection, prompt injection defense, audit) |
| `--multi-tenant` | Multi-tenant architecture support |
| `--ab-testing` | A/B testing framework for prompts/models |
| `--ollama-serve` | Local Ollama deployment in docker-compose |

## 📁 Generated Project Structure

```
my-ai-project/
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI application entry point
│   │   ├── config.py               # Pydantic settings & environment config
│   │   ├── dependencies.py         # Dependency injection
│   │   ├── exceptions.py           # Custom exception handlers
│   │   ├── api/v1/                 # API routes (versioned)
│   │   │   ├── health.py           # Health check endpoint
│   │   │   ├── chat.py             # LLM chat endpoint
│   │   │   ├── rag.py              # RAG query endpoint
│   │   │   ├── documents.py        # Document upload/management
│   │   │   ├── voice.py            # STT/TTS endpoints
│   │   │   ├── websocket.py        # WebSocket streaming
│   │   │   ├── vision.py           # Image/video analysis
│   │   │   ├── emotion.py          # Emotion detection
│   │   │   ├── search.py           # Web search
│   │   │   ├── agents.py           # AI agent endpoint
│   │   │   ├── sessions.py         # Session management
│   │   │   ├── ml.py               # ML training & prediction
│   │   │   ├── cv.py               # Computer vision endpoints
│   │   │   ├── edge.py             # Edge AI (convert, benchmark)
│   │   │   ├── analytics.py        # Text-to-SQL & charts
│   │   │   └── guardrails.py       # AI safety endpoints
│   │   ├── core/
│   │   │   ├── ai/                 # LLM clients + provider factory
│   │   │   │   ├── providers/      # OpenAI, Anthropic, Google, etc.
│   │   │   │   ├── llm_client.py   # Base LLM interface
│   │   │   │   └── embeddings.py   # Embedding generation
│   │   │   ├── rag/                # RAG pipeline
│   │   │   │   ├── ingestion.py    # Document ingestion
│   │   │   │   ├── chunking.py     # Smart text chunking
│   │   │   │   ├── retriever.py    # Vector retrieval
│   │   │   │   └── pipeline.py     # End-to-end RAG
│   │   │   ├── multimodal/         # Voice, vision, emotion
│   │   │   │   ├── stt.py          # Speech-to-Text
│   │   │   │   ├── tts.py          # Text-to-Speech
│   │   │   │   ├── vision.py       # Vision analysis
│   │   │   │   └── emotion.py      # Emotion detection
│   │   │   ├── agents/             # Agent framework
│   │   │   ├── memory/             # Memory management
│   │   │   └── search/             # Web search
│   │   ├── ml/                     # ML training pipeline
│   │   │   ├── trainer.py          # Unified trainer (PyTorch/sklearn/XGBoost)
│   │   │   ├── predictor.py        # Model inference
│   │   │   ├── data_loader.py      # Data loading & splitting
│   │   │   ├── feature_engineering.py # Feature scaling, encoding
│   │   │   ├── model_registry.py   # Model versioning & promotion
│   │   │   ├── evaluation.py       # Metrics (accuracy, F1, RMSE)
│   │   │   ├── experiment.py       # MLflow/W&B tracking
│   │   │   ├── pytorch_models.py   # MLP, CNN, LSTM, Transformer
│   │   │   ├── sklearn_models.py   # RF, SVM, GB, auto-select
│   │   │   ├── tf_models.py        # Keras models
│   │   │   └── fine_tuning.py      # LoRA/QLoRA fine-tuning
│   │   ├── cv/                     # Computer vision
│   │   │   ├── inference.py        # Unified CV pipeline
│   │   │   ├── preprocessing.py    # Resize, normalize, augment
│   │   │   ├── postprocessing.py   # NMS, drawing, formatting
│   │   │   ├── yolo_detector.py    # YOLOv8/v11 detection
│   │   │   ├── sam_segmenter.py    # SAM2 segmentation
│   │   │   ├── ocr_engine.py       # EasyOCR + Tesseract
│   │   │   ├── face_detector.py    # Face detection/recognition
│   │   │   └── image_generator.py  # Stable Diffusion generation
│   │   ├── edge/                   # Edge AI deployment
│   │   │   ├── converter.py        # PyTorch→ONNX→TensorRT
│   │   │   ├── optimizer.py        # Quantization, pruning
│   │   │   └── runtime.py          # ONNX Runtime inference
│   │   ├── analytics/              # Conversational analytics
│   │   │   ├── text_to_sql.py      # NL→SQL engine
│   │   │   ├── chart_gen.py        # Plotly chart generation
│   │   │   └── report.py           # HTML report builder
│   │   ├── guardrails/             # AI safety
│   │   │   ├── content_filter.py   # Toxicity detection (Detoxify)
│   │   │   ├── pii_detector.py     # PII detection (Presidio)
│   │   │   ├── prompt_injection.py # Injection defense
│   │   │   └── audit_logger.py     # Compliance audit trail
│   │   ├── services/               # Business logic layer
│   │   ├── models/                 # Pydantic schemas & enums
│   │   ├── db/                     # Database connections
│   │   └── utils/                  # Logger, security, helpers
│   ├── tests/                      # Test suite
│   ├── vector_stores/              # Vector store implementations
│   ├── middleware/                  # Error handling, rate limiting, logging
│   ├── Dockerfile                  # Production Dockerfile
│   ├── Dockerfile.dev              # Development Dockerfile
│   ├── .env                        # Environment variables
│   └── .env.example                # Environment template
├── docker-compose.dev.yml          # Development orchestration
├── docker-compose.prod.yml         # Production orchestration
├── nginx/
│   └── nginx.conf                  # Reverse proxy configuration
├── .github/
│   └── workflows/
│       ├── test.yml                # CI testing
│       ├── lint.yml                # Code linting
│       └── deploy.yml              # Deployment pipeline
├── infra/
│   ├── terraform/                  # AWS infrastructure
│   └── ansible/                    # Server configuration
├── monitoring/
│   ├── prometheus.yml              # Metrics collection
│   ├── alerts.yml                  # Alert rules
│   └── grafana_dashboard.json      # Pre-built dashboards
├── scripts/
│   ├── start.sh                    # Application launcher
│   └── health_check.py             # Health check script
├── models/                         # Trained model storage
│   ├── checkpoints/                # Training checkpoints
│   └── exported/                   # Production-ready models
├── datasets/                       # Training data
│   ├── raw/                        # Raw datasets
│   └── processed/                  # Processed features
├── experiments/                    # MLflow/W&B experiment logs
├── Makefile                        # Common commands
├── deploy.py                       # Cross-platform deploy script (Python)
├── deploy.sh                       # Deploy script (Bash)
├── .gitignore                      # Git ignore rules
└── DEVELOPMENT_GUIDE.md            # Getting started guide
```

### 🚀 Built for the Future (Extensibility)

This structure is intentionally designed for scaling into a full-stack or microservices architecture:

- **Full-Stack Ready:** Need a frontend? Add a `frontend/` folder (React, Next.js, Streamlit, Gradio) at the root.
- **Microservices Ready:** Plug in other services like `ml-training/`, `data-pipeline/`, or `notification-service/` alongside the backend.
- **Multi-Model Ready:** Each AI provider is isolated behind a factory pattern — adding a new provider is one file.
- **ML/CV Pipeline Ready:** Training, inference, and edge deployment modules are fully isolated and can scale independently.
- **Simplified Orchestration:** New services integrate into the root `docker-compose.yml` and CI/CD pipelines seamlessly.
- **Guardrails by Default:** Content safety, PII protection, and prompt injection defense can be applied to any endpoint.

## 🔧 Tech Stack

| Category | Technologies |
|----------|-------------|
| **Framework** | FastAPI ≥ 0.115 |
| **Runtime** | Python ≥ 3.11, uvicorn |
| **Package Manager** | uv |
| **Validation** | Pydantic v2, pydantic-settings |
| **LLM Providers** | OpenAI, Anthropic, Google, Groq, Grok, Cohere, Mistral, Ollama, DeepSeek, Meta |
| **Vector Stores** | FAISS, Pinecone, Qdrant, Weaviate, ChromaDB, Milvus, pgvector, LanceDB |
| **Voice** | Whisper, Deepgram, whisper-local (STT) · OpenAI TTS, ElevenLabs, Bark (TTS) |
| **Vision** | GPT-4.1, Claude Opus 4, Gemini 2.5 Pro Vision |
| **Emotion** | Hume AI, Affectiva, LLM-based fallback |
| **Search** | Tavily, Serper, DuckDuckGo |
| **ML Frameworks** | PyTorch, TensorFlow/Keras, scikit-learn, XGBoost, LightGBM |
| **Computer Vision** | YOLO (Ultralytics), SAM2, EasyOCR, Tesseract, face-recognition, MediaPipe, Diffusers |
| **Edge AI** | ONNX, ONNX Runtime, TensorRT, HuggingFace Optimum |
| **Fine-Tuning** | PEFT (LoRA/QLoRA), Transformers, TRL, bitsandbytes |
| **MLOps** | MLflow, Weights & Biases |
| **Guardrails** | Detoxify, Presidio (PII), custom prompt injection defense |
| **Analytics** | SQLAlchemy, sqlparse, Plotly |
| **Databases** | PostgreSQL, MongoDB, Redis |
| **Containers** | Docker + docker-compose + Nginx |
| **CI/CD** | GitHub Actions |
| **IaC** | Terraform (AWS) + Ansible |
| **Monitoring** | Prometheus + Grafana + Alertmanager |

## ⚙️ Configuration

On first run, `ocd-ai` will ask for your **GitHub username**, **DockerHub username**, **default LLM provider**, and **default vector store**. These are saved in `~/.config/one-click-ai/config.toml` so you never have to type them again.

You can reset your configuration at any time by editing or deleting the config file.

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/your-username/one-click-ai.git`
3. **Install dependencies:** `uv sync` or `pip install -e .`
4. **Create a branch:** `git checkout -b feature/my-feature`
5. **Make your changes** — add generators in `src/one_click_ai/generator.py` or new templates in `src/one_click_ai/templates/`
6. **Test locally:** `ocd-ai init test-project --all`
7. **Submit a Pull Request** 🎉

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 👨‍💻 Author

**Mohammad Asif Khan**

- GitHub: [@aktonay](https://github.com/aktonay)
- LinkedIn: [Mohammad Asif Khan](https://www.linkedin.com/in/mohammad-asif-khan-tonay-795b641b6)
- Website: [sparktech.agency](https://www.sparktech.agency/)

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ for the AI developer community
  <br>
  <a href="#top">Back to Top ⬆</a>
</p>
