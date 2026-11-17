import typer
from rich.console import Console
from rich.table import Table
from one_click_ai.config import CONFIG_FILE, save_config, get_git_user, load_config

console = Console()

# ──────────────────────────────────────────────
# AI Provider / Vector-Store choices (2026 latest)
# ──────────────────────────────────────────────
LLM_PROVIDERS = [
    "openai", "anthropic", "google", "groq", "grok",
    "cohere", "mistral", "together", "replicate", "ollama",
    "deepseek", "meta",
]

VECTOR_STORES = [
    "faiss", "pinecone", "qdrant", "weaviate",
    "chroma", "milvus", "pgvector", "lancedb",
]

STT_PROVIDERS = ["openai", "google", "deepgram", "assemblyai", "azure", "whisper-local"]
TTS_PROVIDERS = ["elevenlabs", "openai", "google", "azure", "coqui", "bark"]
EMOTION_PROVIDERS = ["hume", "azure", "affectiva"]
VISION_PROVIDERS = ["openai", "google", "aws", "azure", "anthropic", "ultralytics"]
SEARCH_PROVIDERS = ["tavily", "serpapi", "brave", "perplexity", "duckduckgo"]

ML_FRAMEWORKS = ["pytorch", "tensorflow", "sklearn", "xgboost", "lightgbm", "jax"]
CV_FRAMEWORKS = ["yolo", "sam2", "mediapipe", "detectron2", "mmdetection"]
EDGE_RUNTIMES = ["onnx", "tensorrt", "openvino", "tflite", "coreml"]


def _pick_from_list(prompt_text: str, choices: list[str], default: str) -> str:
    """Prompt user to pick from a list, returning the chosen value."""
    display = ", ".join(choices)
    value = typer.prompt(
        f"{prompt_text} ({display})",
        default=default,
        show_default=True,
    )
    value = value.strip().lower()
    if value not in choices:
        console.print(f"[yellow]⚠  Unknown choice '{value}', using default '{default}'[/yellow]")
        return default
    return value


# ──────────────────────────────────────────────
# First-time global config
# ──────────────────────────────────────────────
def ensure_global_config() -> dict:
    """
    Ensures global configuration exists.
    If not, prompts the user (only once).
    """
    if CONFIG_FILE.exists():
        cfg = load_config().get("user", {})
        return cfg

    console.print("\n[bold blue]📝 First-time setup — creating global config...[/bold blue]")
    console.print("Press [bold]ENTER[/bold] to skip any field.\n", style="dim")

    default_github = get_git_user()
    github_user = typer.prompt("GitHub Username", default=default_github, show_default=True)
    docker_user = typer.prompt("DockerHub Username", default="", show_default=False)

    default_llm = _pick_from_list("Default LLM provider", LLM_PROVIDERS, "openai")
    default_vs = _pick_from_list("Default vector store", VECTOR_STORES, "faiss")

    save_config(github_user, docker_user, default_llm, default_vs)
    console.print(f"[green]✅ Configuration saved to {CONFIG_FILE}[/green]")

    return {
        "github_username": github_user,
        "dockerhub_username": docker_user,
        "default_llm_provider": default_llm,
        "default_vector_store": default_vs,
    }


# ──────────────────────────────────────────────
# Project information prompt
# ──────────────────────────────────────────────
def ask_project_info(default_name: str = "ai_project") -> dict:
    """Interactively ask for project-level information."""

    console.print()
    project_name = typer.prompt("Project Name", default=default_name)
    project_description = typer.prompt(
        "Short description",
        default=f"{project_name} — AI-powered application",
    )

    github_url = typer.prompt("GitHub Repository URL (optional)", default="", show_default=False)

    return {
        "project_name": project_name,
        "project_description": project_description,
        "github_url": github_url,
    }


# ──────────────────────────────────────────────
# Feature summary table
# ──────────────────────────────────────────────

def _ml_detail(ctx: dict) -> str:
    """Build detail string for ML frameworks."""
    parts = []
    if ctx.get("pytorch"): parts.append("PyTorch")
    if ctx.get("tensorflow"): parts.append("TensorFlow")
    if ctx.get("sklearn"): parts.append("scikit-learn")
    if ctx.get("xgboost"): parts.append("XGBoost")
    if ctx.get("lightgbm"): parts.append("LightGBM")
    return ", ".join(parts) if parts else "PyTorch"


def _cv_detail(ctx: dict) -> str:
    """Build detail string for CV frameworks."""
    parts = []
    if ctx.get("yolo"): parts.append("YOLO")
    if ctx.get("sam"): parts.append("SAM2")
    if ctx.get("ocr"): parts.append("OCR")
    if ctx.get("face_detection"): parts.append("Face Detection")
    if ctx.get("image_gen"): parts.append("Image Gen")
    return ", ".join(parts) if parts else "YOLO"


def _edge_detail(ctx: dict) -> str:
    """Build detail string for Edge AI runtimes."""
    parts = []
    if ctx.get("onnx"): parts.append("ONNX")
    if ctx.get("tensorrt"): parts.append("TensorRT")
    if ctx.get("quantization"): parts.append("INT8/FP16")
    return ", ".join(parts) if parts else "ONNX"


def show_feature_summary(context: dict):
    """Print a pretty table summarising what will be generated."""
    table = Table(title="🧠 AI Project — Feature Summary", show_lines=True)
    table.add_column("Category", style="bold cyan", width=20)
    table.add_column("Enabled", style="bold green", width=10)
    table.add_column("Details", style="dim", width=40)

    features = [
        ("LLM Chat/Completion", True, context.get("llm_provider", "openai")),
        ("RAG Pipeline", context.get("rag"), "Vector retrieval + reranking"),
        ("Voice (STT/TTS)", context.get("voice"), f"STT: {context.get('stt_provider','openai')} | TTS: {context.get('tts_provider','elevenlabs')}"),
        ("Voice-to-Voice", context.get("voice_to_voice"), "Real-time conversational AI"),
        ("Vision (Image/Video)", context.get("vision"), f"Provider: {context.get('vision_provider','openai')}"),
        ("Emotion Detection", context.get("emotion"), f"Provider: {context.get('emotion_provider','hume')}"),
        ("Web Search", context.get("search"), f"Provider: {context.get('search_provider','tavily')}"),
        ("AI Agents", context.get("agents"), "Tool-calling & orchestration"),
        ("Memory System", context.get("memory"), "Short-term + long-term memory"),
        ("Streaming / WS", context.get("streaming"), "WebSocket + SSE"),
        ("Session Management", context.get("session"), "Redis / PostgreSQL / MongoDB"),
        ("ML Training", context.get("ml_training"), _ml_detail(context)),
        ("Computer Vision", context.get("computer_vision"), _cv_detail(context)),
        ("Edge AI", context.get("edge_ai"), _edge_detail(context)),
        ("Fine-tuning", context.get("fine_tuning"), "LoRA / QLoRA / PEFT"),
        ("MLOps", context.get("mlops"), "MLflow + Weights & Biases"),
        ("API Aggregator", context.get("aggregator"), "Multi-provider fallback routing"),
        ("Analytics (Text2SQL)", context.get("analytics"), "Natural language → SQL"),
        ("Guardrails & Safety", context.get("guardrails"), "Content filter + PII + prompt injection"),
        ("Multi-tenancy", context.get("multi_tenant"), "Isolated data per tenant"),
        ("A/B Testing", context.get("ab_testing"), "Model & prompt experimentation"),
        ("Ollama Server", context.get("ollama_serve"), "Self-hosted LLM in Docker"),
        ("Docker", context.get("docker"), "Dockerfile + compose (dev/prod)"),
        ("CI/CD", context.get("ci_cd"), "GitHub Actions"),
        ("IaC", context.get("iac"), "Terraform + Ansible"),
        ("Monitoring", context.get("monitoring"), "Prometheus + Grafana + Sentry"),
    ]

    for name, enabled, detail in features:
        table.add_row(name, "✅" if enabled else "—", detail if enabled else "")

    console.print(table)
