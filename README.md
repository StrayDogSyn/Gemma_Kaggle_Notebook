<div align="center"># Gemma Kaggle Notebook - 5-Day AI Agents Intensive Course



# 🤖 AI Agents Intensive CourseThis repository contains materials and notebooks for Google's 5-Day AI Agents Intensive Course (November 9-13, 2025), focusing on the **Gemma** family of open-source language models.

### Google's 5-Day Deep Dive into Gemma Models

## 🎯 Project Overview

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

[![Keras](https://img.shields.io/badge/Keras-3.0+-D00000?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io/)This project demonstrates how to use Google's Gemma models - lightweight, state-of-the-art open language models built with the same technology as Gemini. The notebooks cover everything from basic setup to advanced text generation, question answering, and fine-tuning.

[![JAX](https://img.shields.io/badge/JAX-Latest-9cf?style=for-the-badge)](https://github.com/google/jax)

[![Google AI](https://img.shields.io/badge/Google_AI-Gemini_API-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)## 📚 Repository Contents

[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

### Documentation

[![Kaggle](https://img.shields.io/badge/Kaggle-Course-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com)- **`COURSE_INFO.md`** - Complete course information, schedule, and setup checklist

[![Discord](https://img.shields.io/badge/Discord-Community-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/kaggle)- **`GEMMA_INFO.md`** - Technical reference for Gemma models (architecture, benchmarks, best practices)

[![Status](https://img.shields.io/badge/Status-Active_Learning-success?style=for-the-badge)]()- **`README.md`** - This file



*Building production-ready AI agents with Google's open-source Gemma models*### Notebooks

- **`setup.ipynb`** - Environment setup and configuration verification

[Course Info](COURSE_INFO.md) • [Technical Docs](GEMMA_INFO.md) • [Getting Started](GETTING_STARTED.md) • [Quick Reference](QUICK_REFERENCE.md)- **`gemma_quickstart.ipynb`** - Comprehensive guide to using Gemma models with Keras Hub



</div>### Configuration

- **`requirements.txt`** - Python package dependencies

---- **`.env.example`** - Template for environment variables

- **`.gitignore`** - Git ignore rules for sensitive data

## 📋 Table of Contents

## 🚀 Quick Start

- [About](#-about)

- [Features](#-features)### 1. Installation

- [Tech Stack](#-tech-stack)

- [Project Structure](#-project-structure)```bash

- [Quick Start](#-quick-start)# Clone the repository

- [Usage Examples](#-usage-examples)git clone https://github.com/StrayDogSyn/Gemma_Kaggle_Notebook.git

- [Course Schedule](#-course-schedule)cd Gemma_Kaggle_Notebook

- [API Best Practices](#-api-best-practices)

- [Model Performance](#-model-performance)# Install dependencies

- [Resources](#-resources)pip install -r requirements.txt

- [Contributing](#-contributing)```

- [License](#-license)

### 2. Configuration

---

```bash

## 🎯 About# Copy environment template

cp .env.example .env

This repository documents my journey through **Google's 5-Day AI Agents Intensive Course** (November 9-13, 2025), a comprehensive deep-dive into building intelligent agents using the **Gemma** family of open-source language models.

# Edit .env and add your Google AI Studio API key

### What is Gemma?# Get your key from: https://aistudio.google.com/app/apikey

```

Gemma represents Google's commitment to open AI development—a family of lightweight, state-of-the-art LLMs built with the same research and technology that powers Gemini. These models bring production-grade AI capabilities to resource-constrained environments.

### 3. Run the Setup Notebook

**Key Characteristics:**

- 🏗️ **Architecture**: Decoder-only transformer (text-to-text)Open `setup.ipynb` in Jupyter or VS Code and run through the cells to verify your environment.

- 📊 **Training**: 6 trillion tokens (web, code, mathematics)

- ⚡ **Performance**: Optimized for JAX on TPUs### 4. Start with Gemma

- 🌍 **Open Source**: Commercially permissive licensing

- 🎯 **Variants**: 2B and 7B parameter models (base + instruction-tuned)Open `gemma_quickstart.ipynb` to begin working with Gemma models.



### Course Objectives## 📋 Prerequisites



- ✅ Master Gemma model deployment and fine-tuning### System Requirements

- ✅ Build production-ready AI agents with memory and planning- **RAM**: 8GB minimum (16GB recommended for Gemma 2B)

- ✅ Implement tool-calling and multi-agent orchestration- **Storage**: 10GB free space

- ✅ Apply responsible AI practices and safety measures- **Python**: 3.8 or higher

- ✅ Complete capstone project demonstrating learned concepts

### Accounts Needed

---- ✅ [Kaggle Account](https://www.kaggle.com) (phone verified)

- ✅ [Google AI Studio Account](https://aistudio.google.com) (with API key)

## ✨ Features- ✅ [Discord Account](https://discord.gg/kaggle) (linked to Kaggle)



### 🛠️ Development Tools## 🧠 About Gemma Models

- **Interactive Notebooks**: Jupyter-based learning environment

- **Environment Management**: Python virtual environment with dependency isolation**Gemma** is Google's family of lightweight, open-source LLMs:

- **API Integration**: Google AI Studio and Keras Hub connectivity

- **Error Handling**: Robust retry logic with exponential backoff- **Architecture**: Decoder-only transformer

- **Configuration**: Secure credential management with python-dotenv- **Variants**: 2B and 7B parameter models

- **Training**: 6 trillion tokens (web, code, math)

### 📚 Learning Resources- **Capabilities**: Text generation, Q&A, summarization, code generation

- **Comprehensive Documentation**: 6 markdown guides covering all aspects- **Backends**: JAX, TensorFlow, or PyTorch (via Keras 3)

- **Code Examples**: 3 production-ready notebooks with 30+ code sections

- **Daily Templates**: Structured note-taking for 5-day course### Model Performance (Gemma 2B)

- **Best Practices**: API usage patterns, prompt engineering, safety guidelines

| Task | Benchmark | Score |

### 🔒 Production-Ready Features|------|-----------|-------|

- Rate limit handling with exponential backoff| General Knowledge | MMLU | 42.3 |

- Environment detection (Kaggle vs. local)| Commonsense | HellaSwag | 71.4 |

- Secure API key management| Code Generation | HumanEval | 22.0 |

- Multi-backend support (JAX/TensorFlow/PyTorch)| Math | GSM8K | 17.7 |

- Comprehensive error messages and debugging tips

## 📖 Usage Examples

---

### Basic Text Generation

## 🔧 Tech Stack

```python

<table>import keras_hub

<tr>

<td valign="top" width="50%"># Load model

gemma_lm = keras_hub.models.GemmaCausalLM.from_preset("gemma_1.1_instruct_2b_en")

### Core Framework

- **Keras 3** - Multi-backend deep learning# Generate text

- **Keras Hub** - Pre-trained model libraryoutput = gemma_lm.generate("Explain machine learning:", max_length=100)

- **JAX** - High-performance computing (recommended)print(output)

- **TensorFlow** - Alternative backend```

- **PyTorch** - Alternative backend

### Question Answering

</td>

<td valign="top" width="50%">```python

question = "What is the capital of France?"

### AI & APIsanswer = gemma_lm.generate(question, max_length=50)

- **Google Generative AI SDK** - Gemini API accessprint(answer)

- **Gemma Models** - Open-source LLMs```

- **Python 3.8+** - Core language

- **NumPy/Pandas** - Data manipulation### Batch Processing

- **Jupyter** - Interactive development

```python

</td>prompts = [

</tr>    "Write a Python function to sort a list:",

</table>    "Explain quantum computing:",

    "Summarize the theory of relativity:"

### Development Environment]



```textoutputs = gemma_lm.generate(prompts, max_length=100)

├── Virtual Environment (.venv)for prompt, output in zip(prompts, outputs):

├── Environment Variables (.env)    print(f"Q: {prompt}\nA: {output}\n")

├── Package Management (pip, requirements.txt)```

└── Version Control (Git, .gitignore)

```## 🎓 Course Information



---### Schedule

- **Start**: Sunday, November 9, 2025

## 📁 Project Structure- **Duration**: 5 days

- **Live Sessions**: Monday-Friday, 11 AM PT / 8 PM CET / 12:30 AM IST

```text- **Platform**: [Kaggle](https://www.kaggle.com)

Gemma_Kaggle_Notebook/

├── 📓 Notebooks### Daily Format

│   ├── setup.ipynb                 # Environment verification & API testing1. New assignments posted daily

│   ├── gemma_quickstart.ipynb      # Comprehensive Gemma tutorial2. Materials include whitepapers, codelabs, podcasts

│   └── ai_agents_course.ipynb      # 5-day course structure3. Live YouTube sessions with Google researchers

│4. Discord discussions and Q&A

├── 📚 Documentation5. Optional capstone project on Day 5

│   ├── README.md                   # This file

│   ├── COURSE_INFO.md              # Course schedule & checklist### Discord Channels

│   ├── GEMMA_INFO.md               # Technical reference- `#5dgai-announcements` - Official announcements

│   ├── GETTING_STARTED.md          # Setup guide- `#5dgai-introductions` - Meet other participants

│   ├── PROJECT_SUMMARY.md          # Progress tracking- `#5dgai-question-forum` - Ask questions

│   └── QUICK_REFERENCE.md          # Command reference- `#5dgai-general-chat` - General discussion

│

├── ⚙️ Configuration## 🛠️ Key Technologies

│   ├── requirements.txt            # Python dependencies

│   ├── .env.example                # Environment template- **Keras 3** - Multi-backend deep learning framework

│   ├── .gitignore                  # Git exclusions- **Keras Hub** - Pre-trained model library

│   ├── .markdownlint.json          # Linting config- **JAX** - High-performance numerical computing (recommended backend)

│   └── install.py                  # Automated setup script- **Google Generative AI** - API for Google's AI models

│- **Jupyter** - Interactive notebook environment

├── 🔒 Security (gitignored)

│   ├── .env                        # API keys (create from .env.example)## 📦 Dependencies

│   └── .venv/                      # Virtual environment

│Main packages (see `requirements.txt` for full list):

└── 📄 License & Metadata

    └── LICENSE                     # MIT License```

```keras>=3.0.0

keras-hub

---jax[cpu]

google-generativeai

## 🚀 Quick Startnumpy

pandas

### Prerequisitesjupyter

```

<table>

<tr>## 🔒 Safety and Ethics

<td>

Gemma models have been evaluated for:

**System Requirements**- ✅ Content safety

- RAM: 8GB minimum (16GB recommended)- ✅ Bias and fairness

- Storage: 10GB free space- ✅ Factual accuracy

- Python: 3.8 or higher- ✅ Privacy protection (PII filtered)

- OS: Windows, macOS, or Linux

**Important**: Always verify generated content and implement appropriate safety measures for production use.

</td>

<td>## 📚 Resources



**Accounts Needed**### Official Documentation

- [Kaggle](https://www.kaggle.com) (phone verified)- [Gemma on Kaggle](https://www.kaggle.com/models/google/gemma)

- [Google AI Studio](https://aistudio.google.com) (API key)- [Keras Hub Docs](https://keras.io/keras_hub/)

- [Discord](https://discord.gg/kaggle) (linked to Kaggle)- [Gemma Model Card](https://ai.google.dev/gemma)

- [Responsible AI Toolkit](https://ai.google.dev/responsible)

</td>

</tr>### Course Resources

</table>- [Kaggle Course Page](https://www.kaggle.com)

- [Kaggle Discord](https://discord.gg/kaggle)

### Installation- [YouTube Livestreams](https://www.youtube.com/kaggle)



**Option 1: Automated Setup (Recommended)**## 🤝 Contributing



```bashThis is a personal learning repository for the 5-Day AI Agents course. Feel free to fork and adapt for your own learning!

# Clone the repository

git clone https://github.com/StrayDogSyn/Gemma_Kaggle_Notebook.git## 📄 License

cd Gemma_Kaggle_Notebook

- **Code**: MIT License (see LICENSE file)

# Run automated installation- **Gemma Models**: [Gemma Terms of Use](https://ai.google.dev/gemma/terms)

python install.py

```## 👤 Author



**Option 2: Manual Setup****Eric Hunt** - Course participant



```bash## 🙏 Acknowledgments

# Create virtual environment

python -m venv .venv- Google AI team for creating Gemma

- Kaggle team for organizing the course

# Activate virtual environment- Course instructors: Kanchana Patlolla and Anant Nawalgaria

# Windows:- All course participants and community members

.venv\Scripts\activate

# macOS/Linux:---

source .venv/bin/activate

**Note**: This repository is part of the 5-Day AI Agents Intensive Course (Nov 9-13, 2025). Materials will be updated throughout the course.

# Install dependenciesWelcome to our 5-Day AI Agents Intensive Course with Google! We’re glad you’re here.

pip install -r requirements.txt
```

### Configuration

```bash
# 1. Copy environment template
cp .env.example .env

# 2. Get your API key
# Visit: https://aistudio.google.com/app/apikey

# 3. Edit .env and add your key
# GOOGLE_API_KEY=your_key_here

# 4. Verify setup
jupyter notebook setup.ipynb
```

---

## 💻 Usage Examples

### Basic Text Generation

```python
import keras_hub

# Load instruction-tuned Gemma model
model = keras_hub.models.GemmaCausalLM.from_preset("gemma_1.1_instruct_2b_en")

# Generate text
prompt = "Explain quantum computing in simple terms:"
output = model.generate(prompt, max_length=100)
print(output)
```

### Question Answering with Retry Logic

```python
import google.generativeai as genai
from typing import Optional
import time

def generate_with_retry(model, prompt: str, max_retries: int = 3) -> Optional[str]:
    """Generate with exponential backoff for rate limits."""
    delay = 1.0
    
    for attempt in range(max_retries + 1):
        try:
            return model.generate_content(prompt).text
        except Exception as e:
            if '429' in str(e) and attempt < max_retries:
                print(f"⚠ Rate limit. Retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                raise
    return None

# Configure API
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# Ask questions safely
answer = generate_with_retry(model, "What is machine learning?")
print(answer)
```

### Batch Processing

```python
prompts = [
    "Write a Python function to sort a list",
    "Explain the theory of relativity",
    "Summarize the benefits of AI"
]

# Process in batches with delay to avoid rate limits
results = []
for prompt in prompts:
    result = generate_with_retry(model, prompt)
    results.append(result)
    time.sleep(1)  # Respectful delay between requests

for prompt, result in zip(prompts, results):
    print(f"Q: {prompt}\nA: {result}\n---")
```

---

## 📅 Course Schedule

<table>
<tr>
<th>Day</th>
<th>Date</th>
<th>Topic</th>
<th>Deliverables</th>
</tr>
<tr>
<td align="center">1️⃣</td>
<td>Nov 9</td>
<td><b>Introduction to AI Agents</b><br/>Fundamentals, architecture, Gemma overview</td>
<td>✅ Setup complete<br/>✅ First agent built</td>
</tr>
<tr>
<td align="center">2️⃣</td>
<td>Nov 10</td>
<td><b>Planning & Reasoning</b><br/>Agent planning, multi-step tasks</td>
<td>📝 Livestream notes<br/>💻 Planning agent</td>
</tr>
<tr>
<td align="center">3️⃣</td>
<td>Nov 11</td>
<td><b>Tool Integration</b><br/>Function calling, external APIs</td>
<td>🔧 Tool-enabled agent<br/>📊 API integration</td>
</tr>
<tr>
<td align="center">4️⃣</td>
<td>Nov 12</td>
<td><b>Memory & State</b><br/>Conversation history, context management</td>
<td>🧠 Memory-enabled agent<br/>💾 State persistence</td>
</tr>
<tr>
<td align="center">5️⃣</td>
<td>Nov 13</td>
<td><b>Capstone Project</b><br/>Build comprehensive AI agent</td>
<td>🎯 Final project<br/>🏆 Kaggle badge</td>
</tr>
</table>

**Live Sessions**: Monday-Friday, 11 AM PT / 8 PM CET / 12:30 AM IST  
**Platform**: YouTube → [Kaggle Channel](https://www.youtube.com/kaggle)

---

## 🛡️ API Best Practices

### Rate Limit Management

```python
# ✅ DO: Implement exponential backoff
def generate_with_retry(model, prompt, max_retries=3, initial_delay=1.0):
    delay = initial_delay
    for attempt in range(max_retries + 1):
        try:
            return model.generate_content(prompt).text
        except Exception as e:
            if '429' in str(e) and attempt < max_retries:
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                raise

# ❌ DON'T: Rapid-fire requests without delay
for prompt in prompts:
    model.generate_content(prompt)  # Will hit rate limits!
```

### Error Handling

| Error Code | Meaning | Solution |
|------------|---------|----------|
| **429** | Rate limit exceeded | Use retry logic with exponential backoff |
| **404** | Model not found | Update to current model name (e.g., `gemini-2.0-flash`) |
| **400** | Invalid request | Check prompt format and parameters |
| **401/403** | Authentication failed | Verify API key in `.env` file |

### Security Best Practices

```python
# ✅ DO: Use environment variables
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

# ❌ DON'T: Hardcode API keys
api_key = "AIza..."  # NEVER DO THIS!
```

---

## 📊 Model Performance

### Gemma 1.1 Instruct 2B Benchmarks

| Task | Benchmark | Score | Interpretation |
|------|-----------|-------|----------------|
| **General Knowledge** | MMLU (5-shot) | 42.3 | College-level comprehension |
| **Commonsense Reasoning** | HellaSwag (0-shot) | 71.4 | Strong contextual understanding |
| **Physical Reasoning** | PIQA (0-shot) | 77.3 | Excellent physical intuition |
| **Code Generation** | HumanEval (pass@1) | 22.0 | Basic programming tasks |
| **Math Problem Solving** | GSM8K (maj@1) | 17.7 | Elementary mathematics |

### Model Comparison

```text
Gemma 2B vs. 7B Trade-offs:

Gemma 2B (Recommended for this course)
├── ✅ Runs on consumer hardware (8GB RAM)
├── ✅ Faster inference
├── ✅ Lower costs
└── ⚠️ Slightly lower accuracy

Gemma 7B (For production workloads)
├── ✅ Higher accuracy (64.3 MMLU)
├── ✅ Better at complex tasks
├── ⚠️ Requires 28GB+ RAM
└── ⚠️ Slower inference
```

---

## 📚 Resources

### Official Documentation
- 📖 [Gemma Model Card](https://ai.google.dev/gemma) - Official specifications
- 🧪 [Keras Hub Docs](https://keras.io/keras_hub/) - API reference
- 🏛️ [Kaggle Models](https://www.kaggle.com/models/google/gemma) - Pre-trained weights
- 🛡️ [Responsible AI Toolkit](https://ai.google.dev/responsible) - Safety guidelines

### Course Materials
- 🎓 [Kaggle Course Page](https://www.kaggle.com) - Daily assignments
- 💬 [Kaggle Discord](https://discord.gg/kaggle) - Community support
- 📺 [YouTube Livestreams](https://www.youtube.com/kaggle) - Daily sessions
- 📝 [Course Info](COURSE_INFO.md) - Detailed schedule

### Community & Support
- **Discord Channels**:
  - `#5dgai-announcements` - Official updates
  - `#5dgai-question-forum` - Technical Q&A
  - `#5dgai-general-chat` - Discussion
- **GitHub**: [Issues & Discussions](https://github.com/StrayDogSyn/Gemma_Kaggle_Notebook/issues)

---

## 🤝 Contributing

This is a personal learning repository, but feedback and suggestions are welcome!

### Ways to Contribute
1. 🐛 **Report Issues**: Found a bug? [Open an issue](https://github.com/StrayDogSyn/Gemma_Kaggle_Notebook/issues)
2. 💡 **Suggestions**: Have ideas? Start a discussion
3. 📖 **Documentation**: Improvements to docs always appreciated
4. ⭐ **Star**: If this helped you, consider starring the repo!

### Development Setup

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/Gemma_Kaggle_Notebook.git

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push and create PR
git push origin feature/amazing-feature
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses
- **Gemma Models**: [Gemma Terms of Use](https://ai.google.dev/gemma/terms)
- **Keras**: Apache License 2.0
- **JAX**: Apache License 2.0

---

## 🙏 Acknowledgments

<table>
<tr>
<td width="60%">

### Course Team
- **Instructors**: Kanchana Patlolla, Anant Nawalgaria
- **Organization**: Google & Kaggle
- **Community**: 1000+ participants worldwide

### Technology
- **Google AI Team** - For creating Gemma
- **Keras Team** - For the multi-backend framework
- **JAX Team** - For high-performance computing

</td>
<td width="40%">

### My Learning Journey
- 🎯 **Goal**: Master AI agent development
- 📚 **Focus**: Production-ready implementations
- 🌱 **Growth**: From fundamentals to advanced
- 🤝 **Community**: Active learning and sharing

*This represents a significant milestone in my AI/ML learning path.*

</td>
</tr>
</table>

---

## 📈 Progress Tracker

```text
Course Progress: [▓▓▓▓▓▓▓░░░] 70% Setup Complete

✅ Environment configured
✅ API keys obtained
✅ Notebooks created
✅ Documentation complete
⏳ Day 1 (Nov 9) - Ready to start
⏳ Day 2-5 - Upcoming
⏳ Capstone project - Planned
```

### Next Steps
1. ✅ Complete `setup.ipynb` verification
2. ⏳ Join Discord and introduce myself
3. ⏳ Phone verify Kaggle account
4. ⏳ Review Day 1 materials (Nov 9)
5. ⏳ Prepare questions for live session

---

<div align="center">

### 🌟 Star this repo if you find it helpful!

**Built with ❤️ during the 5-Day AI Agents Intensive Course**

[![GitHub stars](https://img.shields.io/github/stars/StrayDogSyn/Gemma_Kaggle_Notebook?style=social)](https://github.com/StrayDogSyn/Gemma_Kaggle_Notebook)
[![GitHub forks](https://img.shields.io/github/forks/StrayDogSyn/Gemma_Kaggle_Notebook?style=social)](https://github.com/StrayDogSyn/Gemma_Kaggle_Notebook/fork)

[⬆ Back to Top](#-ai-agents-intensive-course)

</div>
