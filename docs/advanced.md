# Advanced Guide

Production deployment, scaling, optimization, and best practices for One Click AI Spark projects.

## Table of Contents

- [Production Deployment](#production-deployment)
- [Scaling & Performance](#scaling--performance)
- [Security & Compliance](#security--compliance)
- [Cost Optimization](#cost-optimization)
- [Monitoring & Observability](#monitoring--observability)
- [Custom Templates](#custom-templates)

---

## Production Deployment

### Docker Deployment

**Build and run:**
```bash
# Build production image
docker build -t my-ai-app:latest .

# Run with environment variables
docker run -d \
  -p 8000:8000 \
  --env-file .env \
  --name my-ai-app \
  my-ai-app:latest
```

**Docker Compose (recommended):**
```bash
# Production stack
docker-compose up -d

# Scale workers
docker-compose up -d --scale worker=4

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

---

### Cloud Deployment

#### AWS (Elastic Container Service)

**1. Push image to ECR:**
```bash
# Authenticate
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com

# Build and tag
docker build -t my-ai-app .
docker tag my-ai-app:latest YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/my-ai-app:latest

# Push
docker push YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/my-ai-app:latest
```

**2. Deploy with Terraform:**
```bash
cd iac/terraform
terraform init
terraform plan
terraform apply

# Outputs:
# - ALB URL: https://my-ai-app-123456.us-east-1.elb.amazonaws.com
# - CloudWatch logs: /ecs/my-ai-app
```

---

#### Google Cloud (Cloud Run)

```bash
# Build and deploy
gcloud builds submit --tag gcr.io/PROJECT_ID/my-ai-app
gcloud run deploy my-ai-app \
  --image gcr.io/PROJECT_ID/my-ai-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars OPENAI_API_KEY=sk-...
```

---

#### Kubernetes (K8s)

**deployment.yaml:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-ai-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-ai-app
  template:
    metadata:
      labels:
        app: my-ai-app
    spec:
      containers:
      - name: app
        image: my-ai-app:latest
        ports:
        - containerPort: 8000
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: api-keys
              key: openai
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "2Gi"
            cpu: "2000m"
---
apiVersion: v1
kind: Service
metadata:
  name: my-ai-app
spec:
  selector:
    app: my-ai-app
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer
```

**Deploy:**
```bash
kubectl apply -f deployment.yaml
kubectl get services
```

---

### Database Setup

#### PostgreSQL (Production)

**Docker Compose:**
```yaml
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: ai_app
      POSTGRES_USER: app_user
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
volumes:
  postgres_data:
```

**Migrations:**
```bash
# Run migrations
python -m alembic upgrade head

# Create new migration
python -m alembic revision --autogenerate -m "Add users table"
```

---

#### Redis (Caching & Sessions)

**Docker Compose:**
```yaml
services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes
volumes:
  redis_data:
```

**Usage in app:**
```python
import redis

# Connect
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Cache LLM responses
def get_llm_response(prompt: str) -> str:
    cache_key = f"llm:{hash(prompt)}"
    
    # Check cache
    cached = r.get(cache_key)
    if cached:
        return cached
    
    # Generate
    response = llm.generate(prompt)
    
    # Cache for 1 hour
    r.setex(cache_key, 3600, response)
    
    return response
```

---

## Scaling & Performance

### Horizontal Scaling

**Load Balancing with NGINX:**
```nginx
upstream ai_app {
    least_conn;
    server app1:8000;
    server app2:8000;
    server app3:8000;
}

server {
    listen 80;
    
    location / {
        proxy_pass http://ai_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

**Auto-scaling (K8s):**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-ai-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-ai-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

---

### Async Processing

**Background Tasks with Celery:**
```python
from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379')

@celery.task
def process_document(doc_id: str):
    """Process document in background"""
    doc = load_document(doc_id)
    embeddings = generate_embeddings(doc)
    store_in_vector_db(embeddings)

# In API endpoint
@app.post("/documents/upload")
async def upload_document(file: UploadFile):
    doc_id = save_file(file)
    process_document.delay(doc_id)  # Run in background
    return {"status": "processing", "doc_id": doc_id}
```

**Start Celery worker:**
```bash
celery -A src.tasks worker --loglevel=info --concurrency=4
```

---

### Caching Strategies

**1. LLM Response Caching:**
```python
from functools import lru_cache
import hashlib

@lru_cache(maxsize=1000)
def get_cached_llm_response(prompt: str, model: str) -> str:
    return llm.generate(prompt, model=model)
```

**2. Vector Search Caching:**
```python
# Cache frequently searched queries
cache_key = f"search:{query_hash}"
results = redis.get(cache_key)
if not results:
    results = vector_store.search(query)
    redis.setex(cache_key, 300, results)  # 5 min cache
```

**3. CDN for Static Assets:**
- Use CloudFront (AWS) or Cloud CDN (GCP)
- Cache audio/image responses
- Reduce latency globally

---

### Database Optimization

**Connection Pooling:**
```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=40,
    pool_timeout=30
)
```

**Indexing:**
```sql
-- Index for fast lookups
CREATE INDEX idx_conversations_user_id ON conversations(user_id);
CREATE INDEX idx_documents_created_at ON documents(created_at DESC);

-- Vector index (pgvector)
CREATE INDEX ON embeddings USING ivfflat (embedding vector_cosine_ops);
```

---

## Security & Compliance

### API Authentication

**JWT Tokens:**
```python
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
import jwt

security = HTTPBearer()

def verify_token(credentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(401, "Invalid token")

@app.get("/protected")
def protected_route(user = Depends(verify_token)):
    return {"user": user}
```

---

### Rate Limiting

**Per-user rate limits:**
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.post("/chat")
@limiter.limit("10/minute")  # 10 requests per minute
async def chat(request: Request, message: str):
    return await process_chat(message)
```

---

### Data Encryption

**Encrypt sensitive data:**
```python
from cryptography.fernet import Fernet

# Generate key (do this once, store securely)
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt
encrypted = cipher.encrypt(b"sensitive data")

# Decrypt
decrypted = cipher.decrypt(encrypted)
```

**Environment variables:**
```bash
# Never commit .env files
# Use secrets management:

# AWS Secrets Manager
aws secretsmanager get-secret-value --secret-id prod/api-keys

# K8s Secrets
kubectl create secret generic api-keys \
  --from-literal=openai-key=sk-...
```

---

### GDPR Compliance

**Data deletion:**
```python
@app.delete("/users/{user_id}/data")
async def delete_user_data(user_id: str):
    # Delete from database
    db.query(User).filter(User.id == user_id).delete()
    db.query(Conversation).filter(Conversation.user_id == user_id).delete()
    
    # Delete from vector store
    vector_store.delete(filter={"user_id": user_id})
    
    # Delete from cache
    redis.delete(f"user:{user_id}:*")
    
    return {"status": "deleted"}
```

---

## Cost Optimization

### LLM Cost Reduction

**1. Model Selection:**
```python
# Use cheaper models for simple tasks
def choose_model(task_complexity: str):
    if task_complexity == "simple":
        return "gpt-3.5-turbo"  # ~$0.002/1K tokens
    elif task_complexity == "medium":
        return "gpt-4-turbo"     # ~$0.01/1K tokens
    else:
        return "gpt-4"           # ~$0.03/1K tokens
```

**2. Prompt Optimization:**
```python
# Bad: Long prompt
prompt = f"Here's a 5000 word document: {long_doc}\n\nSummarize this."

# Good: Chunked processing
chunks = chunk_document(long_doc, size=1000)
summaries = [llm.generate(f"Summarize: {chunk}") for chunk in chunks]
final = llm.generate(f"Combine these: {summaries}")
```

**3. Caching:**
- Cache identical queries (save 100% on repeated calls)
- Cache embeddings (generate once, use forever)
- Semantic caching (similar queries → same answer)

**4. Batch Processing:**
```python
# Process multiple requests together
responses = openai.Completion.create(
    prompts=[prompt1, prompt2, prompt3],  # Batch
    model="gpt-3.5-turbo"
)
```

---

### Vector Store Optimization

**Cost comparison:**
| Provider | Cost | When to Use |
|----------|------|-------------|
| FAISS | Free (self-hosted) | < 1M vectors, single server |
| Pinecone | $70/month | Production, scaling |
| Qdrant | Free (self-hosted) | 1M-10M vectors |
| pgvector | DB cost only | Already using PostgreSQL |

**Tip:** Start with FAISS, migrate to Pinecone when scaling

---

### Compute Optimization

**1. Use spot instances:**
```bash
# AWS EC2 spot (70% cheaper)
aws ec2 run-instances --instance-type t3.large --spot-price "0.05"
```

**2. Auto-scaling:**
- Scale down during low traffic
- Use Cloud Run (pay per request)
- Serverless functions for burst workloads

**3. GPU optimization:**
```python
# Use smaller batch sizes
model = AutoModel.from_pretrained("model", torch_dtype=torch.float16)

# Quantization (4-bit)
model = AutoModel.from_pretrained("model", load_in_4bit=True)
```

---

## Monitoring & Observability

### Application Metrics

**Prometheus + Grafana:**
```python
from prometheus_client import Counter, Histogram, start_http_server

# Metrics
llm_requests = Counter('llm_requests_total', 'Total LLM requests')
llm_latency = Histogram('llm_latency_seconds', 'LLM request latency')
llm_tokens = Counter('llm_tokens_total', 'Total tokens used')

@app.post("/chat")
async def chat(message: str):
    llm_requests.inc()
    
    with llm_latency.time():
        response = await llm.generate(message)
    
    llm_tokens.inc(count_tokens(response))
    return response

# Start metrics server
start_http_server(9090)
```

**Grafana dashboard:**
- Request rate (QPS)
- Latency percentiles (p50, p95, p99)
- Error rate
- Token usage (cost tracking)
- Cache hit rate

---

### Logging

**Structured logging:**
```python
import structlog

logger = structlog.get_logger()

@app.post("/chat")
async def chat(request: Request, message: str):
    logger.info(
        "chat_request",
        user_id=request.state.user_id,
        message_length=len(message),
        model="gpt-4"
    )
    
    try:
        response = await llm.generate(message)
        logger.info(
            "chat_response",
            response_length=len(response),
            latency_ms=elapsed_time
        )
        return response
    except Exception as e:
        logger.error(
            "chat_error",
            error=str(e),
            exc_info=True
        )
        raise
```

---

### Error Tracking

**Sentry integration:**
```python
import sentry_sdk

sentry_sdk.init(
    dsn="https://xxx@sentry.io/xxx",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

# Errors are automatically tracked
# Add context:
with sentry_sdk.configure_scope() as scope:
    scope.set_tag("model", "gpt-4")
    scope.set_user({"id": user_id})
```

---

## Custom Templates

### Extending the Generator

**1. Add custom template:**
```bash
# Create custom template
mkdir -p ~/.one-click-ai/templates/my-feature

# Add Jinja2 template
cat > ~/.one-click-ai/templates/my-feature/custom.py.jinja << EOF
"""
{{ project_name }} - Custom Feature
"""

def my_custom_function():
    """Your custom logic"""
    pass
EOF
```

**2. Use in generator:**
```python
# src/one_click_ai/generator.py
def generate_custom_feature(context: dict):
    template = env.get_template("my-feature/custom.py.jinja")
    content = template.render(context)
    write_file("src/custom.py", content)
```

---

### Template Variables

Available in all templates:
```jinja
{{ project_name }}           # e.g., "my-ai-app"
{{ project_description }}     # Project description
{{ github_username }}         # Your GitHub username
{{ llm_provider }}           # e.g., "openai"
{{ vector_store }}           # e.g., "pinecone"
{{ has_rag }}                # Boolean
{{ has_voice }}              # Boolean
# ... all feature flags
```

---

## Best Practices

### Development Workflow

1. **Use virtual environments:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Pin dependencies:**
   ```text
   # requirements.txt
   fastapi==0.109.0
   openai==1.10.0
   # Not: fastapi>=0.109.0 (can break in production)
   ```

3. **Environment-specific configs:**
   ```
   .env.development
   .env.staging
   .env.production
   ```

4. **Pre-commit hooks:**
   ```yaml
   # .pre-commit-config.yaml
   repos:
     - repo: https://github.com/psf/black
       rev: 23.0.0
       hooks:
         - id: black
     - repo: https://github.com/PyCQA/flake8
       rev: 6.0.0
       hooks:
         - id: flake8
   ```

---

### Testing Strategy

**Unit tests:**
```python
# tests/test_llm.py
import pytest
from src.core.ai.llm import LLMService

@pytest.mark.asyncio
async def test_llm_response():
    llm = LLMService(model="gpt-3.5-turbo")
    response = await llm.generate("Say 'test'")
    assert "test" in response.lower()
```

**Integration tests:**
```python
# tests/test_api.py
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post(
        "/api/v1/chat/message",
        json={"message": "Hello"}
    )
    assert response.status_code == 200
    assert "message" in response.json()
```

**Load testing:**
```bash
# Using locust
pip install locust

# locustfile.py
from locust import HttpUser, task

class AIAppUser(HttpUser):
    @task
    def chat(self):
        self.client.post("/api/v1/chat/message", json={"message": "Hello"})

# Run
locust -f locustfile.py --host http://localhost:8000
```

---

## Next Steps

- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions
- **[API Reference](api.md)** - Complete command documentation
- **[Examples](examples.md)** - More project ideas

