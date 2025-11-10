# Getting Started Guide

## Welcome to the Gemma Kaggle Project!

This guide will help you get set up quickly for the 5-Day AI Agents Intensive Course.

## Step-by-Step Setup

### 1. ✅ Verify System Requirements

**Minimum Requirements:**
- Python 3.8 or higher
- 8GB RAM (16GB recommended)
- 10GB free disk space
- Internet connection for downloading models

**Check your Python version:**
```bash
python --version
```

### 2. 📦 Install Dependencies

**Option A: Install all at once (recommended)**
```bash
pip install -r requirements.txt
```

**Option B: Install core packages only**
```bash
pip install keras>=3.0.0 keras-hub jax[cpu] tensorflow
```

> **Note**: TensorFlow is required by keras-hub even when using JAX as the backend. This is due to internal dependencies in keras-hub.

**For GPU support (if available):**
```bash
pip install jax[cuda] -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
```

### 3. 🔑 Configure API Keys

1. **Get Google AI Studio API Key:**
   - Visit: https://aistudio.google.com/app/apikey
   - Create a new API key
   - Copy the key

2. **Set up environment variables:**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your API key
   # GOOGLE_API_KEY=your_actual_key_here
   ```

### 4. 📚 Verify Installation

Open and run `setup.ipynb` to verify everything is working:

```bash
jupyter notebook setup.ipynb
```

**What the setup notebook does:**
- ✓ Checks all package installations
- ✓ Verifies API key configuration
- ✓ Tests connection to Google AI
- ✓ Lists available models

### 5. 🎓 Join the Course Community

1. **Kaggle Account:**
   - Sign up at https://www.kaggle.com
   - **IMPORTANT**: Phone verify your account (required!)
   - Familiarize yourself with Kaggle Notebooks

2. **Discord:**
   - Join Kaggle Discord: https://discord.gg/kaggle
   - Link your Kaggle account: https://kaggle.com/discord/confirmation
   - Introduce yourself in `#5dgai-introductions`

3. **Course Channels:**
   - `#5dgai-announcements` - Official updates
   - `#5dgai-question-forum` - Ask questions
   - `#5dgai-general-chat` - Network with others

### 6. 🚀 Start Learning

**Day 0 (Before Nov 9):**
- ✅ Complete setup steps
- ✅ Review `GEMMA_INFO.md` for model details
- ✅ Run through `gemma_quickstart.ipynb`
- ✅ Introduce yourself on Discord

**Day 1 (Nov 9):**
- Check Kaggle for first assignment
- Review whitepaper, codelab, and podcast
- Start working in `ai_agents_course.ipynb`

**Days 2-5:**
- Attend daily livestreams (11 AM PT)
- Complete daily assignments
- Participate in Discord discussions
- Update your course notebook

## 📁 Repository Structure

```
Gemma_Kaggle_Notebook/
├── README.md                    # Project overview
├── GETTING_STARTED.md          # This file
├── COURSE_INFO.md              # Course details and schedule
├── GEMMA_INFO.md               # Technical reference
├── requirements.txt            # Python dependencies
├── .env.example                # Environment template
├── .gitignore                  # Git ignore rules
├── setup.ipynb                 # Setup verification
├── gemma_quickstart.ipynb      # Gemma model guide
└── ai_agents_course.ipynb      # Main course notebook
```

## 🧠 Understanding the Notebooks

### `setup.ipynb`
- **Purpose**: Verify your environment
- **When to use**: Run once during initial setup
- **What it does**: Tests API keys, checks packages, validates setup

### `gemma_quickstart.ipynb`
- **Purpose**: Learn Gemma model basics
- **When to use**: Before the course starts
- **What it covers**: 
  - Text generation
  - Question answering
  - Code generation
  - Fine-tuning basics

### `ai_agents_course.ipynb`
- **Purpose**: Daily course work
- **When to use**: Throughout the 5-day course
- **Structure**:
  - Day 1: Introduction to AI Agents
  - Day 2: Planning and Reasoning
  - Day 3: Tool Use and Function Calling
  - Day 4: Memory and Context
  - Day 5: Capstone Project

## 🔧 Common Setup Issues

### Issue: "ModuleNotFoundError: No module named 'keras'"
**Solution:**
```bash
pip install --upgrade keras keras-hub
```

### Issue: "ModuleNotFoundError: No module named 'tensorflow'"
**Solution:**
```bash
pip install tensorflow
```
**Note:** This error occurs when importing keras-hub because it has an internal dependency on TensorFlow, even when using JAX as the backend. Installing TensorFlow resolves this issue.

### Issue: "JAX backend not available"
**Solution:**
```bash
pip install jax[cpu]
# OR for GPU:
pip install jax[cuda] -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
```

### Issue: "API key not working"
**Solution:**
- Verify the key is correct in `.env`
- Make sure there are no quotes around the key
- Check that `.env` is in the project root directory
- Restart your Jupyter kernel

### Issue: "Model download is slow"
**Solution:**
- First download takes time (~5GB for Gemma 2B)
- Models are cached after first download
- Consider using Kaggle notebooks (models pre-cached)

### Issue: "Out of memory error"
**Solution:**
- Close other applications
- Use Gemma 2B instead of 7B
- Reduce batch size in generation
- Consider using Kaggle's free GPU/TPU

## 📖 Learning Path

### Week Before Course (Nov 2-8)
1. Complete environment setup
2. Read through `GEMMA_INFO.md`
3. Work through `gemma_quickstart.ipynb`
4. Join Discord and introduce yourself
5. Review Python and ML basics if needed

### During Course (Nov 9-13)
1. Check Kaggle daily for new assignments
2. Watch livestreams (or recordings)
3. Complete daily codelabs
4. Take notes in `ai_agents_course.ipynb`
5. Participate in Discord discussions
6. Ask questions in `#5dgai-question-forum`

### After Course (Nov 14+)
1. Complete capstone project
2. Share your work on Discord
3. Explore advanced topics
4. Build your own AI agent applications

## 💡 Pro Tips

1. **Start Early**: Don't wait until Nov 9 to set up
2. **Take Notes**: Use the provided notebook structure
3. **Ask Questions**: Discord community is there to help
4. **Experiment**: Try different prompts and parameters
5. **Share**: Post your findings and help others
6. **Backup**: Commit your work to Git regularly

## 🎯 Success Checklist

Before Day 1, make sure you have:

- [ ] Python 3.8+ installed
- [ ] All packages from `requirements.txt` installed
- [ ] Google AI Studio API key obtained and configured
- [ ] `setup.ipynb` runs without errors
- [ ] Kaggle account created and phone verified
- [ ] Discord account created and linked to Kaggle
- [ ] Introduced yourself in `#5dgai-introductions`
- [ ] Reviewed `gemma_quickstart.ipynb`
- [ ] Bookmarked course page on Kaggle
- [ ] Added livestream schedule to calendar

## 📞 Getting Help

### Technical Issues
1. Check this guide first
2. Search Discord `#5dgai-question-forum`
3. Review Gemma documentation
4. Post your question with error details

### Course Content Questions
1. Review whitepapers and codelabs
2. Ask in `#5dgai-question-forum`
3. Attend livestreams for Q&A
4. Check course announcements

### Community Support
- Discord: https://discord.gg/kaggle
- Kaggle Discussions: On course page
- YouTube: For livestream recordings

## 🌟 Ready to Begin!

Once you've completed the setup checklist, you're ready for the course!

**Next Steps:**
1. Open `ai_agents_course.ipynb`
2. Wait for Day 1 assignment (Nov 9)
3. Join the first livestream (Nov 10, 11 AM PT)
4. Start building amazing AI agents!

**Good luck and enjoy the course!** 🚀

---

*Last updated: November 7, 2025*
