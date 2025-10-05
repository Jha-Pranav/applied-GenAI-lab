# Applied GenAI Lab - Autonomous Software Engineering Agent

> **🚀 Production-ready AI assistant with unified Agent architecture and intelligent routing**

## 🎯 Project Overview

### Vision: Unified AI Agent with Intelligent Routing
This project demonstrates a **production-grade AI assistant** that uses a single intelligent Agent to handle all requests through automatic routing. The system intelligently decides whether to handle requests directly with tools or route them to specialized agents (debate analysis, task planning) based on request complexity and type.

### Key Features
- ✅ **Single-step execution** - No complex multi-phase analysis
- ✅ **Intelligent tool selection** - Agent automatically chooses appropriate tools
- ✅ **Comparison analysis** - Automatic routing to debate agent for "which is better" questions
- ✅ **Complex project planning** - Automatic routing to task planner for multi-step projects
- ✅ **Streaming responses** - Real-time output without duplicate displays
- ✅ **Clean interface** - Professional console UI with progress tracking

## 🚀 Quick Start

```bash
# Clone and setup
git clone <repository-url>
cd applied-GenAI-lab
pip install -r requirements.txt

# Run the assistant
python main.py
```

## 📚 Documentation

| Topic | Description |
|-------|-------------|
| **[Architecture](docs/ARCHITECTURE.md)** | System design, execution flow, and core capabilities |
| **[Agents & Tools](docs/AGENTS_AND_TOOLS.md)** | BuddyAgent, DebateAgent, TaskPlanner, and tool ecosystem |
| **[Usage Guide](docs/USAGE.md)** | Examples, features, and advanced usage patterns |
| **[Configuration](docs/CONFIGURATION.md)** | Setup options, custom tools, and performance monitoring |
| **[Project Structure](docs/PROJECT_STRUCTURE.md)** | Directory layout and component organization |

## 🤖 Core Components

- **🎯 BuddyAgent**: Unified orchestrator with intelligent routing
- **🛠️ 6 Core Tools**: File system, execution, and intelligence tools
- **🧠 2 Specialized Agents**: DebateAgent for analysis, TaskPlanner for projects
- **⚡ Real-time Streaming**: Live responses with thinking process visibility

## 💡 Example Usage

```bash
# Simple file operation
"Read the README.md file"

# Comparison analysis  
"Which is better Python or JavaScript?"

# Complex project
"Create a REST API with authentication"
```

## 🔧 System Architecture

```
Request → BuddyAgent → Intelligent Routing
                    ↓
    Simple: Direct Tools | Comparison: Debate | Complex: Planner
```

---

**Built with ❤️ for intelligent automation**

*Empowering developers with AI-powered assistance for complex technical tasks*
