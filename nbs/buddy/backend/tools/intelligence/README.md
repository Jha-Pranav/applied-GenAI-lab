# Intelligence Tools

## Overview
Advanced AI-powered tools for multi-perspective analysis, decision making, and intelligent reasoning.

## Tools

### 🧠 debate - Multi-Perspective Analysis Tool

#### Purpose
Conduct structured debates with multiple AI agents to provide balanced analysis for complex decisions and comparisons.

#### Execution Flow
```
Topic Input → Agent Creation → Debate Rounds → Analysis Synthesis → Recommendation Generation
```

#### Core Parameters
```python
{
    "topic": "Python vs JavaScript: which is better?",
    "context": "Web development framework selection",  # Optional
    "max_rounds": 2                                   # Optional: default 2
}
```

#### Agent Architecture

##### 1. **Advocate Agent**
- **Role**: Argues in favor of one position
- **Capabilities**: 
  - Presents strongest arguments
  - Provides supporting evidence
  - Addresses counterarguments
- **Model**: Qwen 3:8B with specialized prompting

##### 2. **Critic Agent** 
- **Role**: Challenges and questions positions
- **Capabilities**:
  - Identifies weaknesses in arguments
  - Presents alternative perspectives
  - Demands evidence and clarification
- **Model**: Qwen 3:8B with critical thinking focus

##### 3. **Expert Agent**
- **Role**: Provides technical expertise and facts
- **Capabilities**:
  - Offers domain-specific knowledge
  - Validates technical claims
  - Provides objective analysis
- **Model**: Qwen 3:8B with expert knowledge base

##### 4. **Moderator Agent**
- **Role**: Facilitates discussion and synthesizes conclusions
- **Capabilities**:
  - Manages debate flow
  - Ensures balanced participation
  - Generates final recommendations
- **Model**: Qwen 3:8B with synthesis capabilities

#### Debate Structure

##### Round 1: Opening Statements
```
1. Advocate presents initial position (2-3 key arguments)
2. Critic challenges with counterarguments
3. Expert provides technical context
4. Moderator summarizes positions
```

##### Round 2: Rebuttals and Evidence
```
1. Advocate responds to criticisms with evidence
2. Critic deepens analysis with specific examples
3. Expert validates or corrects technical claims
4. Moderator synthesizes final position
```

#### Output Format

##### 1. **Structured Analysis**
```python
{
    "debate_summary": {
        "topic": "Original question",
        "participants": ["Advocate", "Critic", "Expert", "Moderator"],
        "rounds_completed": 2,
        "total_exchanges": 8
    },
    "key_arguments": {
        "position_a": ["Argument 1", "Argument 2", "Argument 3"],
        "position_b": ["Counter 1", "Counter 2", "Counter 3"]
    },
    "evidence_presented": [
        "Technical benchmarks",
        "Industry adoption statistics", 
        "Developer experience surveys"
    ],
    "final_recommendation": "Balanced conclusion with conditions"
}
```

##### 2. **Streaming Output**
Real-time display of debate progression:
```
🎯 Advocate: Opening Statement
[Streaming argument presentation]

🔍 Critic: Challenge
[Streaming counterargument]

👨‍💻 Expert: Technical Analysis  
[Streaming expert opinion]

⚖️ Moderator: Round Summary
[Streaming synthesis]
```

#### Use Cases

##### 1. **Technology Comparisons**
```python
debate(
    topic="React vs Vue.js for enterprise applications",
    context="Large-scale web application development",
    max_rounds=3
)
```

##### 2. **Architectural Decisions**
```python
debate(
    topic="Microservices vs Monolithic architecture",
    context="E-commerce platform redesign",
    max_rounds=2
)
```

##### 3. **Strategic Planning**
```python
debate(
    topic="Cloud migration strategy: AWS vs Azure vs GCP",
    context="Fortune 500 company infrastructure modernization",
    max_rounds=3
)
```

#### Quality Assurance

##### 1. **Argument Validation**
- Fact-checking against knowledge base
- Logical consistency verification
- Evidence quality assessment
- Bias detection and mitigation

##### 2. **Balance Enforcement**
- Equal speaking time allocation
- Perspective diversity requirements
- Counterargument completeness
- Conclusion objectivity

##### 3. **Output Quality**
- Clarity and readability scoring
- Technical accuracy validation
- Actionability assessment
- Stakeholder relevance check

---

### 🧩 memory - Conversation Memory Management

#### Purpose
Maintain context and conversation history for improved decision making and continuity.

#### Execution Flow
```
Input → Context Retrieval → Memory Update → Relevance Scoring → Storage Optimization
```

#### Memory Types

##### 1. **Short-term Memory**
- Current conversation context
- Recent tool usage history
- Active task state
- Temporary variables

##### 2. **Long-term Memory**
- User preferences and patterns
- Successful solution templates
- Domain knowledge accumulation
- Performance metrics

##### 3. **Semantic Memory**
- Concept relationships
- Tool usage patterns
- Decision precedents
- Best practice knowledge

#### Features
- **Context Preservation**: Maintains conversation flow
- **Pattern Recognition**: Identifies recurring themes
- **Preference Learning**: Adapts to user behavior
- **Knowledge Accumulation**: Builds expertise over time

---

### 🔍 introspect - Self-Reflection and Validation

#### Purpose
Analyze system performance, validate decisions, and provide self-assessment capabilities.

#### Execution Flow
```
System State → Performance Analysis → Decision Validation → Improvement Recommendations
```

#### Analysis Dimensions

##### 1. **Decision Quality**
- Accuracy of tool selection
- Appropriateness of responses
- User satisfaction indicators
- Outcome effectiveness

##### 2. **Performance Metrics**
- Response time analysis
- Resource utilization
- Error rate tracking
- Success rate measurement

##### 3. **Learning Opportunities**
- Failed interaction analysis
- Improvement area identification
- Knowledge gap detection
- Skill development needs

#### Validation Processes

##### 1. **Pre-execution Validation**
- Parameter completeness check
- Safety requirement verification
- Resource availability confirmation
- Permission validation

##### 2. **Post-execution Analysis**
- Result quality assessment
- User feedback integration
- Performance metric update
- Learning extraction

##### 3. **Continuous Improvement**
- Pattern recognition in failures
- Success factor identification
- Optimization opportunity detection
- Capability enhancement planning

## Configuration

### Debate Settings
```toml
[debate]
default_rounds = 2
max_rounds = 5
agent_timeout = 60
streaming_enabled = true
evidence_validation = true
```

### Memory Management
```toml
[memory]
short_term_limit = 100
long_term_retention = "30d"
semantic_indexing = true
privacy_mode = false
```

### Introspection
```toml
[introspect]
validation_level = "standard"
performance_tracking = true
learning_enabled = true
feedback_integration = true
```
