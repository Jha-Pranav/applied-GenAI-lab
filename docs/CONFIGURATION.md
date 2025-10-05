# Configuration

## 🔧 Configuration Options

### Model Configuration
```toml
[model]
name = "qwen3:14b"           # LLM model name
url = "http://..."           # API endpoint
temperature = 0.7            # Response creativity
max_tokens = 10000          # Response length limit
```

### Behavior Settings
```toml
[settings]
auto_approve = true         # Skip approval prompts
stream = true              # Enable streaming output
debug = false              # Debug mode
max_history = 100          # Conversation history limit
```

### Reasoning Configuration
```toml
[reasoning]
show_thinking = true        # Show AI reasoning process
max_reasoning_steps = 10    # Reasoning depth limit
retry_count = 2            # Retry failed operations
```

## 🚀 Advanced Usage

### Custom Tool Development
```python
from agentic.tools.base import BaseTool, ToolMetadata, ToolCategory

class CustomTool(BaseTool):
    def __init__(self):
        super().__init__(ToolMetadata(
            name="custom_tool",
            description="Custom functionality",
            category=ToolCategory.UTILITY
        ))
    
    def execute(self, **kwargs):
        # Custom implementation
        return {"success": True, "result": "Custom result"}
```

### Agent Integration
```python
# Use agents directly
from agentic.agent.debater import create_debate
from agentic.agent.planner.main import main as planner_main

# Structured debate
debate_result = await create_debate(
    topic="Technical decision",
    context="System architecture choice"
)

# Task planning
plan = await planner_main("Build microservices platform")
```

## 📊 Performance & Monitoring

### Built-in Metrics
- Request processing time
- Tool execution duration  
- LLM response latency
- Success/failure rates

### Debugging Support
- Detailed error logging
- Request/response tracing
- Tool execution monitoring
- Agent decision tracking
