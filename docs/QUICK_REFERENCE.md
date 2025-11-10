# 5-Day AI Agents Course - Quick Reference

## 🚀 Installation (One Command)

```bash
pip install -r requirements.txt
```

Or use the automated script:
```bash
python install.py
```

## 🔑 Environment Setup

```bash
# 1. Copy template
cp .env.example .env

# 2. Edit .env and add:
GOOGLE_API_KEY=your_api_key_here

# Get key from: https://aistudio.google.com/app/apikey
```

## 📅 Course Schedule

| Day | Date | Topic | Focus |
|-----|------|-------|-------|
| 0 | Nov 9 | Setup | First assignment released |
| 1 | Nov 10 | Introduction | AI Agents basics |
| 2 | Nov 11 | Planning | Reasoning & planning |
| 3 | Nov 12 | Tools | Function calling |
| 4 | Nov 13 | Memory | Context management |
| 5 | Nov 14 | Capstone | Final project |

**Livestreams**: Daily at 11 AM PT / 8 PM CET / 12:30 AM IST

## 📖 Notebook Guide

| Notebook | Purpose | When to Use |
|----------|---------|-------------|
| `setup.ipynb` | Verify installation | Once at setup |
| `gemma_quickstart.ipynb` | Learn Gemma basics | Before course |
| `ai_agents_course.ipynb` | Daily coursework | Throughout course |

## 💻 Essential Code Snippets

### Load Gemma Model
```python
import os
os.environ['KERAS_BACKEND'] = 'jax'

import keras_hub
gemma_lm = keras_hub.models.GemmaCausalLM.from_preset("gemma_1.1_instruct_2b_en")
```

### Generate Text
```python
output = gemma_lm.generate("Your prompt here", max_length=100)
print(output)
```

### Batch Processing
```python
prompts = ["Prompt 1", "Prompt 2", "Prompt 3"]
outputs = gemma_lm.generate(prompts, max_length=100)
```

### Custom Sampling
```python
# Top-K sampling
gemma_lm.compile(sampler="top_k")
output = gemma_lm.generate("Prompt", max_length=100)

# Beam search
gemma_lm.compile(sampler=keras_hub.samplers.BeamSampler(num_beams=2))
output = gemma_lm.generate("Prompt", max_length=100)
```

### Google AI API (Alternative)
```python
import google.generativeai as genai

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Your prompt')
print(response.text)
```

## 🌐 Important Links

### Course
- **Kaggle Course**: https://www.kaggle.com
- **Discord**: https://discord.gg/kaggle
- **YouTube**: https://www.youtube.com/kaggle
- **NotebookLM**: https://notebooklm.google.com/notebook/05b7bc62-fd9e-4f0e-a83f-cc9a8ab209bf

### Documentation
- **Gemma Models**: https://www.kaggle.com/models/google/gemma
- **Keras Hub**: https://keras.io/keras_hub/
- **Google AI**: https://ai.google.dev/gemma

### Setup
- **API Key**: https://aistudio.google.com/app/apikey
- **Link Discord**: https://kaggle.com/discord/confirmation

## 📱 Discord Channels

| Channel | Purpose |
|---------|---------|
| `#5dgai-announcements` | Official updates |
| `#5dgai-introductions` | Meet participants |
| `#5dgai-question-forum` | Ask questions |
| `#5dgai-general-chat` | Discussions |

## 🔧 Common Commands

### Start Jupyter
```bash
jupyter notebook
```

### Check Python Version
```bash
python --version
```

### Install Single Package
```bash
pip install keras-hub
```

### Upgrade Package
```bash
pip install --upgrade keras
```

### List Installed Packages
```bash
pip list | grep keras
```

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Module not found | `pip install <package>` |
| API key error | Check `.env` file format |
| Out of memory | Use Gemma 2B, reduce batch size |
| Slow download | First time only (~5GB) |
| JAX not found | `pip install jax[cpu]` |

## 📊 Model Comparison

| Model | Parameters | RAM Needed | Size |
|-------|-----------|------------|------|
| Gemma 2B | 2 billion | 8GB+ | 5GB |
| Gemma 7B | 7 billion | 28GB+ | 14GB |

## 🎯 Daily Checklist

### Every Day
- [ ] Check Kaggle for new assignment
- [ ] Review whitepaper
- [ ] Complete codelab
- [ ] Listen to podcast
- [ ] Watch/attend livestream
- [ ] Take notes in `ai_agents_course.ipynb`
- [ ] Participate in Discord

## 🏆 Capstone Project Tips

1. **Start simple** - Build on basics
2. **Use templates** - Modify Day 1-4 code
3. **Test incrementally** - Verify each component
4. **Document well** - Explain your approach
5. **Share early** - Get feedback on Discord

## 💡 Agent Templates

### Simple Agent
```python
def simple_agent(prompt):
    return gemma_lm.generate(prompt, max_length=150)
```

### Planning Agent
```python
class PlanningAgent:
    def __init__(self, model):
        self.model = model
    
    def plan(self, task):
        prompt = f"Break down: {task}\nSteps:"
        return self.model.generate(prompt, max_length=200)
```

### Tool Agent
```python
class ToolAgent:
    def __init__(self, model):
        self.model = model
        self.tools = {}
    
    def register_tool(self, name, func):
        self.tools[name] = func
```

### Memory Agent
```python
class MemoryAgent:
    def __init__(self, model):
        self.model = model
        self.history = []
    
    def chat(self, message):
        self.history.append(message)
        context = "\n".join(self.history[-5:])
        return self.model.generate(context, max_length=150)
```

## 📈 Performance Tips

1. **Use JAX backend** - Fastest for Gemma
2. **Batch requests** - More efficient
3. **Limit max_length** - Only what you need
4. **Cache models** - First load is slowest
5. **Use GPU if available** - Significant speedup

## ✅ Pre-Course Checklist

- [ ] Python 3.8+ installed
- [ ] All packages installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with API key
- [ ] `setup.ipynb` runs successfully
- [ ] Kaggle account phone verified
- [ ] Discord account created and linked
- [ ] Introduced in `#5dgai-introductions`
- [ ] Reviewed `gemma_quickstart.ipynb`
- [ ] Livestream times in calendar

## 🎓 Success Metrics

By end of course, you should be able to:
- ✅ Load and use Gemma models
- ✅ Build conversational agents
- ✅ Implement planning and reasoning
- ✅ Create tool-using agents
- ✅ Add memory to agents
- ✅ Complete capstone project
- ✅ Earn Kaggle badge

## 🚨 Important Reminders

⚠️ **Phone verify Kaggle** - Required for codelabs  
⚠️ **Link Discord to Kaggle** - For full channel access  
⚠️ **Backup your work** - Commit to Git regularly  
⚠️ **Don't share API keys** - Keep .env private  
⚠️ **Start early** - Don't wait for Nov 9  

## 📞 Getting Help

1. **Search first** - Check docs and Discord
2. **Be specific** - Include error messages
3. **Share code** - Use code blocks in Discord
4. **Be patient** - Community will help

## 🎉 Ready to Start?

```bash
# 1. Install
python install.py

# 2. Configure
# Edit .env with your API key

# 3. Verify
jupyter notebook setup.ipynb

# 4. Learn
jupyter notebook gemma_quickstart.ipynb

# 5. Build
jupyter notebook ai_agents_course.ipynb
```

---

**Good luck with the course!** 🚀

*Quick Reference Card - Updated Nov 7, 2025*
