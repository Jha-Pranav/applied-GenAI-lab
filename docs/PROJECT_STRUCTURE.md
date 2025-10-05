# Project Structure

## 🏗️ Directory Layout

```
applied-GenAI-lab/
├── main.py                     # Entry point
├── agentic/                    # Core system
│   ├── client.py              # BuddyClient (main orchestrator)
│   ├── core/
│   │   └── agent.py           # Core Agent implementation
│   ├── agent/                 # AI Agents
│   │   ├── debater.py         # Multi-perspective debate agent
│   │   └── planner/           # Task planning system
│   │       ├── main.py        # Planner entry point
│   │       ├── executor.py    # Task execution coordinator
│   │       ├── task_generator.py # Task generation engine
│   │       ├── validation.py  # Pre-execution validation
│   │       └── models.py      # Data models
│   ├── tools/                 # Tool ecosystem
│   │   ├── manager.py         # Tool registry and execution
│   │   ├── fs_read.py         # File system reading
│   │   ├── fs_write.py        # File system writing
│   │   ├── execute_bash.py    # Shell command execution
│   │   ├── code_interpreter.py # Python code execution
│   │   ├── debate.py          # Debate tool wrapper
│   │   └── planner.py         # Planning tool wrapper
│   ├── configs/               # Configuration management
│   │   ├── config.toml        # Main configuration
│   │   ├── loader.py          # Config loading
│   │   └── prompts.py         # System prompts
│   └── llms/                  # LLM integration
│       └── client.py          # OpenAI-compatible client
├── docs/                      # Documentation
│   ├── ARCHITECTURE.md        # System architecture
│   ├── AGENTS_AND_TOOLS.md    # Agents and tools reference
│   ├── USAGE.md              # Usage guide and examples
│   ├── CONFIGURATION.md       # Configuration options
│   └── PROJECT_STRUCTURE.md   # This file
├── task_analyzer/             # Standalone task analyzer
│   ├── main.py               # Task analysis entry point
│   └── README_TECHNICAL.md   # Technical documentation
└── benchmark/                # Performance benchmarks
    └── test_prompts.md       # Test scenarios
```

## 📁 Key Components

### Core System (`agentic/`)
- **`client.py`**: Main BuddyClient orchestrator with intelligent routing
- **`core/agent.py`**: Core Agent implementation with tool management
- **`configs/`**: Configuration management and system prompts

### Agents (`agentic/agent/`)
- **`debater.py`**: Multi-perspective debate analysis
- **`planner/`**: Intelligent task planning and execution system

### Tools (`agentic/tools/`)
- **File System**: `fs_read.py`, `fs_write.py`
- **Execution**: `execute_bash.py`, `code_interpreter.py`
- **Intelligence**: `debate.py`, `planner.py`
- **Management**: `manager.py` (tool registry)

### Documentation (`docs/`)
- Comprehensive documentation split into focused files
- Architecture diagrams and flow explanations
- Usage examples and configuration guides
