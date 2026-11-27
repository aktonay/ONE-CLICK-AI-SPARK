# 🛠️ Development Helper Commands

## Clean previous builds
```bash
rm -rf dist build *.egg-info
```

## Build the package
```bash
uv build
```

## Install locally from wheel (for testing)
```bash
uv tool install dist/one_click_ai-3.0.0-py3-none-any.whl
```

## Test the CLI
```bash
ocd-ai --help
```

## Upload to PyPI
```bash
uv run twine upload dist/*
```

## Activate virtual environment
```bash
source .venv/bin/activate
```

## Install in editable mode (for development)
```bash
uv pip install -e .
```

## Test with a full project
```bash
ocd-ai init demo_project --all
```

## Test specific features
```bash
ocd-ai init test_rag --rag --openai --faiss --docker
ocd-ai init test_voice --voice --voice-to-voice --openai --streaming
ocd-ai init test_agent --agents --search --memory --openai
ocd-ai init test_vision --vision --emotion --openai --google
```

## Test v3.0 ML/CV/Edge features
```bash
ocd-ai init test_ml --ml-training --pytorch --sklearn --xgboost --mlops --docker
ocd-ai init test_cv --computer-vision --yolo --sam --ocr --face-detection --docker
ocd-ai init test_edge --edge-ai --onnx --tensorrt --quantization --docker
ocd-ai init test_analytics --analytics --openai --docker
ocd-ai init test_guardrails --guardrails --openai --docker
ocd-ai init test_finetune --fine-tuning --pytorch --gpu --mlops --docker
ocd-ai init test_image_gen --computer-vision --image-gen --gpu --docker
ocd-ai init test_full_v3 --all
```

## Test deploy command
```bash
# After generating a project with --all
cd test_full_v3
ocd-ai deploy          # interactive wizard
ocd-ai deploy railway  # direct deploy
```

## Run tests
```bash
uv run pytest
```

## Run tests with coverage
```bash
uv run pytest --cov=one_click_ai --cov-report=html
```

---

## Git Workflow

### Development
```bash
git checkout dev
# make changes
git add .
git commit -m "feat: your feature description"
git push
```

### Release
```bash
git checkout main
git merge dev
git tag v3.0.0
git push origin main --tags
```

### Fix a tag (if needed)
```bash
git tag -d v3.0.0
git push --delete origin v3.0.0
git tag v3.0.0
git push origin v3.0.0
```
