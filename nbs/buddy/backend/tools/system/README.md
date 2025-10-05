# System Tools

## Overview
Secure system command execution with environment control, output capture, and safety mechanisms.

## Tools

### ⚡ execute_bash - Secure Shell Command Execution

#### Purpose
Execute shell commands safely with comprehensive output capture, timeout control, and security validation.

#### Execution Flow
```
Command → Security Validation → Environment Setup → Execution → Output Capture → Result Processing
```

#### Core Parameters
```python
{
    "command": "ls -la /home",           # Shell command to execute
    "summary": "List home directory",   # Optional: Human-readable description
    "timeout": 30,                      # Optional: Timeout in seconds (default: 30)
    "working_dir": "/path/to/dir",      # Optional: Working directory
    "env_vars": {"VAR": "value"}        # Optional: Environment variables
}
```

#### Security Features

##### 1. **Command Validation**
- **Dangerous Commands**: Blocked by default (rm -rf, dd, mkfs, etc.)
- **Path Traversal**: Prevents access to sensitive directories
- **Privilege Escalation**: Blocks sudo, su commands
- **Network Operations**: Configurable restrictions

##### 2. **Execution Environment**
```python
# Safe execution context
{
    "shell": "/bin/bash",
    "timeout": 30,
    "capture_output": True,
    "text": True,
    "env": "controlled_environment"
}
```

##### 3. **Output Processing**
- **Stream Capture**: Both stdout and stderr captured
- **Real-time Monitoring**: Progress tracking for long operations
- **Size Limits**: Prevents memory exhaustion from large outputs
- **Encoding Handling**: Proper UTF-8 processing

#### Execution Conditions

##### Success Conditions
- Command exists and is executable
- No security violations detected
- Execution completes within timeout
- Exit code indicates success (0)

##### Failure Conditions
- Command not found (exit code 127)
- Permission denied (exit code 126)
- Timeout exceeded
- Security policy violation
- System resource exhaustion

#### Response Format
```python
{
    "exit_status": 0,                    # Command exit code
    "stdout": "command output",          # Standard output
    "stderr": "",                        # Standard error
    "execution_time": 1.23,             # Time taken in seconds
    "working_directory": "/path",        # Actual working directory
    "command_summary": "description"     # Human-readable summary
}
```

#### Example Usage

##### Basic Commands
```bash
# File operations
execute_bash(command="ls -la", summary="List current directory")
execute_bash(command="cat config.txt", summary="Read configuration file")

# System information
execute_bash(command="df -h", summary="Check disk usage")
execute_bash(command="ps aux | grep python", summary="Find Python processes")
```

##### Advanced Usage
```bash
# With working directory
execute_bash(
    command="npm install", 
    working_dir="/project/frontend",
    timeout=300,
    summary="Install Node.js dependencies"
)

# With environment variables
execute_bash(
    command="python script.py",
    env_vars={"PYTHONPATH": "/custom/path", "DEBUG": "1"},
    summary="Run Python script with custom environment"
)
```

#### Safety Mechanisms

##### 1. **Timeout Control**
- Default 30-second timeout
- Configurable per command
- Graceful termination with SIGTERM
- Force kill with SIGKILL if needed

##### 2. **Resource Limits**
- Memory usage monitoring
- CPU time restrictions
- Output size limits
- Process count limits

##### 3. **Sandboxing**
- Restricted file system access
- Network isolation options
- User privilege dropping
- Temporary directory cleanup

#### Error Handling

##### Common Error Scenarios
```python
# Command not found
{
    "exit_status": 127,
    "stderr": "command not found: nonexistent_cmd",
    "error_type": "CommandNotFound"
}

# Permission denied
{
    "exit_status": 126, 
    "stderr": "permission denied",
    "error_type": "PermissionDenied"
}

# Timeout exceeded
{
    "exit_status": -1,
    "stderr": "Command timed out after 30 seconds",
    "error_type": "TimeoutError"
}
```

##### Recovery Strategies
- Automatic retry for transient failures
- Fallback commands for common operations
- Detailed error reporting for debugging
- Cleanup of partial operations

## Configuration

### Security Policy
```toml
[execute_bash]
dangerous_commands = ["rm -rf", "dd", "mkfs", "fdisk"]
allowed_paths = ["/home", "/tmp", "/var/tmp"]
blocked_paths = ["/etc", "/sys", "/proc"]
max_timeout = 300
enable_network = false
```

### Performance Settings
```toml
[execute_bash.limits]
max_output_size = "10MB"
max_memory = "512MB" 
max_processes = 10
cleanup_timeout = 5
```

### Monitoring
- Command execution logging
- Performance metrics collection
- Security violation tracking
- Resource usage monitoring
