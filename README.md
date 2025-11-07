# Gemma Kaggle Notebook - 5-Day AI Agents Intensive Course

This repository contains materials and notebooks for Google's 5-Day AI Agents Intensive Course (November 9-13, 2025), focusing on the **Gemma** family of open-source language models.

## 🎯 Project Overview

This project demonstrates how to use Google's Gemma models - lightweight, state-of-the-art open language models built with the same technology as Gemini. The notebooks cover everything from basic setup to advanced text generation, question answering, and fine-tuning.

## 📚 Repository Contents

### Documentation
- **`COURSE_INFO.md`** - Complete course information, schedule, and setup checklist
- **`GEMMA_INFO.md`** - Technical reference for Gemma models (architecture, benchmarks, best practices)
- **`README.md`** - This file

### Notebooks
- **`setup.ipynb`** - Environment setup and configuration verification
- **`gemma_quickstart.ipynb`** - Comprehensive guide to using Gemma models with Keras Hub

### Configuration
- **`requirements.txt`** - Python package dependencies
- **`.env.example`** - Template for environment variables
- **`.gitignore`** - Git ignore rules for sensitive data

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/StrayDogSyn/Gemma_Kaggle_Notebook.git
cd Gemma_Kaggle_Notebook

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your Google AI Studio API key
# Get your key from: https://aistudio.google.com/app/apikey
```

### 3. Run the Setup Notebook

Open `setup.ipynb` in Jupyter or VS Code and run through the cells to verify your environment.

### 4. Start with Gemma

Open `gemma_quickstart.ipynb` to begin working with Gemma models.

## 📋 Prerequisites

### System Requirements
- **RAM**: 8GB minimum (16GB recommended for Gemma 2B)
- **Storage**: 10GB free space
- **Python**: 3.8 or higher

### Accounts Needed
- ✅ [Kaggle Account](https://www.kaggle.com) (phone verified)
- ✅ [Google AI Studio Account](https://aistudio.google.com) (with API key)
- ✅ [Discord Account](https://discord.gg/kaggle) (linked to Kaggle)

## 🧠 About Gemma Models

**Gemma** is Google's family of lightweight, open-source LLMs:

- **Architecture**: Decoder-only transformer
- **Variants**: 2B and 7B parameter models
- **Training**: 6 trillion tokens (web, code, math)
- **Capabilities**: Text generation, Q&A, summarization, code generation
- **Backends**: JAX, TensorFlow, or PyTorch (via Keras 3)

### Model Performance (Gemma 2B)

| Task | Benchmark | Score |
|------|-----------|-------|
| General Knowledge | MMLU | 42.3 |
| Commonsense | HellaSwag | 71.4 |
| Code Generation | HumanEval | 22.0 |
| Math | GSM8K | 17.7 |

## 📖 Usage Examples

### Basic Text Generation

```python
import keras_hub

# Load model
gemma_lm = keras_hub.models.GemmaCausalLM.from_preset("gemma_1.1_instruct_2b_en")

# Generate text
output = gemma_lm.generate("Explain machine learning:", max_length=100)
print(output)
```

### Question Answering

```python
question = "What is the capital of France?"
answer = gemma_lm.generate(question, max_length=50)
print(answer)
```

### Batch Processing

```python
prompts = [
    "Write a Python function to sort a list:",
    "Explain quantum computing:",
    "Summarize the theory of relativity:"
]

outputs = gemma_lm.generate(prompts, max_length=100)
for prompt, output in zip(prompts, outputs):
    print(f"Q: {prompt}\nA: {output}\n")
```

## 🎓 Course Information

### Schedule
- **Start**: Sunday, November 9, 2025
- **Duration**: 5 days
- **Live Sessions**: Monday-Friday, 11 AM PT / 8 PM CET / 12:30 AM IST
- **Platform**: [Kaggle](https://www.kaggle.com)

### Daily Format
1. New assignments posted daily
2. Materials include whitepapers, codelabs, podcasts
3. Live YouTube sessions with Google researchers
4. Discord discussions and Q&A
5. Optional capstone project on Day 5

### Discord Channels
- `#5dgai-announcements` - Official announcements
- `#5dgai-introductions` - Meet other participants
- `#5dgai-question-forum` - Ask questions
- `#5dgai-general-chat` - General discussion

## 🛠️ Key Technologies

- **Keras 3** - Multi-backend deep learning framework
- **Keras Hub** - Pre-trained model library
- **JAX** - High-performance numerical computing (recommended backend)
- **Google Generative AI** - API for Google's AI models
- **Jupyter** - Interactive notebook environment

## 📦 Dependencies

Main packages (see `requirements.txt` for full list):

```
keras>=3.0.0
keras-hub
jax[cpu]
google-generativeai
numpy
pandas
jupyter
```

## 🔒 Safety and Ethics

Gemma models have been evaluated for:
- ✅ Content safety
- ✅ Bias and fairness
- ✅ Factual accuracy
- ✅ Privacy protection (PII filtered)

**Important**: Always verify generated content and implement appropriate safety measures for production use.

## 📚 Resources

### Official Documentation
- [Gemma on Kaggle](https://www.kaggle.com/models/google/gemma)
- [Keras Hub Docs](https://keras.io/keras_hub/)
- [Gemma Model Card](https://ai.google.dev/gemma)
- [Responsible AI Toolkit](https://ai.google.dev/responsible)

### Course Resources
- [Kaggle Course Page](https://www.kaggle.com)
- [Kaggle Discord](https://discord.gg/kaggle)
- [YouTube Livestreams](https://www.youtube.com/kaggle)

## 🤝 Contributing

This is a personal learning repository for the 5-Day AI Agents course. Feel free to fork and adapt for your own learning!

## 📄 License

- **Code**: MIT License (see LICENSE file)
- **Gemma Models**: [Gemma Terms of Use](https://ai.google.dev/gemma/terms)

## 👤 Author

**Eric Hunt** - Course participant

## 🙏 Acknowledgments

- Google AI team for creating Gemma
- Kaggle team for organizing the course
- Course instructors: Kanchana Patlolla and Anant Nawalgaria
- All course participants and community members

---

**Note**: This repository is part of the 5-Day AI Agents Intensive Course (Nov 9-13, 2025). Materials will be updated throughout the course.
Welcome to our 5-Day AI Agents Intensive Course with Google! We’re glad you’re here.
