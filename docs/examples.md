# Examples

Real-world AI projects you can build with One Click AI Spark. Each example includes the command, explanation, and how to use it.

## Table of Contents

- [Beginner Examples](#beginner-examples)
- [Intermediate Examples](#intermediate-examples)
- [Advanced Examples](#advanced-examples)
- [Industry-Specific Examples](#industry-specific-examples)

---

## Beginner Examples

### Example 1: Simple Chatbot

**What it does:** Basic GPT-4 chatbot with conversation memory.

**Command:**
```bash
one-click-ai generate --name simple-chatbot --features llm,memory --output ./simple-chatbot
```

**What you get:**
- Chat API endpoint
- Conversation history
- OpenAI GPT integration

**Setup:**
```bash
cd simple-chatbot
cp .env.example .env
# Add OPENAI_API_KEY to .env
pip install -r requirements.txt
python src/main.py
```

**Test it:**
```bash
curl -X POST "http://localhost:8000/api/v1/chat/message" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!", "conversation_id": "user-1"}'
```

**Use cases:**
- Customer support
- Personal assistant
- Learning companion

---

### Example 2: Document Q&A System

**What it does:** Upload PDFs and ask questions about them.

**Command:**
```bash
one-click-ai generate --name doc-qa --features llm,rag --vector-store faiss --output ./doc-qa
```

**What you get:**
- Document upload API
- PDF/TXT/DOCX processing
- Vector search
- Context-aware answers

**Setup:**
```bash
cd doc-qa
cp .env.example .env
pip install -r requirements.txt
python src/main.py
```

**Test it:**
```bash
# 1. Upload a document
curl -X POST "http://localhost:8000/api/v1/documents/upload" \
  -F "file=@manual.pdf"

# 2. Ask questions
curl -X POST "http://localhost:8000/api/v1/chat/message" \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the return policy?"}'
```

**Use cases:**
- Company knowledge base
- Research paper analysis
- Legal document review
- Study assistants

---

### Example 3: Voice Note Transcriber

**What it does:** Converts voice recordings to text.

**Command:**
```bash
one-click-ai generate --name transcriber --features voice --stt-provider openai --output ./transcriber
```

**What you get:**
- Audio file upload
- Speech-to-text (Whisper)
- Supports multiple languages

**Test it:**
```bash
curl -X POST "http://localhost:8000/api/v1/voice/transcribe" \
  -F "audio=@recording.mp3"
```

**Use cases:**
- Meeting notes
- Interview transcription
- Voice memos
- Podcast transcripts

---

## Intermediate Examples

### Example 4: Customer Support Bot with Knowledge Base

**What it does:** AI support agent that knows your docs + searches web.

**Command:**
```bash
one-click-ai generate \
  --name support-bot \
  --features llm,rag,search,emotion,guardrails \
  --vector-store pinecone \
  --search-provider tavily \
  --output ./support-bot
```

**What you get:**
- Document-powered answers
- Real-time web search for latest info
- Emotion detection in customer messages
- Content safety filters
- PII protection

**Setup:**
```bash
cd support-bot
cp .env.example .env
# Add API keys:
# OPENAI_API_KEY
# PINECONE_API_KEY
# TAVILY_API_KEY
pip install -r requirements.txt
python src/main.py
```

**Upload knowledge base:**
```bash
# Upload FAQ, policies, manuals
curl -X POST "http://localhost:8000/api/v1/documents/upload" \
  -F "file=@faq.pdf" \
  -F "file=@return_policy.pdf" \
  -F "file=@user_manual.pdf"
```

**Test conversation:**
```bash
# Customer asks about returns
curl -X POST "http://localhost:8000/api/v1/chat/message" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "I want to return my product but lost the receipt",
    "customer_id": "cust-123"
  }'

# Response will:
# 1. Detect emotion (possibly frustrated)
# 2. Search knowledge base for return policy
# 3. Search web if needed for latest policies
# 4. Provide empathetic, accurate answer
# 5. Filter any sensitive info
```

**Use cases:**
- E-commerce support
- SaaS help desks
- Call center deflection
- 24/7 automated support

**Advanced features:**
```python
# Get conversation analytics
curl "http://localhost:8000/api/v1/analytics/customer/cust-123"
# Returns: emotion trends, common issues, satisfaction score
```

---

### Example 5: Voice Assistant (like Alexa/Siri)

**What it does:** Speak to it, it speaks back with AI responses.

**Command:**
```bash
one-click-ai generate \
  --name voice-assistant \
  --features llm,voice,voice_to_voice,memory \
  --stt-provider openai \
  --tts-provider elevenlabs \
  --output ./voice-assistant
```

**What you get:**
- Real-time voice chat
- Natural-sounding responses
- Multi-turn conversations
- Personalized responses

**Setup:**
```bash
cd voice-assistant
cp .env.example .env
# Add API keys:
# OPENAI_API_KEY
# ELEVENLABS_API_KEY
pip install -r requirements.txt
python src/main.py
```

**Web interface example (HTML + JS):**
```html
<!DOCTYPE html>
<html>
<body>
  <button id="record">🎤 Hold to Talk</button>
  <audio id="response" autoplay></audio>

  <script>
    const recordBtn = document.getElementById('record');
    const audioPlayer = document.getElementById('response');
    let mediaRecorder;
    let audioChunks = [];

    recordBtn.addEventListener('mousedown', async () => {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorder = new MediaRecorder(stream);
      
      mediaRecorder.ondataavailable = (e) => {
        audioChunks.push(e.data);
      };
      
      mediaRecorder.start();
    });

    recordBtn.addEventListener('mouseup', () => {
      mediaRecorder.stop();
      
      mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        audioChunks = [];
        
        // Send to API
        const formData = new FormData();
        formData.append('audio', audioBlob);
        
        const response = await fetch('http://localhost:8000/api/v1/voice/chat', {
          method: 'POST',
          body: formData
        });
        
        // Play AI response
        const responseBlob = await response.blob();
        audioPlayer.src = URL.createObjectURL(responseBlob);
      };
    });
  </script>
</body>
</html>
```

**Use cases:**
- Smart home control
- Hands-free apps
- Accessibility tools
- Language learning
- Elderly care assistants

---

### Example 6: Image Analysis API

**What it does:** Analyze images for objects, text, faces, and descriptions.

**Command:**
```bash
one-click-ai generate \
  --name vision-api \
  --features llm,vision,computer_vision \
  --vision-provider openai \
  --cv-frameworks yolo,ocr \
  --output ./vision-api
```

**What you get:**
- GPT-4V image understanding
- YOLO object detection
- OCR text extraction
- Face detection
- Multi-modal chat (images + text)

**Test it:**
```bash
# 1. Describe image
curl -X POST "http://localhost:8000/api/v1/vision/describe" \
  -F "image=@photo.jpg"
# Returns: "A person wearing a blue shirt standing in front of a bookshelf"

# 2. Detect objects
curl -X POST "http://localhost:8000/api/v1/vision/detect" \
  -F "image=@street.jpg"
# Returns: {"objects": [{"class": "car", "confidence": 0.95, "bbox": [...]}]}

# 3. Extract text (OCR)
curl -X POST "http://localhost:8000/api/v1/vision/ocr" \
  -F "image=@document.jpg"
# Returns: {"text": "Invoice #12345..."}

# 4. Chat about image
curl -X POST "http://localhost:8000/api/v1/vision/chat" \
  -F "image=@diagram.png" \
  -F "message=Explain this diagram"
```

**Use cases:**
- Product cataloging
- Content moderation
- Receipt scanning
- Medical imaging
- Security surveillance

---

### Example 7: Research Assistant with Web Search

**What it does:** AI that searches web + docs, plans research, writes reports.

**Command:**
```bash
one-click-ai generate \
  --name research-bot \
  --features llm,rag,search,agents \
  --search-provider tavily \
  --output ./research-bot
```

**What you get:**
- Autonomous research agent
- Multi-step planning
- Web search + document search
- Automated report writing

**Example task:**
```bash
curl -X POST "http://localhost:8000/api/v1/agent/task" \
  -H "Content-Type: application/json" \
  -d '{
    "goal": "Research top 3 AI trends in 2024 and create a 500-word summary with sources",
    "tools": ["web_search", "document_search", "document_writer"]
  }'
```

**What the agent does:**
1. Plans: "I need to search for AI trends, find top 3, gather details, write summary"
2. Executes web searches: "AI trends 2024", "artificial intelligence developments"
3. Analyzes results
4. Searches your internal docs for related info
5. Synthesizes findings
6. Writes formatted report
7. Cites sources

**Use cases:**
- Market research
- Competitive analysis
- Literature reviews
- Due diligence
- Content research

---

## Advanced Examples

### Example 8: Full-Stack AI SaaS Platform

**What it does:** Production-ready AI platform with multi-tenancy, monitoring, and scaling.

**Command:**
```bash
one-click-ai generate \
  --name ai-saas \
  --features llm,rag,voice,vision,agents,memory,guardrails,analytics,multi_tenant \
  --vector-store pinecone \
  --session-backend redis \
  --docker \
  --ci_cd \
  --iac \
  --monitoring \
  --output ./ai-saas
```

**What you get:**
- Multi-tenant architecture (separate data per customer)
- All AI features (LLM, RAG, voice, vision, agents)
- Production infrastructure (Docker, K8s, CI/CD)
- Monitoring (Prometheus, Grafana, Sentry)
- Safety guardrails
- Analytics dashboard
- Infrastructure as code (Terraform)

**Architecture:**
```
┌─────────────────────────────────────────┐
│  Load Balancer (NGINX)                  │
└─────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  API Gateway (FastAPI)                  │
│  - Auth & Rate Limiting                 │
│  - Tenant Isolation                     │
└─────────────────────────────────────────┘
           │
     ┌─────┴─────┬────────┬────────┐
     ▼           ▼        ▼        ▼
┌─────────┐ ┌────────┐ ┌──────┐ ┌─────────┐
│ LLM     │ │ RAG    │ │Voice │ │ Agents  │
│ Service │ │ Engine │ │ AI   │ │ Service │
└─────────┘ └────────┘ └──────┘ └─────────┘
           │
     ┌─────┴─────┬────────┬────────┐
     ▼           ▼        ▼        ▼
┌─────────┐ ┌────────┐ ┌──────┐ ┌─────────┐
│ Vector  │ │ Cache  │ │Queue │ │ Metrics │
│ DB      │ │ Redis  │ │ DB   │ │ System  │
└─────────┘ └────────┘ └──────┘ └─────────┘
```

**Deploy to AWS:**
```bash
cd ai-saas/iac/terraform
terraform init
terraform apply

# Outputs:
# - Load Balancer URL: https://ai-saas.example.com
# - Grafana: https://metrics.example.com
# - Admin Panel: https://admin.example.com
```

**Use cases:**
- AI-powered SaaS products
- Enterprise AI platforms
- White-label AI solutions

---

### Example 9: Edge AI for Mobile Apps

**What it does:** Deploy AI models that run on-device (offline capable).

**Command:**
```bash
one-click-ai generate \
  --name mobile-ai \
  --features ml_training,edge_ai,computer_vision \
  --ml-frameworks pytorch \
  --edge-runtimes onnx,tflite \
  --cv-frameworks yolo \
  --output ./mobile-ai
```

**Workflow:**

**1. Train custom model:**
```bash
# Upload training data
curl -X POST "http://localhost:8000/api/v1/ml/upload_data" \
  -F "data=@training_images.zip" \
  -F "labels=@labels.csv"

# Train
curl -X POST "http://localhost:8000/api/v1/ml/train" \
  -H "Content-Type: application/json" \
  -d '{
    "model_type": "image_classifier",
    "classes": ["dog", "cat", "bird"],
    "epochs": 50
  }'
```

**2. Convert to mobile format:**
```bash
# Convert to ONNX + TFLite
curl -X POST "http://localhost:8000/api/v1/edge/convert" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": "trained-model-123",
    "formats": ["onnx", "tflite"],
    "quantization": "int8",
    "optimization_level": "aggressive"
  }'

# Download optimized models
curl "http://localhost:8000/api/v1/edge/download/model-123.tflite" \
  -o model.tflite
```

**3. Integrate in mobile app:**

**Android (Kotlin):**
```kotlin
import org.tensorflow.lite.Interpreter

class ImageClassifier {
    private val interpreter: Interpreter
    
    init {
        val model = loadModelFile("model.tflite")
        interpreter = Interpreter(model)
    }
    
    fun classify(bitmap: Bitmap): String {
        val input = preprocessImage(bitmap)
        val output = Array(1) { FloatArray(3) }
        interpreter.run(input, output)
        return getTopClass(output[0])
    }
}
```

**iOS (Swift):**
```swift
import CoreML

class ImageClassifier {
    let model = try! model()
    
    func classify(image: UIImage) -> String {
        let input = preprocessImage(image)
        let prediction = try! model.prediction(input: input)
        return prediction.classLabel
    }
}
```

**Use cases:**
- Mobile apps with AI features
- IoT devices
- Raspberry Pi projects
- Offline-first apps
- Privacy-focused AI (data stays on device)

---

### Example 10: Multi-Modal AI Agent

**What it does:** Agent that can see, hear, speak, and reason.

**Command:**
```bash
one-click-ai generate \
  --name multimodal-agent \
  --features llm,rag,voice,vision,agents,memory,search \
  --stt-provider openai \
  --tts-provider elevenlabs \
  --vision-provider openai \
  --search-provider tavily \
  --output ./multimodal-agent
```

**Capabilities:**
- Analyzes images and videos
- Listens to voice commands
- Responds with speech
- Searches web and documents
- Plans and executes tasks
- Remembers past interactions

**Example interaction:**
```python
# Complex multi-modal task
response = requests.post(
    "http://localhost:8000/api/v1/agent/task",
    files={
        "image": open("diagram.png", "rb"),
        "audio": open("instructions.mp3", "rb")
    },
    data={
        "goal": "Analyze this diagram, listen to my voice instructions, search for relevant info, and explain back to me in audio form",
        "user_id": "user-123"
    }
)

# Agent will:
# 1. Transcribe audio: "Explain what's wrong with this circuit diagram"
# 2. Analyze image: Detect circuit components, find errors
# 3. Search web: Look up correct circuit configurations
# 4. Search docs: Find internal troubleshooting guides
# 5. Synthesize answer
# 6. Convert to speech
# 7. Remember this interaction for follow-ups
```

**Use cases:**
- Advanced virtual assistants
- Accessibility tools
- Education platforms
- Healthcare assistants
- Technical support

---

## Industry-Specific Examples

### Example 11: Healthcare - Medical Imaging Analysis

**Command:**
```bash
one-click-ai generate \
  --name medical-imaging \
  --features vision,computer_vision,ml_training,guardrails \
  --cv-frameworks yolo \
  --output ./medical-imaging
```

**Use cases:**
- X-ray analysis
- Tumor detection
- Disease classification
- Medical report generation (with HIPAA compliance)

---

### Example 12: Legal - Contract Analysis

**Command:**
```bash
one-click-ai generate \
  --name legal-ai \
  --features llm,rag,analytics,guardrails \
  --vector-store pinecone \
  --output ./legal-ai
```

**Use cases:**
- Contract review
- Legal research
- Due diligence
- Compliance checking

**Example:**
```bash
# Upload contracts
curl -X POST "http://localhost:8000/api/v1/documents/upload" \
  -F "file=@contract1.pdf" \
  -F "file=@contract2.pdf"

# Ask questions
curl -X POST "http://localhost:8000/api/v1/chat/message" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What are the termination clauses across all contracts?",
    "mode": "legal_analysis"
  }'
```

---

### Example 13: E-commerce - Product Recommendation Engine

**Command:**
```bash
one-click-ai generate \
  --name product-recommender \
  --features llm,ml_training,analytics,memory \
  --ml-frameworks xgboost \
  --output ./product-recommender
```

**Features:**
- User behavior tracking
- Product embeddings
- Personalized recommendations
- Natural language product search

---

### Example 14: Finance - Trading Bot

**Command:**
```bash
one-click-ai generate \
  --name trading-bot \
  --features llm,agents,search,analytics,ml_training \
  --ml-frameworks pytorch \
  --output ./trading-bot
```

**Use cases:**
- Market analysis
- Sentiment analysis from news
- Automated trading strategies
- Risk assessment

---

### Example 15: Education - AI Tutor

**Command:**
```bash
one-click-ai generate \
  --name ai-tutor \
  --features llm,rag,voice,vision,agents,memory \
  --output ./ai-tutor
```

**Features:**
- Personalized learning paths
- Homework help
- Concept explanations
- Progress tracking
- Voice interactions
- Image problem solving

**Example:**
```bash
# Student uploads homework photo
curl -X POST "http://localhost:8000/api/v1/tutor/help" \
  -F "image=@math_problem.jpg" \
  -F "message=I don't understand this calculus problem" \
  -F "student_id=student-123"

# AI tutor will:
# 1. OCR the image to extract problem
# 2. Understand the concept (derivatives)
# 3. Check student's past performance on similar topics
# 4. Provide step-by-step explanation
# 5. Generate practice problems
# 6. Track progress
```

---

## Quick Reference

| Example | Features | Difficulty | Time to Build |
|---------|----------|------------|---------------|
| Simple Chatbot | `llm,memory` | Beginner | 5 min |
| Document Q&A | `llm,rag` | Beginner | 10 min |
| Voice Transcriber | `voice` | Beginner | 5 min |
| Support Bot | `llm,rag,search,emotion,guardrails` | Intermediate | 15 min |
| Voice Assistant | `llm,voice,voice_to_voice,memory` | Intermediate | 20 min |
| Vision API | `llm,vision,computer_vision` | Intermediate | 15 min |
| Research Assistant | `llm,rag,search,agents` | Intermediate | 20 min |
| AI SaaS Platform | All features | Advanced | 30 min |
| Mobile AI | `ml_training,edge_ai,computer_vision` | Advanced | 25 min |
| Multi-Modal Agent | `llm,rag,voice,vision,agents` | Advanced | 30 min |

---

## Next Steps

- **[Advanced Guide](advanced.md)** - Production deployment, scaling, optimization
- **[API Reference](api.md)** - Complete command documentation
- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions

