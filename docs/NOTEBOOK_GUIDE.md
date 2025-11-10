# AI Agents Course Notebook - User Guide

**Last Updated**: November 9, 2025

## 📖 Overview

This notebook is your comprehensive companion for the **5-Day AI Agents Intensive Course** (Nov 9-13, 2025). It's designed for professional learning with maximum readability and organization.

## 🎯 Notebook Philosophy

- **Primary Platform**: Complete all codelabs on **Kaggle** (fully pre-configured environment)
- **This Notebook**: Use for documentation, notes, and local Gemini API experiments
- **Focus**: One day at a time - current focus is **Day 1** with clean templates for Days 2-5

## 📚 Notebook Structure (32 Cells)

### Setup Section (Cells 1-9)
**Purpose**: Configure your local environment for experimentation

| Cell | Type | Purpose | Status |
|------|------|---------|--------|
| 1 | Markdown | Course title and overview | ✅ |
| 2 | Markdown | Platform options and setup notes | ✅ |
| 3 | Python | Check Python version compatibility | ✅ Executed |
| 4 | Python | Install packages (google-generativeai, python-dotenv) | ✅ Executed |
| 5 | Python | Import libraries with graceful error handling | ✅ Executed |
| 6 | Markdown | API configuration section header | ✅ |
| 7 | Python | Load GOOGLE_API_KEY from Kaggle or .env | ✅ Executed |
| 8 | Markdown | Gemma vs Gemini explanation | ✅ |
| 9 | Python | Initialize Gemini Pro model | ✅ Executed |

**Key Variables Initialized**:
- `GOOGLE_API_KEY`: Your API key for Gemini
- `model`: Gemini Pro GenerativeModel instance

---

### Day 1 Section (Cells 10-15)

#### Cell 10: Day 1 Overview & Assignments
**Content**:
- Learning materials checklist (podcast, whitepaper)
- Kaggle codelabs overview
- Livestream information (Nov 10, 11:00 AM PT)
- Learning objectives

#### Cell 11: Consolidated Learning Notes
**Comprehensive sections for**:
- 🎧 **Podcast Notes**: Key topics, concepts, insights, questions
- 📖 **Whitepaper**: Detailed notes on all 3 main sections:
  - Taxonomy of Agent Capabilities
  - Agent Ops Discipline  
  - Interoperability & Security
- 💻 **Codelab 1**: First agent with Gemini + ADK
  - What you built
  - Key concepts learned
  - Code snippets from Kaggle
  - Challenges and solutions
- 👥 **Codelab 2**: Multi-agent systems
  - System architecture
  - Architectural patterns explored
  - Code snippets from Kaggle
  - Key learnings

#### Cell 12: Experiment 1 - Simple Conversational Agent
**Purpose**: Test basic agent concepts with Gemini API  
**Status**: ✅ Executed successfully  
**What it does**: Demonstrates simple prompt-response agent pattern

#### Cell 13: Experiment 2 - Context-Aware Agent
**Purpose**: Agent that maintains conversation history  
**Status**: ✅ Executed successfully  
**What it does**: Shows how to build context across multiple turns

#### Cell 14: Day 1 Summary & Reflection
**Comprehensive sections**:
- ✅ Completion checklist (learning, codelabs, documentation)
- 💡 Key insights and learnings (5 reflection prompts)
- 🤔 Questions for livestream (submit on Discord!)
- 🚀 Project ideas inspired by Day 1
- 📅 Preparation for Day 2

#### Cell 15: Experiment 3 - Custom Agent Playground
**Purpose**: Open experimentation space  
**Use for**: Testing your own agent ideas inspired by Day 1

---

### Days 2-5 Templates (Cells 16-31)

Each future day follows a clean, consistent structure:

#### Day 2 (Cells 16-18)
- **Cell 16**: Overview and learning objectives (to be filled)
- **Cell 17**: Learning materials notes template
- **Cell 18**: Local experiments code cell

#### Day 3 (Cells 19-22)
- Clean 4-cell template ready for content

#### Day 4 (Cells 23-26)
- Clean 4-cell template ready for content

#### Day 5 - Capstone (Cells 27-31)
- **Cell 27**: Project overview
- **Cell 28**: Detailed project planning template
- **Cell 29**: Implementation code cell
- **Cell 30**: Testing code cell
- **Cell 31**: Complete course reflection with comprehensive prompts

### Resources Section (Cell 32)
- Links to course materials
- Documentation references
- Tools and platforms

---

## 🚀 How to Use This Notebook

### Daily Workflow

**1. Start Each Day**
- Read the day's overview cell
- Complete materials on Kaggle platform
- Return here to document learnings

**2. During Learning**
- Take notes in the learning materials section
- Copy interesting code snippets from Kaggle
- Document challenges and solutions

**3. Local Experimentation**
- Use the experiment cells to test ideas
- Try variations of what you learned
- Build on previous experiments

**4. End of Day**
- Complete the summary & reflection section
- Prepare questions for livestream/Discord
- Check off completed items

---

## ✅ Day 1 Completion Checklist

### Setup (Complete!)
- [x] Python environment configured
- [x] google-generativeai installed
- [x] GOOGLE_API_KEY configured
- [x] Gemini Pro model initialized
- [x] Experiment cells tested and working

### Learning Materials
- [ ] Listened to podcast (~50 min)
- [ ] Read whitepaper (1-2 hours)
- [ ] Documented notes in Cell 11

### Hands-On Practice
- [ ] Completed Codelab 1 on Kaggle
- [ ] Completed Codelab 2 on Kaggle
- [ ] Copied code snippets to notebook
- [ ] Ran local experiments (Cells 12-15)

### Reflection & Preparation
- [ ] Completed Day 1 summary (Cell 14)
- [ ] Prepared questions for livestream
- [ ] Ready for Day 2 (Nov 10, 11:00 AM PT)

---

## 💡 Best Practices

### Documentation
- **Be specific**: Write detailed notes about what you learned
- **Include context**: Why is this concept important?
- **Ask questions**: Note things you don't understand yet
- **Link concepts**: Connect ideas across different materials

### Code Snippets
- **Add comments**: Explain what the code does
- **Note source**: Which codelab did this come from?
- **Adapt locally**: Try running variations with Gemini API
- **Track changes**: Document what you modified and why

### Experimentation
- **Start simple**: Build on working examples
- **Test incrementally**: Verify each change works
- **Document errors**: Note what didn't work and why
- **Share learnings**: Prepare insights for Discord community

### Time Management
- **Focus on quality**: Better to deeply understand fewer concepts
- **Take breaks**: Intensive learning requires rest
- **Set boundaries**: Complete what you can, don't rush
- **Review regularly**: Look back at previous days before moving forward

---

## 🔧 Troubleshooting

### Model Not Initialized Error
**Symptom**: "name 'model' is not defined"  
**Solution**: Run Cell 9 to initialize Gemini Pro model

### API Key Issues
**Symptom**: "API key not found" or authentication errors  
**Solution**: 
1. Get API key from https://aistudio.google.com
2. Create `.env` file with `GOOGLE_API_KEY=your_key`
3. Re-run Cell 7 to reload configuration

### Import Errors
**Symptom**: Missing module errors  
**Solution**: Re-run Cell 4 to install packages

### Python 3.13 Compatibility
**Note**: Some packages (tensorflow-text) don't support Python 3.13 yet
**Solution**: Use Kaggle platform for Gemma-based codelabs

---

## 📊 Progress Tracking

### Current Status
- **Day 1**: In Progress ⏳
- **Days 2-5**: Templates Ready ✅
- **Local Setup**: Complete ✅
- **Kaggle Account**: Configured ✅

### What's Working
✅ Local Gemini API experiments  
✅ Note-taking and documentation structure  
✅ Clean templates for future days  
✅ Professional formatting and organization  

### Next Steps
1. Complete Day 1 learning materials
2. Finish both Kaggle codelabs
3. Document everything in Cell 11
4. Complete reflection in Cell 14
5. Prepare for Nov 10 livestream

---

## 🎓 Learning Goals

### Technical Skills
- Understand AI agent architecture
- Build conversational agents
- Implement multi-agent systems
- Integrate tools and APIs
- Apply best practices

### Conceptual Understanding
- Agent vs. model differences
- Planning and reasoning mechanisms
- Memory and context management
- Security and interoperability
- Agent Ops principles

### Practical Application
- Build working prototypes
- Debug and troubleshoot
- Optimize performance
- Document and share learnings
- Plan future projects

---

## 🌟 Tips for Success

1. **Complete codelabs on Kaggle**: It's the official platform with everything pre-configured
2. **Use this notebook for notes**: Keep all learning organized in one place
3. **Experiment locally**: Try variations with Gemini API
4. **Engage with community**: Ask questions on Discord
5. **Attend livestreams**: Great for Q&A and deeper insights
6. **Take your time**: Deep learning > rushing through content
7. **Build projects**: Apply concepts to real-world problems
8. **Share learnings**: Teaching others reinforces your knowledge

---

## 📞 Support Resources

- **Discord**: Course community for questions and discussion
- **Kaggle Forums**: Platform-specific technical support
- **Documentation**: Linked in Cell 32
- **Livestreams**: Live Q&A sessions with instructors

---

**Happy Learning! 🚀**

*Remember: This is an intensive course, but you've got this. Take it one day at a time, focus on understanding over speed, and enjoy the journey of learning about AI agents!*
