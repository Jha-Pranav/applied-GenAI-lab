# Analysis Tools

## Overview
Advanced code analysis and interpretation tools for safe Python execution and code quality assessment.

## Tools

### 🐍 code_interpreter - Safe Python Code Execution

#### Purpose
Execute Python code safely in isolated environments with comprehensive output capture and error handling.

#### Execution Flow
```
Code Input → Syntax Validation → Environment Setup → Safe Execution → Output Capture → Result Processing
```

#### Core Parameters
```python
{
    "code": "print('Hello World')",     # Python code to execute
    "summary": "Test print statement",  # Optional: Description
    "timeout": 30,                      # Optional: Execution timeout
    "capture_plots": True,              # Optional: Capture matplotlib plots
    "working_dir": "/tmp/code_exec"     # Optional: Execution directory
}
```

#### Execution Environment

##### 1. **Isolated Sandbox**
- Separate Python process for each execution
- Restricted file system access
- Limited network capabilities
- Memory and CPU constraints

##### 2. **Available Libraries**
```python
# Pre-installed packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import os
import sys
import datetime
# ... and more standard libraries
```

##### 3. **Security Restrictions**
- No access to sensitive system functions
- File operations limited to working directory
- Network requests monitored and filtered
- Import restrictions on dangerous modules

#### Execution Modes

##### 1. **Standard Execution**
```python
# Simple code execution
{
    "code": """
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
print(f"Squares: {y}")
""",
    "summary": "Calculate squares of numbers"
}
```

##### 2. **Data Analysis Mode**
```python
# Data processing with pandas
{
    "code": """
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'A': np.random.randn(100),
    'B': np.random.randn(100)
})
print(data.describe())
""",
    "summary": "Generate and analyze random data"
}
```

##### 3. **Visualization Mode**
```python
# Plot generation
{
    "code": """
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.savefig('sine_wave.png')
plt.show()
""",
    "capture_plots": True,
    "summary": "Generate sine wave plot"
}
```

#### Output Processing

##### 1. **Standard Output Capture**
```python
{
    "stdout": "Execution output text",
    "stderr": "Error messages if any",
    "return_value": "Last expression result",
    "execution_time": 1.23
}
```

##### 2. **Plot Capture**
```python
{
    "plots": [
        {
            "filename": "sine_wave.png",
            "format": "PNG",
            "size": "1024x768",
            "data": "base64_encoded_image"
        }
    ]
}
```

##### 3. **Variable Inspection**
```python
{
    "variables": {
        "x": "[1, 2, 3, 4, 5]",
        "y": "[1, 4, 9, 16, 25]",
        "data": "DataFrame(100 rows x 2 columns)"
    }
}
```

#### Error Handling

##### 1. **Syntax Errors**
```python
{
    "error_type": "SyntaxError",
    "error_message": "invalid syntax (line 2)",
    "line_number": 2,
    "code_context": "print('hello'"
}
```

##### 2. **Runtime Errors**
```python
{
    "error_type": "ZeroDivisionError", 
    "error_message": "division by zero",
    "traceback": "Full traceback information",
    "execution_stopped_at": "line 5"
}
```

##### 3. **Timeout Errors**
```python
{
    "error_type": "TimeoutError",
    "error_message": "Code execution exceeded 30 seconds",
    "partial_output": "Output before timeout"
}
```

#### Safety Features

##### 1. **Code Validation**
- Syntax checking before execution
- AST analysis for dangerous operations
- Import statement validation
- Function call monitoring

##### 2. **Resource Limits**
- Memory usage constraints (default: 512MB)
- CPU time limits (default: 30 seconds)
- Output size restrictions (default: 10MB)
- File creation limits

##### 3. **Cleanup Mechanisms**
- Automatic cleanup of temporary files
- Process termination on timeout
- Memory garbage collection
- Plot buffer clearing

#### Example Usage

##### Data Analysis
```python
code_interpreter(code="""
import pandas as pd
import numpy as np

# Load and analyze data
df = pd.read_csv('data.csv')
print(f"Dataset shape: {df.shape}")
print(f"Missing values: {df.isnull().sum()}")

# Basic statistics
print(df.describe())
""", summary="Analyze CSV dataset")
```

##### Mathematical Computation
```python
code_interpreter(code="""
import numpy as np
from scipy import stats

# Generate sample data
data = np.random.normal(100, 15, 1000)

# Statistical analysis
mean = np.mean(data)
std = np.std(data)
median = np.median(data)

print(f"Mean: {mean:.2f}")
print(f"Std: {std:.2f}")
print(f"Median: {median:.2f}")

# Normality test
statistic, p_value = stats.normaltest(data)
print(f"Normality test p-value: {p_value:.4f}")
""", summary="Statistical analysis of normal distribution")
```

---

### 📊 code_quality - Code Quality Assessment

#### Purpose
Analyze Python code for quality metrics, style compliance, and potential issues.

#### Execution Flow
```
Code Input → AST Parsing → Quality Analysis → Metrics Calculation → Report Generation
```

#### Analysis Dimensions

##### 1. **Complexity Metrics**
- Cyclomatic complexity
- Cognitive complexity
- Nesting depth
- Function length

##### 2. **Style Compliance**
- PEP 8 adherence
- Naming conventions
- Documentation coverage
- Import organization

##### 3. **Potential Issues**
- Code smells detection
- Security vulnerabilities
- Performance bottlenecks
- Maintainability concerns

#### Example Usage
```python
code_quality(code="""
def complex_function(x, y, z):
    if x > 0:
        if y > 0:
            if z > 0:
                return x + y + z
            else:
                return x + y
        else:
            return x
    else:
        return 0
""", summary="Analyze function complexity")
```

## Configuration

### Execution Environment
```toml
[code_interpreter]
timeout = 30
max_memory = "512MB"
max_output_size = "10MB"
working_directory = "/tmp/code_exec"
cleanup_after_execution = true
```

### Security Settings
```toml
[code_interpreter.security]
allowed_imports = ["numpy", "pandas", "matplotlib", "requests"]
blocked_imports = ["subprocess", "os.system", "eval", "exec"]
network_access = "restricted"
file_access = "working_dir_only"
```

### Quality Analysis
```toml
[code_quality]
max_complexity = 10
max_function_length = 50
enforce_pep8 = true
require_docstrings = true
```
