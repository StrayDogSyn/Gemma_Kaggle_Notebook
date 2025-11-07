<div align="center">

# Gemma AI Agents Course

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-3.0+-D00000?style=for-the-badge&logo=keras&logoColor=white)
![JAX](https://img.shields.io/badge/JAX-Latest-9cf?style=for-the-badge)
![Google AI](https://img.shields.io/badge/Google_AI-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

**Google's 5-Day AI Agents Intensive Course**

Building production-ready AI agents with Gemma open-source models

[Course Documentation](docs/COURSE_INFO.md) · [Technical Reference](docs/GEMMA_INFO.md) · [Quick Reference](docs/QUICK_REFERENCE.md)

</div>

## Overview

This repository documents a comprehensive journey through **Google's 5-Day AI Agents Intensive Course** (November 9-13, 2025), focusing on building intelligent agents using **Gemma** - Google's family of lightweight, state-of-the-art open language models built with the same technology as Gemini.

Gemma models bring production-grade AI capabilities to resource-constrained environments with decoder-only transformer architecture trained on 6 trillion tokens across web content, code, and mathematics.

### Course Objectives

Master Gemma model deployment and fine-tuning  
Build production-ready AI agents with memory and planning  
Implement tool-calling and multi-agent orchestration  
Apply responsible AI practices and safety measures  
Complete capstone project demonstrating learned concepts

## Project Structure

```
gemma-kaggle-notebook/
├── notebooks/          
│   ├── setup.ipynb                
│   ├── gemma_quickstart.ipynb     
│   └── ai_agents_course.ipynb      
├── docs/               
│   ├── COURSE_INFO.md             
│   ├── GEMMA_INFO.md              
│   ├── GETTING_STARTED.md          
│   ├── QUICK_REFERENCE.md          
│   └── PROJECT_SUMMARY.md          
├── scripts/            
│   ├── install.py                  
│   └── fix_markdown.py             
├── config/             
│   └── .env.example                
├── requirements.txt    
├── .gitignore         
└── LICENSE            
```

## Quick Start

### Prerequisites

**System Requirements**

RAM: 8GB minimum (16GB recommended for Gemma 2B)  
Storage: 10GB free space  
Python: 3.8 or higher  
OS: Windows, macOS, or Linux

**Required Accounts**

[Kaggle](https://www.kaggle.com) - Phone verified  
[Google AI Studio](https://aistudio.google.com) - API key required  
[Discord](https://discord.gg/kaggle) - Linked to Kaggle account

### Installation

**Automated Setup (Recommended)**

```bash
git clone https://github.com/StrayDogSyn/Gemma_Kaggle_Notebook.git
cd Gemma_Kaggle_Notebook
python scripts/install.py
```

**Manual Setup**

```bash
git clone https://github.com/StrayDogSyn/Gemma_Kaggle_Notebook.git
cd Gemma_Kaggle_Notebook

python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

### Configuration

```bash
cp config/.env.example .env
# Edit .env and add your Google AI Studio API key
# Get key from: https://aistudio.google.com/app/apikey
```

### Verify Installation

Open and run `notebooks/setup.ipynb` to verify your environment configuration.

## Usage Examples

### Basic Text Generation

```python
import keras_hub

gemma_lm = keras_hub.models.GemmaCausalLM.from_preset("gemma_1.1_instruct_2b_en")
output = gemma_lm.generate("Explain machine learning:", max_length=100)
print(output)
```

### With Retry Logic

```python
import google.generativeai as genai
from tenacity import retry, stop_after_attempt, wait_exponential

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def generate_with_retry(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
```

### Batch Processing

```python
prompts = ["Explain neural networks", "What is reinforcement learning?"]

for prompt in prompts:
    response = gemma_lm.generate(prompt, max_length=50)
    print(f"Prompt: {prompt}\nResponse: {response}\n")
```

## Course Schedule

| Day | Date | Topic | Deliverables |
|-----|------|-------|--------------|
| 1 | Nov 9, 2025 | Gemma Introduction & Setup | Environment configured |
| 2 | Nov 10, 2025 | Advanced Prompting & Fine-tuning | Custom fine-tuned model |
| 3 | Nov 11, 2025 | Agent Architecture & Memory | Working agent with memory |
| 4 | Nov 12, 2025 | Tool Calling & Multi-Agent Systems | Multi-agent demo |
| 5 | Nov 13, 2025 | Capstone Project & Best Practices | Complete project |

## Technology Stack

**Core Framework**

Keras 3 - Multi-backend deep learning  
Keras Hub - Pre-trained model library  
JAX - High-performance numerical computing

**AI & APIs**

Google Generative AI SDK - Gemini API integration  
Gemma Models - Open-source language models

**Development Tools**

Jupyter - Interactive notebook environment  
Python-dotenv - Environment variable management  
Tenacity - Retry logic and resilience

## API Best Practices

### Rate Limit Handling

```python
# DO: Use exponential backoff
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def safe_api_call(prompt):
    return model.generate_content(prompt)
```

### Error Handling

| Error Type | Recommended Action |
|------------|-------------------|
| Rate Limit (429) | Exponential backoff, reduce frequency |
| Quota Exceeded | Implement batching, use caching |
| Invalid API Key | Verify credentials, regenerate if needed |
| Network Timeout | Implement retry logic with timeouts |

### Security

Never commit API keys to version control  
Use environment variables for sensitive data  
Rotate API keys regularly  
Implement request validation  
Monitor usage and set alerts

## Model Performance

### Gemma 2B Benchmarks

| Task | Benchmark | Score |
|------|-----------|-------|
| General Knowledge | MMLU | 42.3 |
| Commonsense Reasoning | HellaSwag | 71.4 |
| Code Generation | HumanEval | 22.0 |
| Mathematical Reasoning | GSM8K | 17.7 |

### Gemma 2B vs 7B

| Feature | Gemma 2B | Gemma 7B |
|---------|----------|----------|
| Parameters | 2 billion | 7 billion |
| RAM Required | 8GB+ | 16GB+ |
| Speed | Faster | Slower, higher quality |
| Use Case | Edge devices, prototyping | Production applications |

## Resources

### Official Documentation

[Gemma on Kaggle](https://www.kaggle.com/models/google/gemma)  
[Keras Hub Documentation](https://keras.io/keras_hub/)  
[Gemma Model Card](https://ai.google.dev/gemma)  
[Responsible AI Toolkit](https://ai.google.dev/responsible)

### Course Materials

[Kaggle Course Page](https://www.kaggle.com)  
[Kaggle Discord Community](https://discord.gg/kaggle)  
[YouTube Livestreams](https://www.youtube.com/kaggle)

## Safety and Ethics

Gemma models have been evaluated for content safety, bias and fairness, factual accuracy, and privacy protection with PII filtered from training data.

**Important**: Always verify generated content and implement appropriate safety measures for production use.

## Contributing

This is a personal learning repository by **Eric 'Hunter' Petross** of **StrayDog Syndications LLC** for the 5-Day AI Agents course. Feel free to fork and adapt for your own learning journey.

## License

**Code**: MIT License (see LICENSE file)  
**Gemma Models**: [Gemma Terms of Use](https://ai.google.dev/gemma/terms)

## Acknowledgments

**Course Team**

Google AI - Gemma models and course development  
Kaggle - Platform and community support  
Discord Community - Peer learning and collaboration

**My Learning Journey**

Part of ongoing AI/ML mastery through StrayDog Syndications LLC  
Building practical skills in production AI agent development  
Contributing to open-source AI learning resources

**Eric 'Hunter' Petross**  
*StrayDog Syndications LLC*

---

<div align="center">

**Next Steps**: Review course materials → Run setup notebook → Join Discord community

[⬆ Back to Top](#gemma-ai-agents-course)

</div>