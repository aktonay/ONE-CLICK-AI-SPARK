"""
one-click-ai · Generator Module
Renders Jinja2 templates and scaffolds the full project tree.
"""

from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from pathlib import Path
import os
import secrets
import shutil
import subprocess
from rich.console import Console

console = Console()

TEMPLATE_DIR = Path(__file__).parent / "templates"
jinja_env = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR)),
    keep_trailing_newline=True,
)


# ──────────────────────────────────────────────
# Utility helpers
# ──────────────────────────────────────────────
def render_to_file(template_name: str, context: dict, dest_path: Path):
    """Render a Jinja2 template and write the result to *dest_path*."""
    try:
        template = jinja_env.get_template(template_name)
        content = template.render(context=context, **context)
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_text(content, encoding="utf-8")
    except TemplateNotFound:
        console.print(f"[bold red]❌ Template missing: {template_name}[/bold red]")


def run_command(cmd: list, cwd: Path, description: str = ""):
    """Run a shell command silently."""
    try:
        env_copy = os.environ.copy()
        subprocess.run(
            cmd,
            cwd=cwd,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            env=env_copy,
        )
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]❌ Command failed: {description}[/bold red]")
        if e.stderr:
            console.print(e.stderr.decode().strip())
    except Exception as e:
        console.print(f"[bold red]❌ Execution failed: {e}[/bold red]")


def setup_uv(project_root: Path):
    """Check for uv, install if missing, initialise project, add deps."""
    if shutil.which("uv") is None:
        console.print("[yellow]uv is not installed. Installing uv…[/yellow]")
        if os.name == "nt":
            subprocess.run(
                ["powershell", "-ExecutionPolicy", "ByPass", "-c",
                 "irm https://astral.sh/uv/install.ps1 | iex"],
                check=True,
            )
        else:
            subprocess.run(
                "curl -LsSf https://astral.sh/uv/install.sh | sh",
                shell=True, check=True,
            )
        uv_bin = Path.home() / ".local" / "bin" / "uv"
        if uv_bin.exists():
            os.environ["PATH"] += os.pathsep + str(uv_bin.parent)

    console.print("Initializing uv project…")
    run_command(["uv", "init", "--no-workspace", "."], cwd=project_root, description="uv init")

    # Remove default files uv creates
    for f in ("main.py", "hello.py"):
        p = project_root / f
        if p.exists():
            p.unlink()


def install_deps(backend_root: Path, context: dict):
    """Add Python deps via uv depending on enabled features."""
    # ── Core (always) ──
    core = [
        "fastapi>=0.115.0",
        "uvicorn[standard]>=0.34.0",
        "pydantic>=2.10.0",
        "pydantic-settings>=2.7.0",
        "httpx>=0.28.0",
        "python-dotenv>=1.0.1",
        "python-multipart>=0.0.18",
        "pyyaml>=6.0.2",
        "click>=8.1.8",
        "python-jose[cryptography]>=3.3.0",
        "passlib[bcrypt]>=1.7.4",
        "python-json-logger>=3.2.0",
    ]

    # ── Databases ──
    if context.get("postgres"):
        core += ["psycopg2-binary>=2.9.10", "sqlalchemy>=2.0.37", "alembic>=1.14.0", "asyncpg>=0.30.0"]
    if context.get("mongodb"):
        core += ["motor>=3.7.0", "pymongo>=4.10.0"]
    if context.get("redis") or context.get("session"):
        core += ["redis>=5.2.0"]

    # ── LLM providers ──
    if context.get("openai") or context.get("llm_provider") == "openai":
        core.append("openai>=1.59.0")
    if context.get("anthropic") or context.get("llm_provider") == "anthropic":
        core.append("anthropic>=0.42.0")
    if context.get("google") or context.get("llm_provider") == "google":
        core.append("google-generativeai>=0.8.0")
    if context.get("groq") or context.get("llm_provider") == "groq":
        core.append("groq>=0.15.0")
    if context.get("cohere") or context.get("llm_provider") == "cohere":
        core.append("cohere>=5.13.0")
    if context.get("mistral") or context.get("llm_provider") == "mistral":
        core.append("mistralai>=1.3.0")

    # ── RAG extras ──
    if context.get("rag"):
        core += [
            "langchain>=0.3.0",
            "langchain-community>=0.3.0",
            "langchain-openai>=0.3.0",
            "tiktoken>=0.8.0",
            "sentence-transformers>=3.4.0",
            "pypdf>=5.1.0",
            "python-docx>=1.1.2",
            "beautifulsoup4>=4.12.3",
            "unstructured>=0.16.0",
        ]
        vs = context.get("vector_store", "faiss")
        if vs == "faiss" or context.get("faiss"):
            core.append("faiss-cpu>=1.9.0")
        if vs == "pinecone" or context.get("pinecone"):
            core.append("pinecone-client>=5.0.0")
        if vs == "qdrant" or context.get("qdrant"):
            core.append("qdrant-client>=1.13.0")
        if vs == "weaviate" or context.get("weaviate"):
            core.append("weaviate-client>=4.11.0")
        if vs == "chroma" or context.get("chroma"):
            core.append("chromadb>=0.6.0")
        if vs == "milvus" or context.get("milvus"):
            core.append("pymilvus>=2.5.0")
        if vs == "pgvector" or context.get("pgvector"):
            core.append("pgvector>=0.3.6")

    # ── Voice ──
    if context.get("voice"):
        core += ["pydub>=0.25.1", "soundfile>=0.13.0"]
        if context.get("stt_provider") in ("openai", None):
            pass  # openai already added
        if context.get("stt_provider") == "deepgram":
            core.append("deepgram-sdk>=3.9.0")
        if context.get("stt_provider") == "assemblyai":
            core.append("assemblyai>=0.36.0")
        if context.get("tts_provider") == "elevenlabs":
            core.append("elevenlabs>=1.16.0")

    # ── Voice-to-Voice ──
    if context.get("voice_to_voice"):
        core.append("websockets>=14.0")

    # ── Emotion ──
    if context.get("emotion"):
        if context.get("emotion_provider") in ("hume", None):
            core.append("hume>=0.7.0")

    # ── Vision ──
    if context.get("vision"):
        core += ["pillow>=11.0.0", "opencv-python-headless>=4.10.0"]

    # ── Search ──
    if context.get("search"):
        if context.get("search_provider") in ("tavily", None):
            core.append("tavily-python>=0.5.0")

    # ── Agents ──
    if context.get("agents"):
        core += ["langgraph>=0.2.0"]

    # ── Streaming / WebSocket ──
    if context.get("streaming"):
        core += ["sse-starlette>=2.2.0", "websockets>=14.0"]

    # ── Monitoring ──
    if context.get("monitoring"):
        core += ["prometheus-client>=0.21.0", "sentry-sdk[fastapi]>=2.19.0"]

    # ── ML Training / Deep Learning ──
    if context.get("pytorch"):
        core += ["torch>=2.5.0", "torchvision>=0.20.0", "torchaudio>=2.5.0"]
    if context.get("tensorflow"):
        core += ["tensorflow>=2.18.0", "keras>=3.7.0"]
    if context.get("sklearn"):
        core += ["scikit-learn>=1.6.0", "joblib>=1.4.0", "pandas>=2.2.0", "numpy>=2.0.0"]
    if context.get("xgboost"):
        core += ["xgboost>=2.1.0", "pandas>=2.2.0", "numpy>=2.0.0", "scikit-learn>=1.6.0"]
    if context.get("lightgbm"):
        core += ["lightgbm>=4.5.0", "pandas>=2.2.0", "numpy>=2.0.0", "scikit-learn>=1.6.0"]
    if context.get("fine_tuning"):
        core += ["peft>=0.14.0", "transformers>=4.47.0", "datasets>=3.2.0",
                 "accelerate>=1.2.0", "bitsandbytes>=0.45.0", "trl>=0.14.0"]
    if context.get("mlops"):
        core += ["mlflow>=2.19.0", "wandb>=0.19.0"]

    # ── Computer Vision ──
    if context.get("yolo"):
        core += ["ultralytics>=8.3.0"]
    if context.get("sam"):
        core += ["segment-anything-2>=0.1.0"]
    if context.get("ocr"):
        core += ["pytesseract>=0.3.13", "easyocr>=1.7.2"]
    if context.get("face_detection"):
        core += ["face-recognition>=1.3.0", "mediapipe>=0.10.0"]
    if context.get("image_gen"):
        core += ["diffusers>=0.31.0", "safetensors>=0.4.0"]
    if context.get("computer_vision") and not context.get("vision"):
        core += ["pillow>=11.0.0", "opencv-python-headless>=4.10.0"]

    # ── Edge AI ──
    if context.get("onnx"):
        core += ["onnx>=1.17.0", "onnxruntime>=1.20.0"]
    if context.get("quantization"):
        core += ["optimum>=1.23.0"]

    # ── Analytics (Text-to-SQL) ──
    if context.get("analytics"):
        core += ["sqlparse>=0.5.0", "tabulate>=0.9.0", "plotly>=5.24.0",
                 "pandas>=2.2.0", "sqlalchemy>=2.0.37"]

    # ── Guardrails / Safety ──
    if context.get("guardrails"):
        core += ["presidio-analyzer>=2.2.0", "presidio-anonymizer>=2.2.0",
                 "detoxify>=0.5.0"]

    # ── Aggregator ──
    if context.get("aggregator"):
        core += ["cachetools>=5.5.0"]

    # ── Multi-tenancy ──
    if context.get("multi_tenant"):
        core += ["sqlalchemy>=2.0.37"]

    # ── A/B Testing ──
    if context.get("ab_testing"):
        pass  # uses stdlib hashlib

    # ── Dev extras (always) ──
    dev = [
        "pytest>=8.3.0",
        "pytest-asyncio>=0.25.0",
        "pytest-cov>=6.0.0",
        "httpx>=0.28.0",
        "black>=25.0.0",
        "ruff>=0.9.0",
        "mypy>=1.14.0",
        "pre-commit>=4.0.0",
    ]

    # De-duplicate
    core = list(dict.fromkeys(core))
    dev = list(dict.fromkeys(dev))

    console.print("Installing core dependencies…")
    run_command(["uv", "add", "--no-workspace"] + core, cwd=backend_root, description="uv add core deps")

    console.print("Installing dev dependencies…")
    run_command(["uv", "add", "--no-workspace", "--group", "dev"] + dev, cwd=backend_root, description="uv add dev deps")


# ──────────────────────────────────────────────
# Git helpers
# ──────────────────────────────────────────────
def setup_git(project_root: Path, github_url: str):
    """Initialise git, commit, push to GitHub (if URL given)."""
    if not github_url:
        console.print("[yellow]GitHub setup skipped (no URL provided).[/yellow]")
        return

    console.print(f"Initializing Git repository and pushing to {github_url}…")

    ssh_url = github_url
    if "https://github.com/" in github_url:
        repo_path = github_url.replace("https://github.com/", "").rstrip("/")
        if repo_path.endswith(".git"):
            repo_path = repo_path[:-4]
        ssh_url = f"git@github.com:{repo_path}.git"

    run_command(["git", "init"], cwd=project_root, description="git init")

    if not (project_root / "README.md").exists():
        (project_root / "README.md").write_text(
            "# AI Project — Generated with one-click-ai\n"
        )

    run_command(["git", "add", "."], cwd=project_root, description="git add")
    run_command(["git", "commit", "-m", "initial project setup (one-click-ai)"], cwd=project_root, description="git commit")
    run_command(["git", "branch", "-M", "main"], cwd=project_root, description="git branch")

    try:
        subprocess.run(
            ["git", "remote", "remove", "origin"],
            cwd=project_root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    except Exception:
        pass

    run_command(["git", "remote", "add", "origin", ssh_url], cwd=project_root, description="git remote add")

    console.print(f"Pushing to {ssh_url}…")
    try:
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=project_root, check=True)
        console.print("[green]Code pushed to GitHub successfully![/green]")
    except subprocess.CalledProcessError:
        console.print("[bold red]❌ Failed to push to GitHub. Check SSH keys / permissions.[/bold red]")


# ══════════════════════════════════════════════
# GENERATOR ENTRY-POINTS  (called from cli.py)
# ══════════════════════════════════════════════

def generate_core(project_root: Path, context: dict):
    """Generate the core FastAPI AI project structure."""
    backend = project_root / "backend"
    backend.mkdir(exist_ok=True)

    setup_uv(backend)
    install_deps(backend, context)

    ctx = {
        **context,
        "secret_key": secrets.token_urlsafe(50),
    }

    # ── FastAPI application files ──
    core_map = {
        "fastapi/main.py.jinja":             backend / "app" / "main.py",
        "fastapi/__init__.py.jinja":          backend / "app" / "__init__.py",
        "fastapi/config.py.jinja":            backend / "app" / "config.py",
        "fastapi/dependencies.py.jinja":      backend / "app" / "dependencies.py",
        "fastapi/exceptions.py.jinja":        backend / "app" / "exceptions.py",

        # API routes
        "fastapi/api/__init__.py.jinja":      backend / "app" / "api" / "__init__.py",
        "fastapi/api/v1/__init__.py.jinja":   backend / "app" / "api" / "v1" / "__init__.py",
        "fastapi/api/v1/router.py.jinja":     backend / "app" / "api" / "v1" / "router.py",
        "fastapi/api/v1/health.py.jinja":     backend / "app" / "api" / "v1" / "health.py",
        "fastapi/api/v1/chat.py.jinja":       backend / "app" / "api" / "v1" / "chat.py",

        # Middleware
        "fastapi/api/middleware/__init__.py.jinja":       backend / "app" / "api" / "middleware" / "__init__.py",
        "fastapi/api/middleware/error_handler.py.jinja":  backend / "app" / "api" / "middleware" / "error_handler.py",
        "fastapi/api/middleware/rate_limit.py.jinja":     backend / "app" / "api" / "middleware" / "rate_limit.py",
        "fastapi/api/middleware/logging_mw.py.jinja":     backend / "app" / "api" / "middleware" / "logging_mw.py",

        # Core AI
        "fastapi/core/__init__.py.jinja":                 backend / "app" / "core" / "__init__.py",
        "fastapi/core/ai/__init__.py.jinja":              backend / "app" / "core" / "ai" / "__init__.py",
        "fastapi/core/ai/llm_client.py.jinja":            backend / "app" / "core" / "ai" / "llm_client.py",
        "fastapi/core/ai/embeddings.py.jinja":            backend / "app" / "core" / "ai" / "embeddings.py",
        "fastapi/core/ai/prompt_manager.py.jinja":        backend / "app" / "core" / "ai" / "prompt_manager.py",
        "fastapi/core/ai/providers/__init__.py.jinja":    backend / "app" / "core" / "ai" / "providers" / "__init__.py",
        "fastapi/core/ai/providers/openai_client.py.jinja":    backend / "app" / "core" / "ai" / "providers" / "openai_client.py",
        "fastapi/core/ai/providers/anthropic_client.py.jinja": backend / "app" / "core" / "ai" / "providers" / "anthropic_client.py",
        "fastapi/core/ai/providers/google_client.py.jinja":    backend / "app" / "core" / "ai" / "providers" / "google_client.py",
        "fastapi/core/ai/factory.py.jinja":               backend / "app" / "core" / "ai" / "factory.py",

        # Models / schemas
        "fastapi/models/__init__.py.jinja":   backend / "app" / "models" / "__init__.py",
        "fastapi/models/schemas.py.jinja":    backend / "app" / "models" / "schemas.py",
        "fastapi/models/enums.py.jinja":      backend / "app" / "models" / "enums.py",

        # Services
        "fastapi/services/__init__.py.jinja":       backend / "app" / "services" / "__init__.py",
        "fastapi/services/chat_service.py.jinja":   backend / "app" / "services" / "chat_service.py",

        # Database
        "fastapi/db/__init__.py.jinja":       backend / "app" / "db" / "__init__.py",
        "fastapi/db/session.py.jinja":        backend / "app" / "db" / "session.py",

        # Utils
        "fastapi/utils/__init__.py.jinja":    backend / "app" / "utils" / "__init__.py",
        "fastapi/utils/logger.py.jinja":      backend / "app" / "utils" / "logger.py",
        "fastapi/utils/security.py.jinja":    backend / "app" / "utils" / "security.py",

        # Tests
        "tests/conftest.py.jinja":            backend / "tests" / "conftest.py",
        "tests/__init__.py.jinja":            backend / "tests" / "__init__.py",
        "tests/test_health.py.jinja":         backend / "tests" / "test_health.py",

        # Root files
        "env/.env.jinja":         backend / ".env",
        "env/.env.example.jinja": backend / ".env.example",
        "env/.gitignore.jinja":   backend / ".gitignore",
        "docs/DEVELOPMENT_GUIDE.md.jinja": project_root / "DEVELOPMENT_GUIDE.md",
    }

    for tmpl, dest in core_map.items():
        render_to_file(tmpl, ctx, dest)

    # ── RAG module ──
    if context.get("rag"):
        rag_map = {
            "fastapi/core/rag/__init__.py.jinja":       backend / "app" / "core" / "rag" / "__init__.py",
            "fastapi/core/rag/config.py.jinja":         backend / "app" / "core" / "rag" / "config.py",
            "fastapi/core/rag/ingestion.py.jinja":      backend / "app" / "core" / "rag" / "ingestion.py",
            "fastapi/core/rag/chunking.py.jinja":       backend / "app" / "core" / "rag" / "chunking.py",
            "fastapi/core/rag/retriever.py.jinja":      backend / "app" / "core" / "rag" / "retriever.py",
            "fastapi/core/rag/reranker.py.jinja":       backend / "app" / "core" / "rag" / "reranker.py",
            "fastapi/core/rag/pipeline.py.jinja":       backend / "app" / "core" / "rag" / "pipeline.py",
            "fastapi/api/v1/rag.py.jinja":              backend / "app" / "api" / "v1" / "rag.py",
            "fastapi/api/v1/documents.py.jinja":        backend / "app" / "api" / "v1" / "documents.py",
            "fastapi/services/rag_service.py.jinja":    backend / "app" / "services" / "rag_service.py",
            "fastapi/vector_stores/__init__.py.jinja":  backend / "app" / "vector_stores" / "__init__.py",
            "fastapi/vector_stores/base.py.jinja":      backend / "app" / "vector_stores" / "base.py",
            "fastapi/vector_stores/faiss_store.py.jinja": backend / "app" / "vector_stores" / "faiss_store.py",
            "fastapi/vector_stores/factory.py.jinja":   backend / "app" / "vector_stores" / "factory.py",
        }
        for tmpl, dest in rag_map.items():
            render_to_file(tmpl, ctx, dest)

    # ── Voice module ──
    if context.get("voice"):
        voice_map = {
            "fastapi/core/multimodal/__init__.py.jinja":      backend / "app" / "core" / "multimodal" / "__init__.py",
            "fastapi/core/multimodal/stt.py.jinja":           backend / "app" / "core" / "multimodal" / "stt.py",
            "fastapi/core/multimodal/tts.py.jinja":           backend / "app" / "core" / "multimodal" / "tts.py",
            "fastapi/api/v1/voice.py.jinja":                  backend / "app" / "api" / "v1" / "voice.py",
            "fastapi/services/voice_service.py.jinja":        backend / "app" / "services" / "voice_service.py",
        }
        for tmpl, dest in voice_map.items():
            render_to_file(tmpl, ctx, dest)

    # ── Voice-to-Voice module ──
    if context.get("voice_to_voice"):
        v2v_map = {
            "fastapi/core/multimodal/voice_to_voice.py.jinja": backend / "app" / "core" / "multimodal" / "voice_to_voice.py",
            "fastapi/api/v1/websocket.py.jinja":               backend / "app" / "api" / "v1" / "websocket.py",
        }
        for tmpl, dest in v2v_map.items():
            render_to_file(tmpl, ctx, dest)

    # ── Vision module ──
    if context.get("vision"):
        vision_map = {
            "fastapi/core/multimodal/vision.py.jinja":   backend / "app" / "core" / "multimodal" / "vision.py",
            "fastapi/api/v1/vision.py.jinja":            backend / "app" / "api" / "v1" / "vision.py",
            "fastapi/services/vision_service.py.jinja":  backend / "app" / "services" / "vision_service.py",
        }
        for tmpl, dest in vision_map.items():
            render_to_file(tmpl, ctx, dest)

    # ── Emotion module ──
    if context.get("emotion"):
        emotion_map = {
            "fastapi/core/multimodal/emotion.py.jinja":      backend / "app" / "core" / "multimodal" / "emotion.py",
            "fastapi/api/v1/emotion.py.jinja":               backend / "app" / "api" / "v1" / "emotion.py",
            "fastapi/services/emotion_service.py.jinja":     backend / "app" / "services" / "emotion_service.py",
        }
        for tmpl, dest in emotion_map.items():
            render_to_file(tmpl, ctx, dest)

    # ── Search module ──
    if context.get("search"):
        search_map = {
            "fastapi/core/search/__init__.py.jinja":        backend / "app" / "core" / "search" / "__init__.py",
            "fastapi/core/search/web_search.py.jinja":      backend / "app" / "core" / "search" / "web_search.py",
            "fastapi/api/v1/search.py.jinja":               backend / "app" / "api" / "v1" / "search.py",
            "fastapi/services/search_service.py.jinja":     backend / "app" / "services" / "search_service.py",
        }
        for tmpl, dest in search_map.items():
            render_to_file(tmpl, ctx, dest)

    # ── Agents module ──
    if context.get("agents"):
        agents_map = {
            "fastapi/core/agents/__init__.py.jinja":         backend / "app" / "core" / "agents" / "__init__.py",
            "fastapi/core/agents/base_agent.py.jinja":       backend / "app" / "core" / "agents" / "base_agent.py",
            "fastapi/core/agents/tools.py.jinja":            backend / "app" / "core" / "agents" / "tools.py",
            "fastapi/api/v1/agents.py.jinja":                backend / "app" / "api" / "v1" / "agents.py",
            "fastapi/services/agent_service.py.jinja":       backend / "app" / "services" / "agent_service.py",
        }
        for tmpl, dest in agents_map.items():
            render_to_file(tmpl, ctx, dest)

    # ── Memory module ──
    if context.get("memory"):
        memory_map = {
            "fastapi/core/memory/__init__.py.jinja":        backend / "app" / "core" / "memory" / "__init__.py",
            "fastapi/core/memory/short_term.py.jinja":      backend / "app" / "core" / "memory" / "short_term.py",
            "fastapi/core/memory/long_term.py.jinja":       backend / "app" / "core" / "memory" / "long_term.py",
        }
        for tmpl, dest in memory_map.items():
            render_to_file(tmpl, ctx, dest)

    # ── Session module ──
    if context.get("session"):
        session_map = {
            "fastapi/services/session_service.py.jinja":  backend / "app" / "services" / "session_service.py",
            "fastapi/api/v1/sessions.py.jinja":           backend / "app" / "api" / "v1" / "sessions.py",
        }
        for tmpl, dest in session_map.items():
            render_to_file(tmpl, ctx, dest)

    # ── Data / storage directories ──
    for d in ("data/uploads", "data/processed", "data/embeddings", "data/temp",
              "storage/audio", "storage/images", "storage/videos", "storage/documents",
              "vector_indexes/faiss", "logs"):
        (project_root / d).mkdir(parents=True, exist_ok=True)
        gitkeep = project_root / d / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.touch()

    # ── Scripts ──
    scripts_map = {
        "scripts/start.sh.jinja": project_root / "scripts" / "start.sh",
        "scripts/health_check.py.jinja": project_root / "scripts" / "health_check.py",
    }
    for tmpl, dest in scripts_map.items():
        render_to_file(tmpl, ctx, dest)

    # ── Makefile ──
    render_to_file("makefile/Makefile.jinja", ctx, project_root / "Makefile")

    # ── Deploy scripts (always — one-command deploy!) ──
    render_to_file("deploy/deploy.sh.jinja", ctx, project_root / "deploy.sh")
    render_to_file("deploy/deploy.py.jinja", ctx, project_root / "deploy.py")
    # Make deploy.sh executable
    deploy_sh = project_root / "deploy.sh"
    if deploy_sh.exists():
        try:
            deploy_sh.chmod(0o755)
        except Exception:
            pass

    # ── Git setup ──
    setup_git(project_root, context.get("github_repository_url", ""))


def generate_docker(project_root: Path, context: dict):
    """Generate Docker files."""
    backend = project_root / "backend"
    ctx = {**context, "secret_key": secrets.token_urlsafe(50)}

    render_to_file("docker/Dockerfile.jinja",              ctx, backend / "Dockerfile")
    render_to_file("docker/Dockerfile.dev.jinja",          ctx, backend / "Dockerfile.dev")
    render_to_file("docker/.dockerignore.jinja",           ctx, backend / ".dockerignore")
    render_to_file("docker/entrypoint.sh.jinja",           ctx, backend / "entrypoint.sh")
    render_to_file("docker/docker-compose.dev.yml.jinja",  ctx, project_root / "docker-compose.dev.yml")
    render_to_file("docker/docker-compose.prod.yml.jinja", ctx, project_root / "docker-compose.prod.yml")
    render_to_file("docker/docker-helper.sh.jinja",        ctx, project_root / "docker-helper.sh")
    render_to_file("docker/nginx.conf.jinja",              ctx, project_root / "nginx" / "ai.conf")

    for f in (backend / "entrypoint.sh", project_root / "docker-helper.sh"):
        if f.exists():
            try:
                f.chmod(0o755)
            except Exception:
                pass


def generate_cicd(project_root: Path, context: dict):
    """Generate CI/CD workflows."""
    ctx = {**context}
    render_to_file("github/test.yml.jinja",     ctx, project_root / ".github" / "workflows" / "test.yml")
    render_to_file("github/deploy.yml.jinja",   ctx, project_root / ".github" / "workflows" / "deploy.yml")
    render_to_file("github/lint.yml.jinja",      ctx, project_root / ".github" / "workflows" / "lint.yml")


def generate_iac(project_root: Path, context: dict):
    """Generate Infrastructure-as-Code templates."""
    ctx = {**context}
    iac_map = {
        "iac/terraform/main.tf.jinja":              "infra/terraform/main.tf",
        "iac/terraform/variables.tf.jinja":         "infra/terraform/variables.tf",
        "iac/terraform/outputs.tf.jinja":           "infra/terraform/outputs.tf",
        "iac/terraform/provider.tf.jinja":          "infra/terraform/provider.tf",
        "iac/terraform/security_groups.tf.jinja":   "infra/terraform/security_groups.tf",
        "iac/terraform/create_infra.sh.jinja":      "infra/terraform/create_infra.sh",
        "iac/terraform/destroy_infra.sh.jinja":     "infra/terraform/destroy_infra.sh",
        "iac/ansible/playbook.yml.jinja":           "infra/ansible/playbook.yml",
        "iac/ansible/hosts.ini.jinja":              "infra/ansible/hosts.ini",
        "iac/ansible/configure_server.sh.jinja":    "infra/ansible/configure_server.sh",
    }
    for tmpl, dest in iac_map.items():
        render_to_file(tmpl, ctx, project_root / dest)

    # Make shell scripts executable
    for script in ("infra/terraform/create_infra.sh", "infra/terraform/destroy_infra.sh",
                   "infra/ansible/configure_server.sh"):
        p = project_root / script
        if p.exists():
            try:
                p.chmod(0o755)
            except Exception:
                pass


def generate_monitoring(project_root: Path, context: dict):
    """Generate monitoring / observability configs."""
    ctx = {**context}
    render_to_file("monitoring/prometheus.yml.jinja",      ctx, project_root / "monitoring" / "prometheus" / "prometheus.yml")
    render_to_file("monitoring/alerts.yml.jinja",          ctx, project_root / "monitoring" / "prometheus" / "alerts.yml")
    render_to_file("monitoring/grafana_dashboard.json.jinja", ctx, project_root / "monitoring" / "grafana" / "dashboards" / "ai_overview.json")


def generate_ml_training(project_root: Path, context: dict):
    """Generate ML training pipeline, model registry, experiment tracking."""
    backend = project_root / "backend"
    ctx = {**context}

    ml_map = {
        "fastapi/ml/__init__.py.jinja":          backend / "app" / "ml" / "__init__.py",
        "fastapi/ml/config.py.jinja":            backend / "app" / "ml" / "config.py",
        "fastapi/ml/trainer.py.jinja":           backend / "app" / "ml" / "trainer.py",
        "fastapi/ml/predictor.py.jinja":         backend / "app" / "ml" / "predictor.py",
        "fastapi/ml/data_loader.py.jinja":       backend / "app" / "ml" / "data_loader.py",
        "fastapi/ml/feature_engineering.py.jinja": backend / "app" / "ml" / "feature_engineering.py",
        "fastapi/ml/model_registry.py.jinja":    backend / "app" / "ml" / "model_registry.py",
        "fastapi/ml/evaluation.py.jinja":        backend / "app" / "ml" / "evaluation.py",
        "fastapi/ml/experiment.py.jinja":        backend / "app" / "ml" / "experiment.py",
        "fastapi/api/v1/ml.py.jinja":           backend / "app" / "api" / "v1" / "ml.py",
        "fastapi/services/ml_service.py.jinja":  backend / "app" / "services" / "ml_service.py",
    }

    # Conditionally add framework-specific templates
    if context.get("pytorch"):
        ml_map["fastapi/ml/pytorch_models.py.jinja"] = backend / "app" / "ml" / "pytorch_models.py"
    if context.get("tensorflow"):
        ml_map["fastapi/ml/tf_models.py.jinja"] = backend / "app" / "ml" / "tf_models.py"
    if context.get("sklearn"):
        ml_map["fastapi/ml/sklearn_models.py.jinja"] = backend / "app" / "ml" / "sklearn_models.py"
    if context.get("fine_tuning"):
        ml_map["fastapi/ml/fine_tuning.py.jinja"] = backend / "app" / "ml" / "fine_tuning.py"

    for tmpl, dest in ml_map.items():
        render_to_file(tmpl, ctx, dest)

    # Create ML data directories
    for d in ("models/checkpoints", "models/exported", "datasets/raw", "datasets/processed",
              "experiments/logs", "experiments/runs"):
        (project_root / d).mkdir(parents=True, exist_ok=True)
        (project_root / d / ".gitkeep").touch()


def generate_computer_vision(project_root: Path, context: dict):
    """Generate computer vision modules."""
    backend = project_root / "backend"
    ctx = {**context}

    cv_map = {
        "fastapi/cv/__init__.py.jinja":          backend / "app" / "cv" / "__init__.py",
        "fastapi/cv/inference.py.jinja":         backend / "app" / "cv" / "inference.py",
        "fastapi/cv/preprocessing.py.jinja":     backend / "app" / "cv" / "preprocessing.py",
        "fastapi/cv/postprocessing.py.jinja":    backend / "app" / "cv" / "postprocessing.py",
        "fastapi/api/v1/cv.py.jinja":           backend / "app" / "api" / "v1" / "cv.py",
        "fastapi/services/cv_service.py.jinja":  backend / "app" / "services" / "cv_service.py",
    }

    if context.get("yolo"):
        cv_map["fastapi/cv/yolo_detector.py.jinja"] = backend / "app" / "cv" / "yolo_detector.py"
    if context.get("sam"):
        cv_map["fastapi/cv/sam_segmenter.py.jinja"] = backend / "app" / "cv" / "sam_segmenter.py"
    if context.get("ocr"):
        cv_map["fastapi/cv/ocr_engine.py.jinja"] = backend / "app" / "cv" / "ocr_engine.py"
    if context.get("face_detection"):
        cv_map["fastapi/cv/face_detector.py.jinja"] = backend / "app" / "cv" / "face_detector.py"
    if context.get("image_gen"):
        cv_map["fastapi/cv/image_generator.py.jinja"] = backend / "app" / "cv" / "image_generator.py"

    for tmpl, dest in cv_map.items():
        render_to_file(tmpl, ctx, dest)


def generate_edge_ai(project_root: Path, context: dict):
    """Generate edge AI deployment configs."""
    backend = project_root / "backend"
    ctx = {**context}

    edge_map = {
        "fastapi/edge/__init__.py.jinja":        backend / "app" / "edge" / "__init__.py",
        "fastapi/edge/converter.py.jinja":       backend / "app" / "edge" / "converter.py",
        "fastapi/edge/optimizer.py.jinja":       backend / "app" / "edge" / "optimizer.py",
        "fastapi/edge/runtime.py.jinja":         backend / "app" / "edge" / "runtime.py",
        "fastapi/api/v1/edge.py.jinja":         backend / "app" / "api" / "v1" / "edge.py",
        "fastapi/services/edge_service.py.jinja": backend / "app" / "services" / "edge_service.py",
    }

    for tmpl, dest in edge_map.items():
        render_to_file(tmpl, ctx, dest)


def generate_analytics(project_root: Path, context: dict):
    """Generate conversational analytics / Text-to-SQL modules."""
    backend = project_root / "backend"
    ctx = {**context}

    analytics_map = {
        "fastapi/analytics/__init__.py.jinja":       backend / "app" / "analytics" / "__init__.py",
        "fastapi/analytics/text_to_sql.py.jinja":    backend / "app" / "analytics" / "text_to_sql.py",
        "fastapi/analytics/chart_gen.py.jinja":      backend / "app" / "analytics" / "chart_gen.py",
        "fastapi/analytics/report.py.jinja":         backend / "app" / "analytics" / "report.py",
        "fastapi/api/v1/analytics.py.jinja":        backend / "app" / "api" / "v1" / "analytics.py",
        "fastapi/services/analytics_service.py.jinja": backend / "app" / "services" / "analytics_service.py",
    }

    for tmpl, dest in analytics_map.items():
        render_to_file(tmpl, ctx, dest)


def generate_guardrails(project_root: Path, context: dict):
    """Generate AI safety guardrails modules."""
    backend = project_root / "backend"
    ctx = {**context}

    guard_map = {
        "fastapi/guardrails/__init__.py.jinja":           backend / "app" / "guardrails" / "__init__.py",
        "fastapi/guardrails/content_filter.py.jinja":     backend / "app" / "guardrails" / "content_filter.py",
        "fastapi/guardrails/pii_detector.py.jinja":       backend / "app" / "guardrails" / "pii_detector.py",
        "fastapi/guardrails/prompt_injection.py.jinja":   backend / "app" / "guardrails" / "prompt_injection.py",
        "fastapi/guardrails/audit_logger.py.jinja":       backend / "app" / "guardrails" / "audit_logger.py",
        "fastapi/api/v1/guardrails.py.jinja":            backend / "app" / "api" / "v1" / "guardrails.py",
        "fastapi/services/guardrails_service.py.jinja":   backend / "app" / "services" / "guardrails_service.py",
    }

    for tmpl, dest in guard_map.items():
        render_to_file(tmpl, ctx, dest)
