"""
one-click-ai · CLI  — ULTIMATE EDITION v3.0
Usage:
    ocd-ai init <project> [FLAGS]
    ocd-ai version
"""

import typer
import os
from pathlib import Path
from rich.console import Console

from one_click_ai.prompts import (
    ask_project_info,
    ensure_global_config,
    show_feature_summary,
)
from one_click_ai.generator import (
    generate_core,
    generate_docker,
    generate_cicd,
    generate_iac,
    generate_monitoring,
    generate_ml_training,
    generate_computer_vision,
    generate_edge_ai,
    generate_analytics,
    generate_guardrails,
)

help_text = """
🧠 One-Click AI v3.0 — Generate a production-ready AI/ML backend in seconds.

Supports: LLM (GPT-4.1, Claude Opus 4, Gemini 2.5, etc.), RAG, Voice,
Vision, Emotion, Agents, ML Training (PyTorch, TensorFlow, scikit-learn,
XGBoost), Computer Vision (YOLO, SAM2), Edge AI (ONNX, TensorRT),
Analytics, Guardrails, Docker, CI/CD, IaC, Monitoring & more.

Made with ❤️  by Mohammad Asif Khan
GitHub: https://github.com/aktonay

Usage:
    ocd-ai init [PATH] [OPTIONS]

Examples:
    ocd-ai init myproject --all
    ocd-ai init myproject --rag --voice --docker
    ocd-ai init myproject --ml-training --pytorch --gpu --docker
    ocd-ai init myproject --computer-vision --yolo --docker
    ocd-ai init . --llm-only --docker
"""

app = typer.Typer(help=help_text, add_completion=False)
console = Console()


@app.command()
def init(
    # ── Path ──
    path: Path = typer.Argument(
        None, help="Project name or path. Use '.' for current directory.", show_default=False
    ),

    # ── Meta flags ──
    all_features: bool = typer.Option(False, "--all", help="Enable ALL features"),
    llm_only: bool = typer.Option(False, "--llm-only", help="Pure LLM project (chat + completion only)"),

    # ── AI feature flags ──
    rag: bool = typer.Option(False, "--rag", help="RAG pipeline (vector retrieval + reranking)"),
    voice: bool = typer.Option(False, "--voice", help="Speech-to-Text & Text-to-Speech"),
    voice_to_voice: bool = typer.Option(False, "--voice-to-voice", help="Real-time voice conversation (Hume / OpenAI Realtime)"),
    vision: bool = typer.Option(False, "--vision", help="Image & video analysis"),
    emotion: bool = typer.Option(False, "--emotion", help="Emotion detection from voice/text"),
    search: bool = typer.Option(False, "--search", help="Web search integration (Tavily, SerpAPI, …)"),
    agents: bool = typer.Option(False, "--agents", help="AI agents with tool calling"),
    memory: bool = typer.Option(False, "--memory", help="Short-term & long-term memory systems"),
    streaming: bool = typer.Option(False, "--streaming", help="Real-time streaming (WebSocket + SSE)"),
    session: bool = typer.Option(False, "--session", help="Session management (Redis/Postgres/Mongo)"),

    # ── LLM provider flags ──
    openai: bool = typer.Option(True, "--openai/--no-openai", help="OpenAI provider"),
    anthropic: bool = typer.Option(False, "--anthropic", help="Anthropic Claude provider"),
    google: bool = typer.Option(False, "--google", help="Google Gemini provider"),
    groq: bool = typer.Option(False, "--groq", help="Groq provider"),
    grok: bool = typer.Option(False, "--grok", help="xAI Grok provider"),
    cohere: bool = typer.Option(False, "--cohere", help="Cohere provider"),
    mistral: bool = typer.Option(False, "--mistral", help="Mistral AI provider"),
    ollama: bool = typer.Option(False, "--ollama", help="Ollama (local models)"),
    all_providers: bool = typer.Option(False, "--all-providers", help="Enable ALL LLM providers"),

    # ── Vector store flags ──
    faiss: bool = typer.Option(False, "--faiss", help="FAISS vector store (default for RAG)"),
    pinecone: bool = typer.Option(False, "--pinecone", help="Pinecone vector store"),
    qdrant: bool = typer.Option(False, "--qdrant", help="Qdrant vector store"),
    weaviate: bool = typer.Option(False, "--weaviate", help="Weaviate vector store"),
    chroma: bool = typer.Option(False, "--chroma", help="ChromaDB vector store"),
    milvus: bool = typer.Option(False, "--milvus", help="Milvus vector store"),
    pgvector: bool = typer.Option(False, "--pgvector", help="pgvector (PostgreSQL extension)"),

    # ── Database flags ──
    postgres: bool = typer.Option(False, "--postgres", help="PostgreSQL"),
    mongodb: bool = typer.Option(False, "--mongodb", help="MongoDB"),
    redis: bool = typer.Option(False, "--redis", help="Redis"),
    all_databases: bool = typer.Option(False, "--all-databases", help="All databases"),

    # ── Infra flags ──
    docker: bool = typer.Option(False, "--docker", help="Docker + docker-compose"),
    ci_cd: bool = typer.Option(False, "--ci-cd", help="GitHub Actions CI/CD"),
    iac: bool = typer.Option(False, "--iac", help="Terraform + Ansible"),
    monitoring: bool = typer.Option(False, "--monitoring", help="Prometheus + Grafana + Sentry"),

    # ── ML / Training flags ──
    ml_training: bool = typer.Option(False, "--ml-training", help="ML model training pipeline"),
    pytorch: bool = typer.Option(False, "--pytorch", help="PyTorch deep learning"),
    tensorflow: bool = typer.Option(False, "--tensorflow", help="TensorFlow / Keras"),
    sklearn: bool = typer.Option(False, "--sklearn", help="scikit-learn (classical ML)"),
    xgboost: bool = typer.Option(False, "--xgboost", help="XGBoost gradient boosting"),
    lightgbm: bool = typer.Option(False, "--lightgbm", help="LightGBM gradient boosting"),
    fine_tuning: bool = typer.Option(False, "--fine-tuning", help="LLM fine-tuning (LoRA, QLoRA)"),
    gpu: bool = typer.Option(False, "--gpu", help="GPU support (CUDA / cuDNN)"),
    mlops: bool = typer.Option(False, "--mlops", help="MLOps (MLflow, W&B experiment tracking)"),

    # ── Computer Vision flags ──
    computer_vision: bool = typer.Option(False, "--computer-vision", help="Computer vision pipeline"),
    yolo: bool = typer.Option(False, "--yolo", help="YOLO object detection (Ultralytics)"),
    sam: bool = typer.Option(False, "--sam", help="Segment Anything Model 2 (SAM2)"),
    ocr: bool = typer.Option(False, "--ocr", help="OCR (Tesseract + EasyOCR + PaddleOCR)"),
    face_detection: bool = typer.Option(False, "--face-detection", help="Face detection & recognition"),
    image_gen: bool = typer.Option(False, "--image-gen", help="Image generation (DALL-E, Stable Diffusion)"),

    # ── Edge AI flags ──
    edge_ai: bool = typer.Option(False, "--edge-ai", help="Edge AI deployment"),
    onnx: bool = typer.Option(False, "--onnx", help="ONNX model conversion & runtime"),
    tensorrt: bool = typer.Option(False, "--tensorrt", help="NVIDIA TensorRT optimization"),
    quantization: bool = typer.Option(False, "--quantization", help="Model quantization (INT8, FP16)"),

    # ── Advanced project types ──
    aggregator: bool = typer.Option(False, "--aggregator", help="AI API aggregator with fallback routing"),
    analytics: bool = typer.Option(False, "--analytics", help="Conversational data analytics (Text-to-SQL)"),
    guardrails: bool = typer.Option(False, "--guardrails", help="AI safety: content filter, PII, prompt injection"),
    multi_tenant: bool = typer.Option(False, "--multi-tenant", help="Multi-tenancy support"),
    ab_testing: bool = typer.Option(False, "--ab-testing", help="A/B testing for models & prompts"),

    # ── Ollama local deployment ──
    ollama_serve: bool = typer.Option(False, "--ollama-serve", help="Include Ollama server in docker-compose"),
):
    """
    🧠 Initialize a new production-ready AI project.
    """

    # ── --all → turn everything on ──
    if all_features:
        rag = voice = voice_to_voice = vision = emotion = True
        search = agents = memory = streaming = session = True
        docker = ci_cd = iac = monitoring = True
        all_providers = all_databases = True
        ml_training = pytorch = tensorflow = sklearn = xgboost = lightgbm = True
        fine_tuning = gpu = mlops = True
        computer_vision = yolo = sam = ocr = face_detection = image_gen = True
        edge_ai = onnx = quantization = True
        aggregator = analytics = guardrails = True
        multi_tenant = ab_testing = True
        ollama_serve = True

    if all_providers:
        openai = anthropic = google = groq = grok = cohere = mistral = ollama = True

    if all_databases:
        postgres = mongodb = redis = True

    # If session is on, ensure at least redis
    if session and not (postgres or mongodb or redis):
        redis = True

    # If RAG is on and no vector store selected, default to faiss
    if rag and not any([faiss, pinecone, qdrant, weaviate, chroma, milvus, pgvector]):
        faiss = True

    # If voice_to_voice, imply voice + streaming + emotion
    if voice_to_voice:
        voice = True
        streaming = True

    # If ml_training, default to pytorch if no framework selected
    if ml_training and not any([pytorch, tensorflow, sklearn, xgboost, lightgbm]):
        pytorch = True

    # If computer_vision, default to yolo
    if computer_vision and not any([yolo, sam, ocr, face_detection, image_gen]):
        yolo = True

    # If edge_ai, default to onnx
    if edge_ai and not any([onnx, tensorrt, quantization]):
        onnx = True

    # If fine_tuning, ensure pytorch
    if fine_tuning:
        pytorch = True
        ml_training = True

    # If yolo/sam/ocr, ensure computer_vision
    if any([yolo, sam, ocr, face_detection, image_gen]):
        computer_vision = True

    # If pytorch/tensorflow/sklearn/xgboost/lightgbm, ensure ml_training
    if any([pytorch, tensorflow, sklearn, xgboost, lightgbm]):
        ml_training = True

    # If ollama_serve, ensure ollama provider
    if ollama_serve:
        ollama = True

    # ── Global config (first-time) ──
    global_config = ensure_global_config()

    # ── Project root ──
    if path is None:
        info = ask_project_info()
        project_name = info["project_name"]
        project_root = Path.cwd() / project_name
        if project_root.exists() and any(project_root.iterdir()):
            console.print(f"[bold red]❌ Directory '{project_name}' already exists and is not empty.[/bold red]")
            raise typer.Exit(code=1)
        project_root.mkdir(exist_ok=True)
    elif str(path) == ".":
        project_root = Path.cwd()
        info = ask_project_info(default_name=project_root.name)
        project_name = info["project_name"]
    else:
        project_root = path.resolve()
        project_root.mkdir(parents=True, exist_ok=True)
        console.print(f"[dim]Using target directory: {project_root}[/dim]")
        info = ask_project_info(default_name=path.name)
        project_name = info["project_name"]

    # ── Determine default vector store ──
    vector_store = "faiss"
    if pinecone: vector_store = "pinecone"
    elif qdrant: vector_store = "qdrant"
    elif weaviate: vector_store = "weaviate"
    elif chroma: vector_store = "chroma"
    elif milvus: vector_store = "milvus"
    elif pgvector: vector_store = "pgvector"

    # ── Determine default LLM provider ──
    llm_provider = global_config.get("default_llm_provider", "openai")
    if anthropic and not openai:
        llm_provider = "anthropic"
    elif google and not openai:
        llm_provider = "google"
    elif groq and not openai:
        llm_provider = "groq"

    # ── Build context ──
    context = {
        "project_name": project_name.replace(" ", "_").replace("-", "_"),
        "project_description": info.get("project_description", ""),
        "project_version": "0.1.0",

        "github_username": global_config.get("github_username", ""),
        "dockerhub_username": global_config.get("dockerhub_username", ""),
        "github_repository_url": info.get("github_url", ""),

        # Feature flags
        "llm_only": llm_only,
        "rag": rag,
        "voice": voice,
        "voice_to_voice": voice_to_voice,
        "vision": vision,
        "emotion": emotion,
        "search": search,
        "agents": agents,
        "memory": memory,
        "streaming": streaming,
        "session": session,

        # Providers
        "llm_provider": llm_provider,
        "openai": openai,
        "anthropic": anthropic,
        "google": google,
        "groq": groq,
        "grok": grok,
        "cohere": cohere,
        "mistral": mistral,
        "ollama": ollama,

        # Vector stores
        "vector_store": vector_store,
        "faiss": faiss,
        "pinecone": pinecone,
        "qdrant": qdrant,
        "weaviate": weaviate,
        "chroma": chroma,
        "milvus": milvus,
        "pgvector": pgvector,

        # Databases
        "postgres": postgres,
        "mongodb": mongodb,
        "redis": redis,

        # Sub-providers
        "stt_provider": "openai",
        "tts_provider": "elevenlabs",
        "emotion_provider": "hume",
        "vision_provider": "openai",
        "search_provider": "tavily",

        # ML / Training
        "ml_training": ml_training,
        "pytorch": pytorch,
        "tensorflow": tensorflow,
        "sklearn": sklearn,
        "xgboost": xgboost,
        "lightgbm": lightgbm,
        "fine_tuning": fine_tuning,
        "gpu": gpu,
        "mlops": mlops,

        # Computer Vision
        "computer_vision": computer_vision,
        "yolo": yolo,
        "sam": sam,
        "ocr": ocr,
        "face_detection": face_detection,
        "image_gen": image_gen,

        # Edge AI
        "edge_ai": edge_ai,
        "onnx": onnx,
        "tensorrt": tensorrt,
        "quantization": quantization,

        # Advanced project types
        "aggregator": aggregator,
        "analytics": analytics,
        "guardrails": guardrails,
        "multi_tenant": multi_tenant,
        "ab_testing": ab_testing,
        "ollama_serve": ollama_serve,

        # Infra
        "docker": docker,
        "ci_cd": ci_cd,
        "iac": iac,
        "monitoring": monitoring,
    }

    # ── Show summary ──
    show_feature_summary(context)

    console.print(f"\n[bold green]🚀 Initializing '{project_name}' in {project_root} …[/bold green]\n")

    # ── Generate Core (always) ──
    with console.status("[bold cyan]Generating FastAPI core & AI modules…[/bold cyan]"):
        generate_core(project_root, context)
    console.print("[green]✓ Core AI project generated[/green]")

    # ── Docker ──
    if docker:
        with console.status("Generating Docker files…"):
            generate_docker(project_root, context)
        console.print("[green]✓ Docker files generated[/green]")

    # ── CI/CD ──
    if ci_cd:
        with console.status("Generating CI/CD workflows…"):
            generate_cicd(project_root, context)
        console.print("[green]✓ CI/CD workflows generated[/green]")

    # ── IaC ──
    if iac:
        with console.status("Generating IaC templates…"):
            generate_iac(project_root, context)
        console.print("[green]✓ IaC templates generated[/green]")

    # ── Monitoring ──
    if monitoring:
        with console.status("Generating monitoring configs…"):
            generate_monitoring(project_root, context)
        console.print("[green]✓ Monitoring configs generated[/green]")

    # ── ML Training ──
    if ml_training:
        with console.status("Generating ML training pipeline…"):
            generate_ml_training(project_root, context)
        console.print("[green]✓ ML training pipeline generated[/green]")

    # ── Computer Vision ──
    if computer_vision:
        with console.status("Generating computer vision modules…"):
            generate_computer_vision(project_root, context)
        console.print("[green]✓ Computer vision modules generated[/green]")

    # ── Edge AI ──
    if edge_ai:
        with console.status("Generating edge AI deployment configs…"):
            generate_edge_ai(project_root, context)
        console.print("[green]✓ Edge AI configs generated[/green]")

    # ── Analytics ──
    if analytics:
        with console.status("Generating analytics modules…"):
            generate_analytics(project_root, context)
        console.print("[green]✓ Analytics modules generated[/green]")

    # ── Guardrails ──
    if guardrails:
        with console.status("Generating AI guardrails & safety modules…"):
            generate_guardrails(project_root, context)
        console.print("[green]✓ AI guardrails generated[/green]")

    # ── Done ──
    console.print("\n[bold green]✨ Project initialized successfully![/bold green]")
    console.print(f"\nNext steps:")
    if str(path) != ".":
        console.print(f"  cd {project_root.name if path is None else project_name}")

    console.print("\n[bold]Run Locally:[/bold]")
    console.print("  cd backend")
    console.print("  uv run uvicorn app.main:app --reload")

    if docker:
        console.print("\n[bold]Run with Docker:[/bold]")
        console.print("  docker compose -f docker-compose.dev.yml up --build")

    if ml_training:
        console.print("\n[bold]ML Training:[/bold]")
        console.print("  cd backend && python -m app.ml.train --config configs/train.yaml")

    if computer_vision:
        console.print("\n[bold]Computer Vision:[/bold]")
        console.print("  cd backend && python -m app.cv.inference --source image.jpg")

    console.print("\n[bold blue]API Docs:[/bold blue]")
    console.print("  Swagger: http://localhost:8000/docs")
    console.print("  ReDoc:   http://localhost:8000/redoc")

    console.print("\n[bold magenta]🚀 Deploy (ONE COMMAND!):[/bold magenta]")
    console.print("  ./deploy.sh                    [dim]# Interactive wizard — pick any platform[/dim]")
    console.print("  python deploy.py               [dim]# Cross-platform (Windows/Mac/Linux)[/dim]")
    console.print("  make deploy                    [dim]# Via Makefile[/dim]")
    console.print("\n[bold]Quick deploy targets:[/bold]")
    console.print("  ./deploy.sh railway            [dim]# Easiest — Railway[/dim]")
    console.print("  ./deploy.sh aws                [dim]# AWS (ECS / EC2 / App Runner)[/dim]")
    console.print("  ./deploy.sh azure              [dim]# Azure Container Apps[/dim]")
    console.print("  ./deploy.sh gcp                [dim]# GCP Cloud Run[/dim]")
    console.print("  ./deploy.sh do                 [dim]# DigitalOcean[/dim]")
    console.print("  ./deploy.sh fly                [dim]# Fly.io[/dim]")
    console.print("  ./deploy.sh server             [dim]# Your own server[/dim]")
    console.print("\n[dim]Git push only:  ./deploy.sh push[/dim]")
    console.print("[dim]Build image:    ./deploy.sh build[/dim]")


@app.command()
def version():
    """Show the installed version."""
    from one_click_ai import __version__
    typer.echo(f"one-click-ai v{__version__}")


@app.command()
def deploy(
    platform: str = typer.Argument(
        None,
        help="Target platform: aws, azure, gcp, do, railway, fly, render, server",
        show_default=False,
    ),
    push_only: bool = typer.Option(False, "--push", help="Only git push (no deploy)"),
    build_only: bool = typer.Option(False, "--build", help="Only build Docker image"),
):
    """
    🚀 Deploy your generated project to any cloud platform.

    Run from inside a project generated by 'ocd-ai init'.
    Without arguments, launches an interactive deploy wizard.
    """
    import subprocess as _sp
    import shutil as _sh

    cwd = Path.cwd()

    # Check we're in a generated project
    deploy_sh = cwd / "deploy.sh"
    deploy_py = cwd / "deploy.py"

    if not deploy_sh.exists() and not deploy_py.exists():
        console.print("[bold red]❌ No deploy.sh or deploy.py found in current directory.[/bold red]")
        console.print("[dim]Run this from inside a project generated by 'ocd-ai init'.[/dim]")
        raise typer.Exit(code=1)

    if push_only:
        cmd = "push"
    elif build_only:
        cmd = "build"
    elif platform:
        valid = {"aws", "azure", "gcp", "do", "railway", "fly", "render", "server"}
        if platform not in valid:
            console.print(f"[bold red]❌ Unknown platform: {platform}[/bold red]")
            console.print(f"[dim]Valid: {', '.join(sorted(valid))}[/dim]")
            raise typer.Exit(code=1)
        cmd = platform
    else:
        cmd = "deploy"

    # Prefer deploy.py (cross-platform), fall back to deploy.sh
    if deploy_py.exists():
        python = _sh.which("python3") or _sh.which("python") or "python"
        console.print(f"[bold cyan]🚀 Launching deploy wizard...[/bold cyan]\n")
        _sp.run([python, str(deploy_py), cmd], cwd=str(cwd))
    elif deploy_sh.exists():
        if os.name == "nt":
            bash = _sh.which("bash") or _sh.which("git-bash")
            if bash:
                _sp.run([bash, str(deploy_sh), cmd], cwd=str(cwd))
            else:
                console.print("[yellow]bash not found. Using deploy.py instead...[/yellow]")
                console.print("[dim]Install Git for Windows for bash support.[/dim]")
        else:
            _sp.run(["bash", str(deploy_sh), cmd], cwd=str(cwd))


if __name__ == "__main__":
    app()
