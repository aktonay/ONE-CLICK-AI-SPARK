# API Reference

Complete command-line reference for One Click AI Spark.

## Table of Contents

- [Global Options](#global-options)
- [Commands](#commands)
- [Generate Command](#generate-command)
- [List Command](#list-command)
- [Config Command](#config-command)
- [Feature Flags](#feature-flags)
- [Provider Options](#provider-options)

---

## Global Options

Options available for all commands:

```bash
one-click-ai [GLOBAL OPTIONS] COMMAND [OPTIONS]
```

| Option | Description | Default |
|--------|-------------|---------|
| `--version` | Show version and exit | - |
| `--help` | Show help message | - |
| `--verbose` / `-v` | Enable verbose output | false |
| `--quiet` / `-q` | Suppress output | false |

**Examples:**
```bash
# Show version
one-click-ai --version

# Get help
one-click-ai --help

# Verbose mode
one-click-ai --verbose generate --name my-app
```

---

## Commands

### Available Commands

| Command | Description |
|---------|-------------|
| `generate` | Generate a new AI project |
| `list` | List available features and providers |
| `config` | Manage global configuration |
| `version` | Show version information |

---

## Generate Command

Generate a new AI-powered backend project.

### Syntax

```bash
one-click-ai generate [OPTIONS]
```

### Required Options

| Option | Description | Example |
|--------|-------------|---------|
| `--name NAME` | Project name | `--name my-chatbot` |
| `--output PATH` | Output directory | `--output ./my-chatbot` |

### Core Options

| Option | Description | Default | Example |
|--------|-------------|---------|---------|
| `--features FEATURES` | Comma-separated list of features | `llm` | `--features llm,rag,voice` |
| `--description TEXT` | Project description | Auto-generated | `--description "My AI app"` |
| `--github-url URL` | GitHub repository URL | None | `--github-url https://github.com/user/repo` |

### Provider Options

| Option | Description | Default | Choices |
|--------|-------------|---------|---------|
| `--llm-provider PROVIDER` | LLM provider | `openai` | openai, anthropic, google, groq, mistral, ollama |
| `--vector-store STORE` | Vector database | `faiss` | faiss, pinecone, qdrant, weaviate, chroma, milvus |
| `--stt-provider PROVIDER` | Speech-to-text | `openai` | openai, google, deepgram, assemblyai, azure |
| `--tts-provider PROVIDER` | Text-to-speech | `elevenlabs` | elevenlabs, openai, google, azure, coqui |
| `--vision-provider PROVIDER` | Vision AI | `openai` | openai, google, aws, azure, anthropic |
| `--emotion-provider PROVIDER` | Emotion detection | `hume` | hume, azure, affectiva |
| `--search-provider PROVIDER` | Web search | `tavily` | tavily, serpapi, brave, perplexity, duckduckgo |
| `--session-backend BACKEND` | Session storage | `redis` | redis, postgresql, mongodb |

### Framework Options

| Option | Description | Default | Choices |
|--------|-------------|---------|---------|
| `--ml-frameworks FRAMEWORKS` | ML frameworks (comma-separated) | `pytorch` | pytorch, tensorflow, sklearn, xgboost, lightgbm |
| `--cv-frameworks FRAMEWORKS` | Computer vision frameworks | `yolo` | yolo, sam, mediapipe, detectron2 |
| `--edge-runtimes RUNTIMES` | Edge AI runtimes | `onnx` | onnx, tensorrt, openvino, tflite |

### Infrastructure Options

| Option | Description | Default |
|--------|-------------|---------|
| `--docker` | Include Docker configuration | Auto (if any feature enabled) |
| `--ci-cd` | Include GitHub Actions CI/CD | false |
| `--iac` | Include Terraform/Ansible | false |
| `--monitoring` | Include Prometheus/Grafana | false |

### Examples

**Basic chatbot:**
```bash
one-click-ai generate \
  --name simple-bot \
  --features llm \
  --output ./simple-bot
```

**RAG-powered chatbot:**
```bash
one-click-ai generate \
  --name doc-bot \
  --features llm,rag \
  --vector-store pinecone \
  --llm-provider openai \
  --output ./doc-bot
```

**Voice assistant:**
```bash
one-click-ai generate \
  --name voice-assistant \
  --features llm,voice,voice_to_voice \
  --stt-provider openai \
  --tts-provider elevenlabs \
  --output ./voice-assistant
```

**Computer vision API:**
```bash
one-click-ai generate \
  --name vision-api \
  --features vision,computer_vision \
  --cv-frameworks yolo,sam,ocr \
  --vision-provider openai \
  --output ./vision-api
```

**Full-stack AI platform:**
```bash
one-click-ai generate \
  --name ai-platform \
  --features llm,rag,voice,vision,agents,memory,guardrails \
  --vector-store pinecone \
  --docker \
  --ci-cd \
  --monitoring \
  --output ./ai-platform
```

**Multi-modal agent:**
```bash
one-click-ai generate \
  --name multimodal-agent \
  --features llm,rag,voice,vision,agents,search \
  --llm-provider anthropic \
  --vector-store qdrant \
  --search-provider tavily \
  --output ./multimodal-agent
```

**Edge AI for mobile:**
```bash
one-click-ai generate \
  --name mobile-ai \
  --features ml_training,edge_ai,computer_vision \
  --ml-frameworks pytorch \
  --edge-runtimes onnx,tflite \
  --cv-frameworks yolo \
  --output ./mobile-ai
```

---

## List Command

Display available features and providers.

### Syntax

```bash
one-click-ai list [OPTIONS]
```

### Options

| Option | Description |
|--------|-------------|
| `--features` | List all feature flags |
| `--providers` | List all provider options |
| `--all` | Show everything (default) |

### Examples

```bash
# List everything
one-click-ai list

# Only features
one-click-ai list --features

# Only providers
one-click-ai list --providers
```

### Output Example

```
🧠 Available Features:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Core AI:
  llm              - Large Language Models (GPT, Claude, etc.)
  rag              - Retrieval Augmented Generation
  voice            - Speech-to-Text & Text-to-Speech
  voice_to_voice   - Real-time voice conversations
  vision           - Image & video analysis
  emotion          - Emotion detection
  search           - Web search integration
  agents           - AI agents with tool use
  memory           - Conversation memory

Multimodal:
  computer_vision  - Object detection, OCR, segmentation
  ml_training      - Train custom ML models
  edge_ai          - Edge deployment (mobile, IoT)

Infrastructure:
  docker           - Docker containerization
  ci_cd            - GitHub Actions CI/CD
  iac              - Terraform & Ansible
  monitoring       - Prometheus & Grafana

🔧 Available Providers:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LLM: openai, anthropic, google, groq, mistral, ollama
Vector Store: faiss, pinecone, qdrant, weaviate, chroma
Voice (STT): openai, google, deepgram, assemblyai
Voice (TTS): elevenlabs, openai, google, azure
Vision: openai, google, aws, azure, anthropic
Search: tavily, serpapi, brave, perplexity
```

---

## Config Command

Manage global configuration (stored in `~/.one-click-ai/config.yaml`).

### Syntax

```bash
one-click-ai config [SUBCOMMAND] [OPTIONS]
```

### Subcommands

| Subcommand | Description |
|------------|-------------|
| `show` | Display current configuration |
| `set` | Set a configuration value |
| `reset` | Reset to defaults |

### Examples

```bash
# Show current config
one-click-ai config show

# Set default LLM provider
one-click-ai config set llm_provider anthropic

# Set default vector store
one-click-ai config set vector_store qdrant

# Set GitHub username
one-click-ai config set github_username myusername

# Reset to defaults
one-click-ai config reset
```

### Configuration Options

| Key | Description | Default |
|-----|-------------|---------|
| `github_username` | Your GitHub username | Auto-detected from git |
| `dockerhub_username` | Your DockerHub username | None |
| `default_llm_provider` | Default LLM provider | `openai` |
| `default_vector_store` | Default vector store | `faiss` |

---

## Feature Flags

Complete list of feature flags for `--features` option.

### Core AI Features

| Flag | Description | Dependencies |
|------|-------------|--------------|
| `llm` | Large Language Models | - |
| `rag` | Retrieval Augmented Generation | `llm` |
| `voice` | Speech-to-Text & Text-to-Speech | - |
| `voice_to_voice` | Real-time voice conversations | `llm`, `voice` |
| `vision` | Image & video analysis | `llm` (optional) |
| `emotion` | Emotion detection | - |
| `search` | Web search integration | - |
| `agents` | AI agents with tool use | `llm` |
| `memory` | Conversation memory (short + long term) | - |

### Multimodal AI

| Flag | Description | Dependencies |
|------|-------------|--------------|
| `computer_vision` | Object detection, OCR, segmentation | - |
| `ml_training` | Train custom ML models | - |
| `edge_ai` | Edge deployment optimization | `ml_training` or `computer_vision` |
| `fine_tuning` | Fine-tune LLMs (LoRA, QLoRA) | `llm` |

### Advanced Features

| Flag | Description | Dependencies |
|------|-------------|--------------|
| `streaming` | WebSocket & SSE streaming | `llm` |
| `session` | Session management | - |
| `mlops` | MLflow & Weights & Biases | `ml_training` |
| `aggregator` | Multi-provider routing | `llm` |
| `analytics` | Text-to-SQL analytics | `llm` |
| `guardrails` | Content filtering & safety | `llm` |
| `multi_tenant` | Multi-tenancy support | - |
| `ab_testing` | A/B testing framework | `llm` |
| `ollama_serve` | Self-hosted LLM server | - |

### Infrastructure

| Flag | Description | Dependencies |
|------|-------------|--------------|
| `docker` | Docker containerization | - |
| `ci_cd` | GitHub Actions workflows | - |
| `iac` | Terraform & Ansible | - |
| `monitoring` | Prometheus, Grafana, Sentry | - |

---

## Provider Options

### LLM Providers

| Provider | Models | Notes |
|----------|--------|-------|
| `openai` | GPT-3.5, GPT-4, GPT-4 Turbo | Most popular, best quality |
| `anthropic` | Claude 3 (Opus, Sonnet, Haiku) | Long context (200K tokens) |
| `google` | Gemini Pro, Ultra | Multimodal, competitive pricing |
| `groq` | Llama 3, Mixtral | Ultra-fast inference (500 tokens/s) |
| `mistral` | Mistral Large, Small | Open-source friendly |
| `ollama` | Llama, Phi, Mistral | Self-hosted, free |
| `cohere` | Command, Command-R | Good for RAG |
| `together` | Various open-source | Competitive pricing |
| `deepseek` | DeepSeek-V2 | Coding focused |

### Vector Stores

| Store | Type | Best For | Cost |
|-------|------|----------|------|
| `faiss` | Local | < 1M vectors, development | Free |
| `pinecone` | Cloud | Production, scaling | $70/mo |
| `qdrant` | Self-hosted/Cloud | 1-10M vectors | Free (self) |
| `weaviate` | Self-hosted/Cloud | Graph + vector | Free (self) |
| `chroma` | Local | Development | Free |
| `milvus` | Self-hosted | Enterprise scale | Free |
| `pgvector` | PostgreSQL | Already using Postgres | DB cost |
| `lancedb` | Local/Cloud | Embeddings + metadata | Free (local) |

### Voice Providers

**Speech-to-Text (STT):**

| Provider | Languages | Real-time | Accuracy |
|----------|-----------|-----------|----------|
| `openai` | 50+ | ✅ Yes | ⭐⭐⭐⭐⭐ |
| `google` | 125+ | ✅ Yes | ⭐⭐⭐⭐ |
| `deepgram` | 36+ | ✅ Yes | ⭐⭐⭐⭐⭐ |
| `assemblyai` | English focus | ✅ Yes | ⭐⭐⭐⭐⭐ |
| `azure` | 100+ | ✅ Yes | ⭐⭐⭐⭐ |

**Text-to-Speech (TTS):**

| Provider | Voices | Quality | Real-time |
|----------|--------|---------|-----------|
| `elevenlabs` | 1000+ | ⭐⭐⭐⭐⭐ | ✅ Yes |
| `openai` | 6 | ⭐⭐⭐⭐ | ✅ Yes |
| `google` | 400+ | ⭐⭐⭐⭐ | ✅ Yes |
| `azure` | 400+ | ⭐⭐⭐⭐ | ✅ Yes |
| `coqui` | Unlimited | ⭐⭐⭐ | ✅ Yes (local) |

### Vision Providers

| Provider | Features | Cost |
|----------|----------|------|
| `openai` | GPT-4V, object detection | $0.01/image |
| `google` | Vision AI, OCR, face detection | $1.50/1K images |
| `aws` | Rekognition | $1/1K images |
| `azure` | Computer Vision, OCR | $1/1K images |
| `anthropic` | Claude 3 Vision | $3/1K images |
| `ultralytics` | YOLO (self-hosted) | Free |

### Search Providers

| Provider | Type | Cost |
|----------|------|------|
| `tavily` | AI-optimized search | $0.10/1K searches |
| `serpapi` | Google results | $50/5K searches |
| `brave` | Privacy-focused | $3/1K searches |
| `perplexity` | AI search | API access |
| `duckduckgo` | Free search | Free (limited) |

---

## Environment Variables

Generated projects use these environment variables (in `.env` file):

### Core Settings

```bash
# Application
APP_NAME=my-app
DEBUG=false
LOG_LEVEL=INFO
PORT=8000
HOST=0.0.0.0

# LLM
OPENAI_API_KEY=sk-...
LLM_MODEL=gpt-4
LLM_TEMPERATURE=0.7
MAX_TOKENS=2000

# RAG
PINECONE_API_KEY=...
PINECONE_ENVIRONMENT=us-east-1
EMBEDDING_MODEL=text-embedding-3-small
CHUNK_SIZE=1000
CHUNK_OVERLAP=200

# Voice
ELEVENLABS_API_KEY=...
DEEPGRAM_API_KEY=...
DEFAULT_VOICE=ElevenLabs

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/db
REDIS_URL=redis://localhost:6379

# Security
SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRATION=3600
```

---

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | General error |
| 2 | Invalid arguments |
| 3 | Project already exists |
| 4 | Template rendering error |
| 5 | File system error |

---

## Configuration File

Global configuration is stored in `~/.one-click-ai/config.yaml`:

```yaml
user:
  github_username: myusername
  dockerhub_username: dockeruser
  default_llm_provider: openai
  default_vector_store: faiss

templates:
  custom_path: /path/to/custom/templates

defaults:
  docker: true
  ci_cd: false
  monitoring: false
```

---

## Advanced Usage

### Custom Templates

Place custom templates in `~/.one-click-ai/templates/`:

```
~/.one-click-ai/
└── templates/
    └── my-feature/
        ├── __init__.py.jinja
        ├── service.py.jinja
        └── api.py.jinja
```

Use in generation:
```bash
one-click-ai generate \
  --name my-app \
  --features llm,my-feature \
  --output ./my-app
```

### Scripting

Use in scripts for automation:

```bash
#!/bin/bash

# Generate multiple projects
for project in chatbot doc-qa voice-assistant; do
  one-click-ai generate \
    --name "$project" \
    --features llm,rag \
    --output "./$project" \
    --quiet
done
```

### CI/CD Integration

```yaml
# .github/workflows/generate.yml
name: Generate Project

on:
  workflow_dispatch:
    inputs:
      project_name:
        description: 'Project name'
        required: true
      features:
        description: 'Features (comma-separated)'
        required: true
        default: 'llm,rag'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - name: Install One Click AI Spark
        run: pip install one-click-ai-spark
      
      - name: Generate project
        run: |
          one-click-ai generate \
            --name ${{ github.event.inputs.project_name }} \
            --features ${{ github.event.inputs.features }} \
            --output ./${{ github.event.inputs.project_name }}
      
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: ${{ github.event.inputs.project_name }}
          path: ./${{ github.event.inputs.project_name }}
```

---

## Next Steps

- **[Getting Started](getting-started.md)** - Basics and prerequisites
- **[Quick Start](quick-start.md)** - Build your first project
- **[Features](features.md)** - Detailed feature documentation
- **[Examples](examples.md)** - Real-world project examples

