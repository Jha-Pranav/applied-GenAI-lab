# System Architecture

## 🏗️ Unified Agent Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    BUDDY AI ASSISTANT                          │
├─────────────────────────────────────────────────────────────────┤
│  main.py → agentic/client.py (BuddyClient)                     │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ SINGLE AGENT    │  │ INTELLIGENT     │  │ TOOL            │ │
│  │ ARCHITECTURE    │  │ ROUTING         │  │ ECOSYSTEM       │ │
│  │                 │  │                 │  │                 │ │
│  │ • Unified Agent │  │ • Direct Tools  │  │ • 6 Core Tools  │ │
│  │ • Smart Routing │  │ • Debate Agent  │  │ • 2 AI Agents   │ │
│  │ • Tool Manager  │  │ • Task Planner  │  │ • Streaming     │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                    EXECUTION FLOW                          │ │
│  │                                                             │ │
│  │  Request → Agent → Routing Decision → Tool/Agent Selection │ │
│  │     ↓                                                       │ │
│  │  Simple: Direct tool usage (fs_read, execute_bash, etc.)   │ │
│  │  Comparison: Route to DebateAgent for analysis             │ │
│  │  Complex: Route to TaskPlanner for project execution       │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## 🔄 Execution Flow

### High-Level Flow Summary
1. **Request Processing** → Single Agent receives user request
2. **Intelligent Routing** → Agent analyzes request and selects appropriate approach:
   - **Simple tasks** → Direct tool usage (fs_read, fs_write, execute_bash, code_interpreter)
   - **Comparison questions** → Route to debate tool for multi-perspective analysis
   - **Complex projects** → Route to planner tool for task breakdown and execution
3. **Streaming Execution** → Real-time response with thinking process visibility
4. **Result Display** → Clean output without duplicate content

### 🧠 Core Capabilities

#### 1. Intelligent Request Analysis
The system automatically analyzes request type and routes to appropriate execution strategies:
- **Simple**: Direct tool execution
- **Comparison**: Multi-perspective debate analysis  
- **Complex**: Planning with tool coordination

#### 2. Comprehensive Tool Ecosystem
- **File System Tools**: Advanced file discovery and intelligent operations with Git integration
- **Execution Tools**: Secure shell command execution and safe Python code interpretation
- **Intelligence Tools**: Multi-agent debate analysis and intelligent task planning

#### 3. Single-Agent Coordination
- **Unified Architecture**: One Agent handles all routing decisions
- **Tool Integration**: Seamless access to all tools through ToolManager
- **Streaming Output**: Real-time response with thinking process visibility
