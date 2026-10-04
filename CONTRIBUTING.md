# 🤝 Contributing to One Click AI

Thank you for your interest in contributing to **One Click AI**! We welcome contributions from the community.

## 🚀 Getting Started

### 1. Fork & Clone

```bash
git clone https://github.com/your-username/one-click-ai.git
cd one-click-ai
```

### 2. Set Up Development Environment

```bash
# Install uv if you haven't
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Install in editable mode
uv pip install -e .

# Verify it works
ocd-ai --help
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

## 📁 Project Structure

```
one-click-ai/
├── src/one_click_ai/
│   ├── __init__.py       # Package version
│   ├── cli.py            # Typer CLI commands & flags
│   ├── config.py         # TOML configuration management
│   ├── prompts.py        # Interactive prompts (Rich)
│   ├── generator.py      # Project generation logic
│   └── templates/        # Jinja2 templates
│       ├── fastapi/      # FastAPI application templates
│       ├── docker/       # Docker & compose templates
│       ├── env/          # Environment file templates
│       ├── github/       # CI/CD workflow templates
│       ├── iac/          # Terraform & Ansible templates
│       ├── monitoring/   # Prometheus & Grafana templates
│       ├── deploy/       # Deploy script templates
│       ├── tests/        # Test templates
│       ├── scripts/      # Utility script templates
│       ├── docs/         # Documentation templates
│       └── makefile/     # Makefile template
├── pyproject.toml        # Package metadata & dependencies
├── README.md             # Project documentation
└── LICENSE               # MIT license
```

## 🔧 How to Contribute

### Adding a New Template

1. Create your `.jinja` template file in the appropriate `templates/` subdirectory
2. Add the rendering logic in `generator.py`
3. If needed, add new CLI flags in `cli.py`
4. Update the feature summary in `prompts.py`
5. Test with: `ocd-ai init test-project --your-flag`

### Adding a New LLM Provider

1. Add the provider template in `templates/fastapi/core/ai/providers/`
2. Add the provider option in `prompts.py` (the provider choice list)
3. Add the CLI flag in `cli.py`
4. Update the factory template to include the new provider
5. Update `README.md` with the new provider

### Adding a New Vector Store

1. Add the store template in `templates/fastapi/vector_stores/`
2. Add the store option in `prompts.py`
3. Add the CLI flag in `cli.py`
4. Update the factory template
5. Update `README.md`

### Fixing Bugs

1. Identify the issue and create a minimal reproduction
2. Write a fix
3. Test with: `ocd-ai init test-fix --all`
4. Submit a PR with a clear description

## 📝 Code Style

- Use **type hints** throughout
- Follow **PEP 8** conventions
- Use **Rich** for console output (no raw `print()`)
- Use **Typer** for CLI arguments
- Keep Jinja2 templates clean and well-commented

## 🧪 Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=one_click_ai --cov-report=html

# Test a specific feature
ocd-ai init test-project --rag --openai --faiss --docker
```

## 📋 Pull Request Checklist

- [ ] Code follows existing patterns and style
- [ ] Templates render correctly (`ocd-ai init test --all`)
- [ ] README updated (if adding features)
- [ ] No broken imports or missing templates
- [ ] Commit messages are clear and descriptive

## 🐛 Reporting Issues

When reporting issues, please include:

1. **OS and Python version**
2. **Command you ran** (e.g., `ocd-ai init myproject --rag --openai`)
3. **Full error output**
4. **Expected behavior**

## 💡 Feature Requests

We'd love to hear your ideas! Open an issue with the `enhancement` label and describe:

1. **What** you'd like to see
2. **Why** it would be useful
3. **How** you envision it working

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for making One Click AI better! 🚀
