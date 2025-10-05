# Agents and Tools

## 🤖 Current System Components

### 🎯 Core Agent (1 Active)

#### **BuddyAgent** (`agentic/client.py`)
- **Purpose**: Unified AI assistant with intelligent routing capabilities
- **Capabilities**: 
  - Automatic request analysis and routing decisions
  - Direct tool usage for simple tasks (file operations, code execution)
  - Intelligent routing to specialized agents for complex analysis
  - Real-time streaming responses with thinking process
- **Routing Logic**: 
  - **Simple tasks** → Direct tool usage
  - **Comparison questions** → Route to DebateAgent
  - **Complex projects** → Route to TaskPlanner
- **Model**: Qwen 3:14B with streaming output

### 🎯 Specialized Agents (2 Active)

#### 1. **DebateAgent** (`agentic/agent/debater.py`)
- **Purpose**: Multi-perspective analysis and structured decision making
- **Capabilities**: 
  - Creates 4 specialized agents (Advocate, Critic, Expert, Moderator)
  - Conducts structured debates with opening statements and rebuttals
  - Provides balanced recommendations with evidence-based analysis
- **Use Cases**: "Which is better" questions, pros/cons analysis, decision support
- **Model**: Qwen 3:8B with streaming output

#### 2. **TaskPlanner** (`agentic/agent/planner/`)
- **Purpose**: Intelligent task breakdown and execution planning
- **Capabilities**:
  - Project complexity analysis and framework selection
  - Hierarchical task decomposition with dependencies
  - Pre/post-execution validation with feedback loops
  - Caching system for performance optimization
- **Components**: 
  - `main.py` - Orchestration layer
  - `executor.py` - Task execution coordinator
  - `task_generator.py` - LLM-powered task creation
  - `validation.py` - Quality assurance system
- **Model**: Qwen 3:14B with advanced reasoning

### 🛠️ Core Tools (6 Active)

#### File System Tools
1. **`fs_read`** - Advanced file discovery with Git integration and fuzzy matching
2. **`fs_write`** - Intelligent file operations with diff preview and validation

#### Execution Tools  
3. **`execute_bash`** - Secure shell command execution with environment control
4. **`code_interpreter`** - Safe Python code execution with output capture

#### Intelligence Tools
5. **`debate`** - Tool wrapper for DebateAgent with streaming support
6. **`planner`** - Tool wrapper for TaskPlanner with caching
