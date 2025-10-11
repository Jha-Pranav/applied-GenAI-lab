

# 🧑‍💻 Buddy: Autonomous Software Engineering Agent

🚀 **Build software autonomously with AI** — Buddy is an edge-ready agent that handles coding, testing, deployment, and more, powered by efficient, smaller models.

---

### 🌟 Why Buddy?

Buddy is not just another AI project—it's a **starting point for learning agentic solutions** without getting lost in the hype of complex frameworks like `langX` or other SDKs.
Built **entirely in Python with no external frameworks**, Buddy offers a minimal yet powerful foundation for understanding and building autonomous agents.

---


### 🔗 See It in Action

Explore task traces (from simple to complex) on **[Weights & Biases](https://wandb.ai/pranav_jha/buddy-agent-project/weave/traces?view=traces_default)**.

> ⚠️ **Note**: These traces may be outdated. Features have been significantly enhanced.
> For the latest experience, **run the project locally** to witness the magic.

---

## 📖 Overview

**Buddy** is an autonomous AI agent designed to act as your **personal software engineer**, managing the full development lifecycle: **requirement gathering**, **implementation**, **testing**, **deployment**, **monitoring**, and **productization at scale**. 

Inspired by innovations like **Amazon Q** and advancements in AI reasoning , Buddy enables **local-first, low-latency, and private** AI assistance on consumer-grade CPUs/GPUs, eliminating cloud dependency.

---
🎥 Live Demo: Try Buddy yourself
![alt text](image.png)


## 💡 Why Buddy?

Think of Buddy as your **AI-powered intern or junior developer** that:

- Understands plain-language requirements
- Implements and tests features
- Debugs and fixes issues
- Writes, commits, and optionally deploys code
- Collaborates in a multi-agent ecosystem

Just **ask Buddy in the terminal**, and it autonomously handles tasks, from bug fixes to building frameworks, aligning with the rise of **experience-driven agents** with memory, self-reflection, and task planning [2].

---

## 🎯 Project Vision

### Goal
To showcase **powerful agentic AI systems** running efficiently on local machines, enabling **fully autonomous software development workflows** without heavy cloud infrastructure, inspired by scalable autonomy research [1].

### Key Features
- **🤖 Autonomous Task Execution**: Manages planning → coding → testing → deployment.
- **🧠 Intelligent Decision-Making**: Multi-agent reasoning for architectural and technical choices.
- **⚡ Edge-Ready AI**: Lightweight models (e.g., Phi, Gemma, Mistral) for consumer hardware.
- **🔧 Tool-Based Architecture**: Modular tools with intelligent coordination (inspired by Toolformer).
- **📊 Future Roadmap**: Tool-augmented reinforcement learning for continual improvement [1].

### Research Objectives
1. Enhance **multi-agent coordination** architectures.
2. Advance **tool-based learning** with plug-and-play AI tools.
3. Optimize **edge deployment** for real-world software engineering.
4. Develop a **reinforcement learning framework** with dynamic memory and tools.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    BUDDY AI ASSISTANT                       │
├─────────────────────────────────────────────────────────────┤
│ main.py → agentic/frontend/client.py (BuddyClient)          │
│                                                            │
│ ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ │
│ │ COMPLEXITY      │ │ REQUEST         │ │ TOOL            │ │
│ │ ANALYSIS        │ │ ROUTING         │ │ COORDINATION    │ │
│ │ • Simple        │ │ • Direct Tool   │ │ • 6 Core Tools  │ │
│ │ • Moderate      │ │ • Planning      │ │ • 2 AI Agents   │ │
│ │ • Complex       │ │ • Debate        │ │ • Streaming     │ │
│ └─────────────────┘ └─────────────────┘ └─────────────────┘ │
│                                                            │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │                 AGENT ECOSYSTEM                         │ │
│ │  🎯 DebateAgent   📋 TaskPlanner   🔍 Introspection     │ │
│ │  Multi-perspective Intelligent     Self-reflection     │ │
│ │  analysis         task breakdown   & validation        │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## ✅ Use Cases

- **"Add a new feature"**: Describe it in plain text, and Buddy plans, implements, and tests it.
- **"Fix a bug"**: Share an error trace or describe the issue, and Buddy patches and validates it.
- **"Build a framework or microservice"**: Specify goals, and Buddy handles the implementation while you focus on high-level design.

---

## 🚀 Getting Started

### Installation
1. **Install Ollama**  
   Follow instructions on the [official Ollama website](https://ollama.com/download) for your OS.

2. **Pull the Reasoning Model**  
   ```bash
   ollama pull <reasoning-model>
   ```

3. **Install uv**  
   Use `uv`, a fast Python package manager:
   ```bash
   pip install uv
   ```

4. **Clone and Set Up the Repository**  
   ```bash
   git clone https://github.com/Jha-Pranav/applied-GenAI-lab.git
   cd applied-GenAI-lab
   uv sync
   ```
Configure Buddy in `agentic/configs/config.toml`:

```toml
[model]
name = "qwen3:14b"
url = "http://localhost:11434/v1"
api_key = "ollama"
```

5. **Run Buddy**  
   ```bash
   uv run main.py
   # or simply run `buddy` in the terminal from the project root
   ```

---



## 📚 Documentation


### 🧰 Tools

| Tool | Description |
|------|-------------|
| [Core](nbs/buddy/backend/tools/core/README.md) | Base toolset used by the agent for coordination and routing |
| [File System](nbs/buddy/backend/tools/filesystem/README.md) | Read/write operations, file handling, and project updates |
| [Intelligence](nbs/buddy/backend/tools/intelligence/README.md) | Tooling for LLM interaction, summarization, and response generation |
| [Planner](nbs/buddy/backend/tools/planner/README.md) | Task planning, breakdown, and execution preparation |
| [System](nbs/buddy/backend/tools/system/README.md) | Shell command execution and system-level operations |
| [Analysis](nbs/buddy/backend/tools/analysis/README.md) | Code analysis, introspection, and validation |
| [Utilities](nbs/buddy/backend/tools/utilities/README.md) | Support tools for logging, config management, and helpers |

### Project 

| Topic | Description |
|-------|-------------|
| [Architecture](docs/ARCHITECTURE.md) | System design, execution flow, and core capabilities |
 [Execution Flow](docs/Execution_Flow_Diagram.md) | Complete Execution Flow Diagram |
| [Agents & Tools](docs/AGENTS_AND_TOOLS.md) | Details on BuddyAgent, DebateAgent, TaskPlanner, and tools |
| [Usage Guide](docs/USAGE.md) | Examples, features, and advanced usage patterns |
| [Configuration](docs/CONFIGURATION.md) | Setup options, custom tools, and performance monitoring |
| [Project Structure](docs/PROJECT_STRUCTURE.md) | Directory layout and component organization |

---
### ⚠️ Project Status

This project is under **active development**.
You may encounter bugs—**contributions are welcome and encouraged**!

📊 **Benchmarking results** will be shared soon. Expect ongoing improvements and new features.

---

## 🤖 Core Components

- **🎯 BuddyAgent**: Central orchestrator with intelligent request routing.
- **🛠️ 6 Core Tools**: File system, execution, and intelligence tools for task execution.
- **🧠 2 Specialized Agents**: 
  - **DebateAgent**: Multi-perspective analysis.
  - **TaskPlanner**: Intelligent task breakdown for complex projects.
- **⚡ Real-time Streaming**: Live responses with visible thinking processes.


## ❤️ Built for Developers

Buddy empowers developers with **intelligent automation** for complex technical tasks, running efficiently on the edge.

*Empowering the future of software engineering with AI-driven assistance.*

---
