# Core Tools Infrastructure

## Overview
Foundation components for tool management, registration, and execution coordination in the Buddy AI system.

## Components

### 🏗️ manager - Tool Management System

#### Purpose
Central orchestrator for tool discovery, registration, and execution with intelligent routing capabilities.

#### Execution Flow
```
Tool Request → Tool Discovery → Parameter Validation → Execution Coordination → Result Processing
```

#### Core Responsibilities

##### 1. **Tool Registration**
```python
# Automatic tool discovery
def _register_default_tools(self):
    default_tools = [
        FsReadTool(),
        FsWriteTool(), 
        ExecuteBashTool(),
        CodeInterpreterTool(),
        DebateTool(),
        PlannerTool()
    ]
```

##### 2. **Execution Coordination**
```python
def execute_tool(self, tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute tool with validation and error handling
    
    Flow:
    1. Validate tool exists
    2. Validate parameters against schema
    3. Execute with timeout and monitoring
    4. Process and return results
    """
```

##### 3. **OpenAI Schema Generation**
```python
def get_tools(self, tool_names: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    """
    Generate OpenAI-compatible tool schemas for LLM integration
    
    Returns:
    - Function definitions
    - Parameter schemas
    - Usage descriptions
    """
```

#### Features
- **Dynamic Discovery**: Automatic tool registration
- **Schema Validation**: Parameter type checking
- **Error Handling**: Graceful failure management
- **Performance Monitoring**: Execution time tracking
- **Security**: Permission and safety validation

---

### 📋 registry - Tool Registry System

#### Purpose
Centralized registry for tool metadata, schemas, and lifecycle management.

#### Execution Flow
```
Tool Definition → Schema Generation → Registration → Validation → Availability
```

#### Registry Operations

##### 1. **Tool Registration**
```python
def register_tool(self, tool: BaseTool) -> None:
    """
    Register tool with validation and schema generation
    
    Process:
    1. Validate tool implementation
    2. Generate OpenAI schema
    3. Store metadata
    4. Enable for execution
    """
```

##### 2. **Schema Management**
```python
def get_openai_schemas(self, tool_names: Optional[List[str]] = None) -> List[Dict]:
    """
    Generate OpenAI function calling schemas
    
    Schema Format:
    {
        "type": "function",
        "function": {
            "name": "tool_name",
            "description": "Tool description",
            "parameters": {JSON Schema}
        }
    }
    """
```

##### 3. **Tool Discovery**
```python
def list_tools(self) -> List[str]:
    """Return list of available tool names"""
    
def get_tool_info(self, tool_name: str) -> Optional[Dict[str, Any]]:
    """Get detailed tool information and capabilities"""
```

#### Registry Features
- **Metadata Storage**: Tool descriptions and capabilities
- **Schema Validation**: Parameter type enforcement
- **Version Management**: Tool versioning support
- **Dependency Tracking**: Tool relationship management
- **Performance Metrics**: Usage statistics and monitoring

---

### 🔧 base - Tool Base Classes

#### Purpose
Foundation classes and interfaces for consistent tool implementation across the system.

#### Execution Flow
```
Tool Implementation → Base Class Inheritance → Interface Compliance → Registration Ready
```

#### Core Classes

##### 1. **BaseTool Abstract Class**
```python
class BaseTool(ABC):
    """
    Abstract base class for all tools
    
    Required Methods:
    - execute(**kwargs) -> Dict[str, Any]
    - get_parameters_schema() -> Dict[str, Any]
    
    Provided Methods:
    - validate_parameters()
    - format_response()
    - handle_errors()
    """
```

##### 2. **ToolMetadata Class**
```python
@dataclass
class ToolMetadata:
    name: str                    # Unique tool identifier
    description: str             # Human-readable description
    category: ToolCategory       # Tool classification
    version: str = "1.0.0"      # Tool version
    author: str = "System"      # Tool author
    tags: List[str] = None      # Searchable tags
```

##### 3. **ToolCategory Enum**
```python
class ToolCategory(Enum):
    FILESYSTEM = "filesystem"    # File operations
    SYSTEM = "system"           # System commands
    ANALYSIS = "analysis"       # Code/data analysis
    INTELLIGENCE = "intelligence" # AI-powered tools
    UTILITY = "utility"         # General utilities
    COMMUNICATION = "communication" # External APIs
```

#### Implementation Requirements

##### 1. **Parameter Schema**
```python
def get_parameters_schema(self) -> Dict[str, Any]:
    """
    Return JSON Schema for tool parameters
    
    Format:
    {
        "type": "object",
        "properties": {
            "param_name": {
                "type": "string",
                "description": "Parameter description",
                "default": "default_value"
            }
        },
        "required": ["required_param"]
    }
    """
```

##### 2. **Execution Method**
```python
def execute(self, **kwargs) -> Dict[str, Any]:
    """
    Execute tool with provided parameters
    
    Returns:
    {
        "success": bool,
        "result": Any,
        "error": Optional[str],
        "metadata": Dict[str, Any]
    }
    """
```

##### 3. **Error Handling**
```python
def handle_error(self, error: Exception) -> Dict[str, Any]:
    """
    Standardized error response format
    
    Returns:
    {
        "success": False,
        "error": str(error),
        "error_type": type(error).__name__,
        "traceback": Optional[str]
    }
    """
```

#### Tool Development Guidelines

##### 1. **Implementation Checklist**
- [ ] Inherit from BaseTool
- [ ] Implement required abstract methods
- [ ] Define comprehensive parameter schema
- [ ] Include proper error handling
- [ ] Add comprehensive documentation
- [ ] Include usage examples

##### 2. **Best Practices**
- **Idempotency**: Tools should be safe to run multiple times
- **Validation**: Validate all inputs before execution
- **Logging**: Include detailed execution logging
- **Performance**: Optimize for common use cases
- **Security**: Implement appropriate safety checks

##### 3. **Testing Requirements**
- Unit tests for all methods
- Integration tests with ToolManager
- Error condition testing
- Performance benchmarking
- Security validation

## Configuration

### Tool Manager Settings
```toml
[tool_manager]
auto_discovery = true
validation_strict = true
timeout_default = 30
retry_count = 2
logging_level = "INFO"
```

### Registry Configuration
```toml
[tool_registry]
cache_schemas = true
validate_on_register = true
allow_duplicates = false
version_tracking = true
```

### Base Tool Settings
```toml
[base_tool]
error_handling = "graceful"
parameter_validation = "strict"
response_formatting = "standard"
metadata_required = true
```

## Example Tool Implementation

```python
from agentic.tools.base import BaseTool, ToolMetadata, ToolCategory

class ExampleTool(BaseTool):
    def __init__(self):
        super().__init__(ToolMetadata(
            name="example_tool",
            description="Example tool implementation",
            category=ToolCategory.UTILITY,
            version="1.0.0"
        ))
    
    def execute(self, message: str, count: int = 1) -> Dict[str, Any]:
        try:
            result = message * count
            return {
                "success": True,
                "result": result,
                "metadata": {
                    "message_length": len(message),
                    "repeat_count": count
                }
            }
        except Exception as e:
            return self.handle_error(e)
    
    def get_parameters_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "Message to repeat"
                },
                "count": {
                    "type": "integer",
                    "description": "Number of repetitions",
                    "default": 1,
                    "minimum": 1,
                    "maximum": 100
                }
            },
            "required": ["message"]
        }
```
