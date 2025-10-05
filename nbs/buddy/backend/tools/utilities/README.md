# Utility Tools

## Overview
General-purpose utility tools for documentation generation, memory management, and system support functions.

## Tools

### 📝 doc_generator - Documentation Generation Tool

#### Purpose
Automatically generate comprehensive documentation from code, comments, and project structure.

#### Execution Flow
```
Source Analysis → Content Extraction → Template Processing → Documentation Generation → Format Output
```

#### Core Parameters
```python
{
    "source_path": "/path/to/project",           # Project root directory
    "output_format": "markdown",                 # markdown/html/pdf/rst
    "include_private": False,                    # Include private methods/classes
    "template": "default",                       # Documentation template
    "sections": ["api", "examples", "setup"]    # Sections to include
}
```

#### Documentation Types

##### 1. **API Documentation**
```python
# Automatic API doc generation
{
    "type": "api_documentation",
    "source": "python_modules",
    "output": {
        "classes": [
            {
                "name": "ClassName",
                "description": "Class purpose and usage",
                "methods": [
                    {
                        "name": "method_name",
                        "parameters": ["param1", "param2"],
                        "returns": "return_type",
                        "description": "Method functionality"
                    }
                ]
            }
        ],
        "functions": [...],
        "constants": [...]
    }
}
```

##### 2. **User Guide Generation**
```python
# User-friendly documentation
{
    "type": "user_guide",
    "sections": [
        "installation",
        "quick_start", 
        "examples",
        "troubleshooting",
        "faq"
    ],
    "format": "step_by_step",
    "include_screenshots": True
}
```

##### 3. **Technical Specifications**
```python
# Detailed technical documentation
{
    "type": "technical_specs",
    "content": [
        "architecture_overview",
        "data_models",
        "api_specifications",
        "deployment_guide",
        "performance_metrics"
    ],
    "detail_level": "comprehensive"
}
```

#### Generation Features

##### 1. **Code Analysis**
- AST parsing for Python code
- Docstring extraction and formatting
- Type hint documentation
- Import dependency mapping
- Function/class relationship analysis

##### 2. **Content Processing**
- Markdown formatting and styling
- Code syntax highlighting
- Cross-reference link generation
- Table of contents creation
- Index and glossary generation

##### 3. **Template System**
```python
# Available templates
templates = {
    "default": "Standard documentation layout",
    "api_focused": "API-centric documentation",
    "tutorial": "Step-by-step tutorial format",
    "reference": "Reference manual style",
    "minimal": "Concise documentation"
}
```

#### Output Formats

##### 1. **Markdown**
- GitHub-compatible formatting
- Mermaid diagram support
- Code block highlighting
- Table formatting
- Link validation

##### 2. **HTML**
- Responsive web design
- Interactive navigation
- Search functionality
- Mobile-friendly layout
- Custom CSS styling

##### 3. **PDF**
- Professional formatting
- Print-optimized layout
- Bookmarks and navigation
- Vector graphics support
- Custom branding

#### Example Usage

##### Project Documentation
```python
doc_generator(
    source_path="./my_project",
    output_format="markdown",
    sections=["readme", "api", "examples", "deployment"],
    template="default"
)
```

##### API Reference
```python
doc_generator(
    source_path="./src/api",
    output_format="html",
    include_private=False,
    template="api_focused",
    sections=["api", "examples"]
)
```

---

### 🧠 memory - Advanced Memory Management

#### Purpose
Sophisticated memory management for conversation context, user preferences, and system state persistence.

#### Execution Flow
```
Memory Request → Context Retrieval → Relevance Scoring → Memory Update → Optimization → Storage
```

#### Memory Architecture

##### 1. **Hierarchical Memory Structure**
```python
{
    "working_memory": {
        "current_conversation": [...],
        "active_tasks": [...],
        "temporary_variables": {...}
    },
    "short_term_memory": {
        "recent_interactions": [...],
        "session_context": {...},
        "user_preferences": {...}
    },
    "long_term_memory": {
        "user_profile": {...},
        "learned_patterns": [...],
        "knowledge_base": {...},
        "success_templates": [...]
    }
}
```

##### 2. **Memory Types**

###### Working Memory (Active Context)
- Current conversation state
- Active tool executions
- Temporary calculations
- Immediate context variables

###### Short-term Memory (Session Context)
- Recent conversation history
- User interaction patterns
- Session preferences
- Temporary learning

###### Long-term Memory (Persistent Knowledge)
- User behavior patterns
- Successful solution templates
- Domain expertise accumulation
- Performance optimization data

##### 3. **Memory Operations**

###### Storage Operations
```python
def store_memory(self, content: Dict, memory_type: str, tags: List[str]) -> str:
    """
    Store information in appropriate memory layer
    
    Parameters:
    - content: Information to store
    - memory_type: working/short_term/long_term
    - tags: Searchable metadata tags
    
    Returns: Memory ID for retrieval
    """
```

###### Retrieval Operations
```python
def retrieve_memory(self, query: str, memory_type: str = "all") -> List[Dict]:
    """
    Retrieve relevant memories based on query
    
    Uses:
    - Semantic similarity matching
    - Tag-based filtering
    - Recency weighting
    - Relevance scoring
    """
```

###### Update Operations
```python
def update_memory(self, memory_id: str, updates: Dict) -> bool:
    """
    Update existing memory with new information
    
    Features:
    - Incremental updates
    - Version tracking
    - Conflict resolution
    - Automatic reindexing
    """
```

#### Memory Features

##### 1. **Intelligent Indexing**
- Semantic embedding generation
- Keyword extraction and tagging
- Relationship mapping
- Temporal indexing
- Usage frequency tracking

##### 2. **Context Management**
```python
{
    "context_window": 4096,           # Token limit for active context
    "relevance_threshold": 0.7,       # Minimum relevance score
    "decay_factor": 0.95,            # Memory importance decay
    "compression_ratio": 0.8,         # Context compression target
    "refresh_interval": 3600          # Memory optimization interval
}
```

##### 3. **Privacy and Security**
- Sensitive information detection
- Automatic data anonymization
- Encryption for persistent storage
- Access control and permissions
- Data retention policies

#### Memory Optimization

##### 1. **Automatic Cleanup**
- Expired memory removal
- Duplicate detection and merging
- Relevance-based pruning
- Storage optimization
- Index maintenance

##### 2. **Compression Strategies**
- Semantic summarization
- Redundancy elimination
- Hierarchical compression
- Lossy compression for old data
- Priority-based retention

##### 3. **Performance Optimization**
- Caching frequently accessed memories
- Lazy loading for large datasets
- Parallel processing for searches
- Index optimization
- Query result caching

#### Example Usage

##### Conversation Context
```python
memory.store_memory(
    content={
        "user_question": "How do I deploy a Flask app?",
        "solution_provided": "Docker containerization approach",
        "user_satisfaction": "high",
        "follow_up_questions": []
    },
    memory_type="short_term",
    tags=["flask", "deployment", "docker", "web_development"]
)
```

##### User Preference Learning
```python
memory.store_memory(
    content={
        "preferred_frameworks": ["Flask", "FastAPI"],
        "coding_style": "pythonic",
        "documentation_level": "detailed",
        "example_preference": "practical"
    },
    memory_type="long_term",
    tags=["user_preferences", "development", "python"]
)
```

##### Solution Template Storage
```python
memory.store_memory(
    content={
        "problem_pattern": "web_api_with_auth",
        "solution_template": {
            "framework": "Flask",
            "auth_method": "JWT",
            "database": "PostgreSQL",
            "deployment": "Docker"
        },
        "success_rate": 0.95,
        "user_feedback": "positive"
    },
    memory_type="long_term",
    tags=["solution_template", "web_api", "authentication"]
)
```

## Configuration

### Documentation Generator
```toml
[doc_generator]
default_template = "default"
output_directory = "./docs"
include_private_members = false
generate_index = true
syntax_highlighting = true
```

### Memory Management
```toml
[memory]
working_memory_limit = 1000      # Max items in working memory
short_term_retention = "24h"     # Short-term memory retention
long_term_retention = "30d"      # Long-term memory retention
compression_enabled = true       # Enable memory compression
encryption_enabled = true        # Encrypt sensitive data
```

### Performance Settings
```toml
[utilities.performance]
cache_size = "100MB"            # Memory cache size
index_update_interval = 3600    # Index update frequency (seconds)
cleanup_interval = 86400        # Cleanup frequency (seconds)
parallel_processing = true      # Enable parallel operations
```
