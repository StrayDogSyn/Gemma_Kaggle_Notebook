# Day 1 Quick Start Guide

**⏱️ Time**: 90 minutes - 4 hours  
**📊 Difficulty**: Beginner to Intermediate  
**🎯 Goal**: Understand and implement AI agents

---

## 🚀 Quick Navigation

1. **Theory** → Read `DAY1_CONCEPTS.md` (30 min)
2. **Practice** → Run `ai_agents_course.ipynb` Examples 1-4 (45 min)
3. **Apply** → Complete Exercises 1-3 (60+ min)
4. **Debug** → Review debugging section (15 min)
5. **Reflect** → Fill in notes and checklist (10 min)

---

## 📚 What You'll Build Today

### 4 Working Examples
1. **SimpleAgent** - Basic agent loop (perceive/plan/act/evaluate)
2. **ContextAwareAgent** - Agent with memory and personalization
3. **SelfEvaluatingAgent** - Agent that improves its own responses
4. **LLM vs Agent** - Side-by-side comparison showing the difference

### 3 Exercises
1. **MovieAgent** (Beginner) - Recommendation system with preferences
2. **StudyBuddy** (Intermediate) - Multi-step planning and adaptation
3. **CodeAgent** (Advanced) - Self-correcting code generation

### 3 Debugging Patterns
1. Fix memory loss between calls
2. Add error handling with retries
3. Implement bounded memory management

---

## ⚡ Speed Run (90 minutes)

### Phase 1: Understand (20 min)
- Skim `DAY1_CONCEPTS.md` - focus on examples
- Read the Movie Director analogy
- Understand the 5 components diagram

### Phase 2: Run Examples (30 min)
- Open `ai_agents_course.ipynb`
- Run Examples 1-4 in order
- Observe outputs, note key differences

### Phase 3: Exercise 1 (25 min)
- Try implementing MovieAgent yourself (15 min)
- Compare with solution (10 min)

### Phase 4: Debug & Review (15 min)
- Run all 3 debugging examples
- Review best practices checklist
- Identify which apply to your code

---

## 🎓 Deep Dive (4 hours)

### Session 1: Theory (60 min)
- Read all of `DAY1_CONCEPTS.md` thoroughly
- Take notes on each component
- Understand all code examples
- Review agent types taxonomy

### Session 2: Examples (60 min)
- Run Example 1, modify and experiment
- Run Example 2, test with different inputs
- Run Example 3, observe evaluation process
- Run Example 4, understand memory difference

### Session 3: Exercises (90 min)
- Complete Exercise 1 fully (30 min)
- Attempt Exercise 2 (40 min)
- Challenge yourself with Exercise 3 (20 min)

### Session 4: Mastery (30 min)
- Review debugging section
- Complete best practices checklist
- Fill in all notes sections
- Prepare questions for livestream

---

## ✅ Success Criteria

You've completed Day 1 successfully if you can:

### Explain
- [ ] What makes something an "agent" vs just an LLM
- [ ] The 5 core components of an agent
- [ ] When to use agents vs simple LLM calls
- [ ] Why memory management matters

### Implement
- [ ] A basic agent with the 5 components
- [ ] Conversation history tracking
- [ ] Context-aware responses
- [ ] Basic error handling

### Debug
- [ ] Identify when agent has no memory
- [ ] Add retry logic for API calls
- [ ] Implement bounded memory
- [ ] Trace agent execution

---

## 🔗 Key Concepts Reference

### The Agent Loop
```
PERCEIVE → PLAN → ACT → EVALUATE → RESPOND
    ↑                                   ↓
    └─────────── (if not good) ────────┘
```

### Core Components

**1. Perception**: Gather information
```python
def perceive(self, user_message):
    return {
        "message": user_message,
        "history": self.conversation_history,
        "context": self.user_profile
    }
```

**2. Planning**: Decide actions
```python
def plan(self, perception):
    if "question" in perception["message"]:
        return ["search", "formulate_answer"]
    else:
        return ["acknowledge", "clarify"]
```

**3. Action**: Execute plan
```python
def act(self, plan):
    results = []
    for action in plan:
        result = self.execute(action)
        results.append(result)
    return results
```

**4. Evaluation**: Check quality
```python
def evaluate(self, response):
    if len(response) < 10:
        return {"quality": "poor"}
    return {"quality": "good"}
```

**5. Memory**: Remember context
```python
def remember(self, user_msg, agent_response):
    self.history.append({"user": user_msg, "agent": agent_response})
    if len(self.history) > 50:
        self.history = self.history[-50:]  # Keep bounded
```

---

## 🐛 Common Issues Quick Fix

| Problem | Quick Fix |
|---------|-----------|
| Agent forgets previous messages | Add `self.history = []` and store conversations |
| API call fails | Wrap in try/except with retry logic |
| Memory grows too large | Implement max size: `history[-50:]` |
| Responses are generic | Add user context to prompts |
| Agent doesn't improve | Add evaluation and improvement loop |
| Code is hard to test | Separate components (perceive/plan/act) |

---

## 📊 Learning Progression

```
Beginner → Intermediate → Advanced
   ↓            ↓             ↓
Example 1   Example 2    Example 3
   +            +            +
Exercise 1  Exercise 2   Exercise 3
```

**Where to start**: 
- New to agents? Start with Example 1
- Some experience? Jump to Example 2
- Want a challenge? Go straight to Exercise 2

---

## 🎯 What to Do Next

### Immediate (Today)
1. ✅ Complete at least Examples 1-2
2. ✅ Attempt Exercise 1
3. ✅ Review debugging section
4. ✅ Fill in notes

### Before Day 2
1. ✅ Finish all examples
2. ✅ Complete Exercise 1 solution
3. ✅ Attempt Exercises 2-3
4. ✅ Review best practices checklist
5. ✅ Prepare questions for livestream

### Optional Deep Dive
1. 📖 Read ReAct paper
2. 🔍 Explore LangChain agents
3. 💬 Share learnings on Discord
4. 🛠️ Build your own agent variation

---

## 💡 Pro Tips

### For Your Learning Style

**If you like theory first**:
→ Read `DAY1_CONCEPTS.md` completely before coding

**If you learn by doing**:
→ Run examples first, then read theory

**If you learn by teaching**:
→ Explain each concept to rubber duck/friend

**If you like visual learning**:
→ Draw the agent loop diagram yourself

### Time Management

**30-minute session**:
- Run Example 1 only
- Understand the basic loop
- Come back later for more

**1-hour session**:
- Examples 1-2
- Exercise 1 attempt
- Quick debugging review

**2-hour session**:
- All examples
- Exercise 1 complete
- Exercise 2 started
- Full debugging section

**4-hour session**:
- Theory + all examples
- All exercises attempted
- Complete documentation
- Ready for Day 2

---

## 📞 Getting Help

### Stuck on Concepts?
1. Re-read the Movie Director analogy
2. Review the LLM vs Agent comparison
3. Check Discord #5dgai-question-forum

### Code Not Working?
1. Check debugging section in notebook
2. Verify GOOGLE_API_KEY is set
3. Run cells in order from top
4. Restart kernel if needed

### Need Inspiration?
1. Look at the working examples
2. Compare your code to solutions
3. Ask for code review on Discord

---

## 🏆 Completion Milestone

### You're ready for Day 2 when you can:
- ✅ Explain agents to a friend
- ✅ Build a simple agent from scratch
- ✅ Add memory to any LLM call
- ✅ Debug common agent issues
- ✅ Complete Exercise 1 independently

---

**Ready to start? Open `ai_agents_course.ipynb` and run Example 1!** 🚀

**Questions? Check Discord #5dgai-question-forum** 💬

**Want more theory? Read `DAY1_CONCEPTS.md`** 📚
