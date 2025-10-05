# Filesystem Tools

## Overview
Advanced file system operations with Git integration, fuzzy matching, and intelligent content discovery.

## Tools

### 🔍 fs_read - Advanced File Reading Tool

#### Purpose
Intelligent file discovery and content extraction with multiple operation modes.

#### Execution Flow
```
Request → Mode Detection → Path Resolution → Content Processing → Response
```

#### Operation Modes

##### 1. **Line Mode** - Read specific lines from files
```python
# Parameters
{
    "mode": "Line",
    "path": "/path/to/file.py",
    "start_line": 1,      # Optional: starting line (default: 1)
    "end_line": 50        # Optional: ending line (default: -1, end of file)
}
```

**Conditions:**
- File must exist and be readable
- Line numbers must be valid (positive integers)
- Supports negative indexing from end of file

##### 2. **Directory Mode** - List directory contents
```python
# Parameters
{
    "mode": "Directory", 
    "path": "/path/to/directory",
    "depth": 2           # Optional: recursion depth (default: 0)
}
```

**Conditions:**
- Path must be a valid directory
- Depth controls recursion level (0 = current level only)
- Returns file/directory listing with metadata

##### 3. **Search Mode** - Pattern-based content search
```python
# Parameters
{
    "mode": "Search",
    "path": "/path/to/file",
    "pattern": "function.*main",  # Regex pattern
    "context_lines": 3           # Optional: lines around matches (default: 2)
}
```

**Conditions:**
- Pattern must be valid regex
- Case-insensitive matching
- Returns matches with surrounding context

#### Advanced Features
- **Git Integration**: Respects .gitignore patterns
- **Fuzzy Matching**: Intelligent path resolution
- **Binary Detection**: Automatically skips binary files
- **Error Handling**: Graceful failure with detailed messages

#### Example Usage
```bash
# Read specific lines
fs_read(mode="Line", path="main.py", start_line=10, end_line=20)

# Search for patterns
fs_read(mode="Search", path="src/", pattern="class.*Agent", context_lines=5)

# List directory
fs_read(mode="Directory", path="./", depth=1)
```

---

### ✏️ fs_write - Intelligent File Writing Tool

#### Purpose
Safe file operations with diff preview, backup creation, and validation.

#### Execution Flow
```
Request → Path Validation → Backup Creation → Content Processing → Write Operation → Verification
```

#### Operation Modes

##### 1. **Create Mode** - Create new files
```python
# Parameters
{
    "command": "create",
    "path": "/path/to/newfile.py",
    "file_text": "print('Hello World')"
}
```

**Conditions:**
- Path must not exist (prevents overwriting)
- Parent directory must exist or be creatable
- Content must be valid text

##### 2. **String Replace Mode** - Targeted content replacement
```python
# Parameters
{
    "command": "str_replace",
    "path": "/path/to/file.py",
    "old_str": "def old_function():",
    "new_str": "def new_function():"
}
```

**Conditions:**
- File must exist and be readable
- `old_str` must match exactly one occurrence
- Preserves file formatting and encoding

##### 3. **Insert Mode** - Add content at specific line
```python
# Parameters
{
    "command": "insert",
    "path": "/path/to/file.py", 
    "insert_line": 10,
    "new_str": "# New comment"
}
```

**Conditions:**
- File must exist
- Line number must be valid
- Content inserted after specified line

##### 4. **Append Mode** - Add content to end of file
```python
# Parameters
{
    "command": "append",
    "path": "/path/to/file.py",
    "new_str": "\n# Footer comment"
}
```

**Conditions:**
- File must exist
- Automatically adds newline if needed

#### Safety Features
- **Automatic Backup**: Creates `.backup` files before modifications
- **Diff Preview**: Shows changes before applying (in debug mode)
- **Validation**: Verifies operations completed successfully
- **Rollback**: Can restore from backup on failure

#### Example Usage
```bash
# Create new file
fs_write(command="create", path="config.py", file_text="DEBUG = True")

# Replace content
fs_write(command="str_replace", path="main.py", 
         old_str="version = '1.0'", new_str="version = '2.0'")

# Insert at line
fs_write(command="insert", path="README.md", insert_line=5, 
         new_str="## New Section")
```

## Configuration

### Security Settings
- **Dangerous Operations**: Flagged operations require approval
- **Path Restrictions**: Configurable allowed/blocked paths
- **Backup Policy**: Automatic backup creation for modifications

### Performance Optimization
- **Caching**: Frequently accessed files cached in memory
- **Lazy Loading**: Large files processed in chunks
- **Git Integration**: Efficient .gitignore processing
