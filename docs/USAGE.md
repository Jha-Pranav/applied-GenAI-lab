# Usage Guide

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone <repository-url>
cd applied-GenAI-lab

# Install dependencies
pip install -r requirements.txt

# Run the assistant
python main.py
```

## 📋 Usage Examples

### Simple Request
```bash
# Direct tool usage for simple tasks
"Read the config file and show me the database settings"
# → Agent uses fs_read tool directly
```

### Comparison Request  
```bash
# Automatic routing to debate analysis
"Which is better Python or JavaScript?"
# → Agent routes to debate tool → Multi-perspective analysis
```

### Complex Request
```bash
# Automatic routing to task planner
"Create a Python web API with 3 endpoints for user management"
# → Agent routes to planner tool → Task breakdown and execution
```

## 🔧 Advanced Features

### Streaming Output
Real-time response streaming with visual progress indicators:

```
🛠️ Executing debate (trusted)
topic: Python vs. JavaScript: which is better?

🤔 Thinking...
[Character-by-character streaming output with debate analysis]
```

### Intelligent Tool Selection
The Agent automatically selects the most appropriate tools:

```
💬 You: which framework is better argo vs flask?
🔄 Processing: which framework is better argo vs flask?
🚀 Executing with AI agent...
🛠️ Executing debate (trusted)
[Multi-agent debate with structured analysis]
```

### Conversation History
Persistent conversation history with context management:

```bash
# View conversation history
/history

# Clear conversation history  
/clear
```

## 🎯 Key Features

### ✅ Intelligent Request Analysis
- Automatic complexity detection
- Context-aware routing
- Single-step execution

### ✅ Unified Agent Architecture  
- Single Agent handles all routing decisions
- Direct tool access for simple tasks
- Intelligent routing to specialized agents
- Real-time streaming with thinking process

### ✅ Comprehensive Tool Ecosystem
- File system operations with Git integration
- Secure command execution
- Python code interpretation
- Multi-perspective debate analysis
- Intelligent task planning

### ✅ Production-Ready Features
- Streaming output with progress tracking
- Configurable approval workflows
- Error handling and retry logic
- Conversation history management
- Rich console interface

### ✅ Extensible Architecture
- Plugin-based tool system
- Configurable agent behaviors
- Custom prompt management
- Flexible LLM integration
