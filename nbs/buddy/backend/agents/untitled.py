# models.py
from enum import Enum
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class ExecutionMode(Enum):
    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"

class Resources(BaseModel):
    previous: List[str] = Field(default_factory=list, description="Resources created in previous steps")
    required: List[str] = Field(default_factory=list, description="Resources helpful or required for this/current next step")

class ActionStep(BaseModel):
    step: int = Field(..., description="The step number")
    action: str = Field(..., description="The action description")
    tool: Optional[str] = Field(None, description="The tool to use (from available tools)")
    purpose: str = Field(..., description="The purpose of this step")
    sub_steps: List[str] = Field(default_factory=list, description="Sub-steps if any")
    introspect_after: bool = Field(True, description="Whether to call introspect after this step for feedback and retry")
    system_prompt: str = Field(..., description="Self-sufficient system prompt for this subtask, including context and rules")
    user_prompt: str = Field(..., description="Self-sufficient user prompt for this subtask, with instructions and prior progress")
    introspect_prompt: str = Field(..., description="Template prompt for introspect, with placeholders like {performed_action}")
    resources: Resources = Field(default_factory=Resources, description="Resources for this subtask")
    execution_mode: ExecutionMode = Field(ExecutionMode.SEQUENTIAL, description="Sequential or parallel execution")

class Task(BaseModel):
    id: str = Field(..., description="Unique task ID, e.g., T001")
    name: str = Field(..., description="Concise task name")
    description: str = Field(..., description="Detailed task description")
    dependencies: List[str] = Field(default_factory=list, description="List of dependent task IDs")
    tools: List[str] = Field(default_factory=list, description="List of tool names, e.g., fs_read, debate_agent")
    actions: List[ActionStep] = Field(default_factory=list, description="List of action steps (subtasks)")
    success_criteria: str = Field(..., description="Criteria for task success, including retry logic")
    expected_outputs: List[str] = Field(default_factory=list, description="Expected output artifacts")
    resources: Resources = Field(default_factory=Resources, description="Overall resources for the task")

class ExecutionPlan(BaseModel):
    sequential_phases: List[List[str]] = Field(default_factory=list, description="Phases of task IDs in sequence, with parallel lists")
    parallel_groups: List[List[str]] = Field(default_factory=list, description="Groups of tasks that can run in parallel")
    critical_path: List[str] = Field(default_factory=list, description="Critical path task IDs")
    total_actions: int = Field(0, description="Total number of actions across tasks")
    ordering: List[str] = Field(default_factory=list, description="Explicit overall ordering of tasks")

class AnalysisResult(BaseModel):
    tasks: List[Task] = Field(default_factory=list, description="List of decomposed tasks")
    execution_plan: ExecutionPlan = Field(..., description="Execution plan")
    tools_needed: List[str] = Field(default_factory=list, description="Unique tools needed across tasks")
    success_criteria: List[str] = Field(default_factory=list, description="Overall success criteria")
    resources: Resources = Field(default_factory=Resources, description="Overall resources across the plan")

# ================================================================================
# json_utils.py
import json
from typing import List, Dict, Any, Tuple, Optional

# Optional library imports
try:
    import jsonrepair
    HAS_JSONREPAIR = True
except ImportError:
    HAS_JSONREPAIR = False

try:
    import json5
    HAS_JSON5 = True
except ImportError:
    HAS_JSON5 = False

try:
    from jsonschema import validate, ValidationError as JsonSchemaValidationError
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

class JSONRepairUtils:
    """Utility class for JSON parsing and repair using external libraries"""
    
    @staticmethod
    def repair_json_with_libraries(raw_response: str) -> Tuple[str, List[str]]:
        """Use libraries for JSON repair and cleaning"""
        errors = []
        response = raw_response.strip()

        # Extract from code blocks
        if "```json" in response:
            start = response.find("```json") + 7
            end = response.rfind("```")
            if start > 6 and end > start:
                response = response[start:end].strip()
            else:
                errors.append("Invalid code block boundaries")

        # Try jsonrepair first (most comprehensive)
        if HAS_JSONREPAIR:
            try:
                repaired = jsonrepair.repair_json(response)
                json.loads(repaired)  # Validate
                return repaired, errors
            except Exception as e:
                errors.append(f"jsonrepair failed: {str(e)}")

        # Try json5 (handles trailing commas, comments)
        if HAS_JSON5:
            try:
                parsed = json5.loads(response)
                return json.dumps(parsed), errors
            except Exception as e:
                errors.append(f"json5 parsing failed: {str(e)}")

        # Try standard JSON
        try:
            parsed = json.loads(response)
            return response, errors
        except json.JSONDecodeError as e:
            errors.append(f"Standard JSON parsing failed: {str(e)}")

        # Fallback to manual extraction
        cleaned = JSONRepairUtils._extract_json_manually(response)
        try:
            json.loads(cleaned)
            return cleaned, errors
        except json.JSONDecodeError as e:
            errors.append(f"Manual extraction failed: {str(e)}")
            return "[]", errors

    @staticmethod
    def _extract_json_manually(response: str) -> str:
        """Manual JSON extraction as last resort"""
        # Try to find array boundaries
        bracket_start = response.find("[")
        bracket_end = response.rfind("]")
        
        if bracket_start != -1 and bracket_end != -1 and bracket_start < bracket_end:
            potential_json = response[bracket_start:bracket_end + 1]
            try:
                json.loads(potential_json)
                return potential_json
            except json.JSONDecodeError:
                pass

        # Try to find object boundaries
        brace_start = response.find("{")
        brace_end = response.rfind("}")
        
        if brace_start != -1 and brace_end != -1 and brace_start < brace_end:
            potential_json = response[brace_start:brace_end + 1]
            try:
                parsed = json.loads(potential_json)
                return json.dumps([parsed] if isinstance(parsed, dict) else parsed)
            except json.JSONDecodeError:
                pass

        return "[]"

    @staticmethod
    def clean_json_response(raw_response: str) -> str:
        """Clean raw response to valid JSON"""
        response = raw_response.strip()
        if "```json" in response:
            start = response.find("```json") + 7
            end = response.rfind("```")
            if start > 6 and end > start:
                return response[start:end].strip()
        
        # Try to extract JSON boundaries
        bracket_start = response.find("[")
        bracket_end = response.rfind("]")
        brace_start = response.find("{")
        brace_end = response.rfind("}")
        
        if bracket_start != -1 and bracket_end != -1 and bracket_start < bracket_end:
            return response[bracket_start:bracket_end + 1]
        elif brace_start != -1 and brace_end != -1 and brace_start < brace_end:
            return response[brace_start:brace_end + 1]
        
        return "[]"

# ================================================================================
# schema_validator.py
from typing import List, Dict, Any, Tuple
from pydantic import ValidationError
from .models import Task
from .json_utils import HAS_JSONSCHEMA

if HAS_JSONSCHEMA:
    from jsonschema import validate, ValidationError as JsonSchemaValidationError

class SchemaValidator:
    """Handles schema validation for tasks using jsonschema or pydantic"""
    
    AVAILABLE_TOOLS = ["fs_read", "fs_write", "execute_bash", "introspect", "debate_agent"]
    
    @classmethod
    def get_task_schema(cls) -> Dict[str, Any]:
        """Get the JSON schema for task validation"""
        return {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "name", "description", "dependencies", "tools", "actions", "success_criteria", "expected_outputs", "resources"],
                "properties": {
                    "id": {"type": "string", "pattern": "^T\\d+$"},
                    "name": {"type": "string", "minLength": 1},
                    "description": {"type": "string", "minLength": 1},
                    "dependencies": {"type": "array", "items": {"type": "string"}},
                    "tools": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": cls.AVAILABLE_TOOLS
                        }
                    },
                    "actions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["step", "action", "purpose", "system_prompt", "user_prompt", "introspect_prompt"],
                            "properties": {
                                "step": {"type": "integer", "minimum": 1},
                                "action": {"type": "string", "minLength": 1},
                                "tool": {"type": "string"},
                                "purpose": {"type": "string", "minLength": 1},
                                "sub_steps": {"type": "array", "items": {"type": "string"}},
                                "introspect_after": {"type": "boolean"},
                                "system_prompt": {"type": "string", "minLength": 1},
                                "user_prompt": {"type": "string", "minLength": 1},
                                "introspect_prompt": {"type": "string", "minLength": 1},
                                "resources": {
                                    "type": "object",
                                    "properties": {
                                        "previous": {"type": "array", "items": {"type": "string"}},
                                        "required": {"type": "array", "items": {"type": "string"}}
                                    }
                                },
                                "execution_mode": {"type": "string", "enum": ["sequential", "parallel"]}
                            }
                        }
                    },
                    "success_criteria": {"type": "string", "minLength": 1},
                    "expected_outputs": {"type": "array", "items": {"type": "string"}},
                    "resources": {
                        "type": "object",
                        "properties": {
                            "previous": {"type": "array", "items": {"type": "string"}},
                            "required": {"type": "array", "items": {"type": "string"}}
                        }
                    }
                }
            }
        }

    @classmethod
    def validate_with_jsonschema(cls, task_data: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[str]]:
        """Validate using jsonschema library"""
        if not HAS_JSONSCHEMA:
            return cls.validate_with_pydantic(task_data)
            
        task_schema = cls.get_task_schema()
        errors = []
        
        try:
            validate(task_data, task_schema)
            return task_data, errors
        except JsonSchemaValidationError as e:
            errors.append(f"Schema validation failed: {str(e)}")

        # Validate individual tasks and try to fix them
        valid_tasks = []
        for idx, task in enumerate(task_data):
            try:
                validate(task, task_schema["items"])
                valid_tasks.append(task)
            except JsonSchemaValidationError as e:
                errors.append(f"Task {idx+1} validation failed: {str(e)}")
                fixed_task = cls.fix_task_schema_issues(task)
                try:
                    validate(fixed_task, task_schema["items"])
                    valid_tasks.append(fixed_task)
                except JsonSchemaValidationError:
                    continue

        return valid_tasks, errors

    @classmethod
    def validate_with_pydantic(cls, task_data: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[str]]:
        """Fallback validation using pydantic"""
        errors = []
        valid_tasks = []
        
        for idx, task in enumerate(task_data):
            try:
                Task.model_validate(task)
                valid_tasks.append(task)
            except ValidationError as ve:
                errors.append(f"Task {idx+1}: {str(ve)}")
                # Try to fix and re-validate
                fixed_task = cls.fix_task_schema_issues(task)
                try:
                    Task.model_validate(fixed_task)
                    valid_tasks.append(fixed_task)
                except ValidationError:
                    continue
        
        return valid_tasks, errors

    @staticmethod
    def fix_task_schema_issues(task: Dict[str, Any]) -> Dict[str, Any]:
        """Fix common schema issues in tasks"""
        fixed_task = task.copy()
        
        # Ensure required fields exist with defaults
        defaults = {
            "dependencies": [],
            "tools": [],
            "actions": [],
            "expected_outputs": [],
            "resources": {"previous": [], "required": []}
        }
        
        for field, default_value in defaults.items():
            if field not in fixed_task:
                fixed_task[field] = default_value

        # Fix actions
        if "actions" in fixed_task and isinstance(fixed_task["actions"], list):
            for action in fixed_task["actions"]:
                if isinstance(action, dict):
                    if "introspect_after" not in action:
                        action["introspect_after"] = True
                    if "execution_mode" not in action:
                        action["execution_mode"] = "sequential"
                    if "resources" not in action:
                        action["resources"] = {"previous": [], "required": []}
                    if "sub_steps" not in action:
                        action["sub_steps"] = []

        return fixed_task

# ================================================================================
# json_repair_agent.py
import json
import time
from typing import List, Dict, Any
from rich.console import Console

from agentic.core.agent import Agent, AgentConfig
from .json_utils import JSONRepairUtils
from .schema_validator import SchemaValidator

class JsonSchemaRepairAgent(Agent):
    """Agent for performing static checks and LLM-based repair of malformed JSON or schema issues"""

    def __init__(self, config: AgentConfig):
        super().__init__(config)
        self.console = Console()

    def repair_json(self, raw_response: str, user_input: str) -> List[Dict[str, Any]]:
        """Repair JSON using libraries first, then LLM as fallback"""
        self.console.print("[DEBUG] Starting JSON repair process with libraries")

        # Step 1: Try library-based repair first
        cleaned, static_errors = JSONRepairUtils.repair_json_with_libraries(raw_response)
        self.console.print(f"[DEBUG] Static errors: {static_errors}")

        if not static_errors:
            try:
                task_data = json.loads(cleaned)
                if not isinstance(task_data, list):
                    task_data = self._fix_non_list_json(cleaned)
                
                # Step 2: Validate with libraries
                valid_tasks, schema_errors = SchemaValidator.validate_with_jsonschema(task_data)
                
                self.console.print(f"[DEBUG] Schema errors: {schema_errors}")
                self.console.print(f"[DEBUG] Valid tasks before repair: {len(valid_tasks)}")
                
                if not schema_errors:
                    return valid_tasks
                
            except json.JSONDecodeError as je:
                static_errors.append(f"JSON parsing failed: {str(je)}")
                task_data = []

        # Step 3: If issues persist, use LLM repair
        self.console.print("[DEBUG] Invoking LLM for repair")
        repaired_tasks = self._llm_repair(raw_response, user_input, static_errors, 
                                        schema_errors if 'schema_errors' in locals() else [], 
                                        task_data if 'task_data' in locals() else [])
        
        # Step 4: Final validation
        final_tasks = []
        for idx, task in enumerate(repaired_tasks):
            try:
                from .models import Task
                Task.model_validate(task)
                final_tasks.append(task)
            except Exception as ve:
                self.console.print(f"⚠️ Task {idx+1} still invalid after repair: {ve}")
                continue

        self.console.print(f"[DEBUG] Final repaired tasks: {len(final_tasks)}")
        return final_tasks if final_tasks else []

    def _fix_non_list_json(self, cleaned: str) -> List[Dict[str, Any]]:
        """Fix JSON that isn't a list"""
        try:
            data = json.loads(cleaned)
            if isinstance(data, dict):
                return [data]
            return []
        except json.JSONDecodeError:
            return []

    def _llm_repair(self, raw_response: str, user_input: str, static_errors: List[str], 
                   schema_errors: List[str], tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Use LLM to repair JSON and schema issues"""
        prompt = f"""
The following JSON response from a task decomposition is malformed or does not fully comply with the expected schema:
```
{raw_response}
```

Static check errors:
{json.dumps(static_errors, indent=2)}

Schema validation errors:
{json.dumps(schema_errors, indent=2)}

Original user input: '{user_input}'

Current tasks (may include invalid ones):
{json.dumps(tasks, indent=2)}

Repair the JSON to produce a valid list of tasks that matches the following schema:
- id: string (e.g., T001)
- name: string
- description: string
- dependencies: list of strings
- tools: list of strings (from {', '.join(SchemaValidator.AVAILABLE_TOOLS)})
- actions: list of objects with step (int), action (str), tool (str optional), purpose (str), sub_steps (list str), introspect_after (bool), system_prompt (str), user_prompt (str), introspect_prompt (str), resources (object with previous/required lists), execution_mode ("sequential"|"parallel")
- success_criteria: string
- expected_outputs: list of strings
- resources: object with previous/required lists

Rules:
- Preserve all information from the original response.
- Fix structural issues (e.g., missing brackets, invalid JSON).
- Correct schema issues (e.g., invalid execution_mode, missing fields) by providing sensible defaults or inferring from user_input.
- Ensure all tasks are valid and include all required fields.
- Do not discard any tasks unless absolutely unrecoverable.

Output a valid JSON array of tasks.
"""
        response = self._call_llm_with_retry(prompt)
        try:
            cleaned = JSONRepairUtils.clean_json_response(response)
            return json.loads(cleaned)
        except json.JSONDecodeError as je:
            self.console.print(f"⚠️ LLM repair failed: {je}")
            return tasks  # Return original tasks if repair fails

    def _call_llm_with_retry(self, prompt: str, max_retries: int = 3) -> str:
        """Call LLM with retry"""
        for attempt in range(max_retries):
            try:
                messages = [{"role": "user", "content": prompt}]
                response = self.llm_client.create_completion(messages=messages, stream=True)
                result = self.llm_client.handle_streaming_response(response)
                return result.get("content", "") if isinstance(result, dict) else str(result)
            except Exception as e:
                self.console.print(f"⚠️ LLM call failed (attempt {attempt+1}): {str(e)}")
                time.sleep(1)
        return ""

# ================================================================================
# execution_planner.py
from typing import List, Dict, Set
from .models import Task, ExecutionPlan

class ExecutionPlanner:
    """Handles execution plan generation from tasks"""
    
    @staticmethod
    def build_execution_plan(tasks: List[Task]) -> ExecutionPlan:
        """Build execution plan from tasks using topological sorting"""
        task_dict = {task.id: task for task in tasks}
        dep_graph = {task.id: set(task.dependencies) for task in tasks}
        
        # Topological sort for phases
        phases = []
        visited = set()
        independents = [tid for tid, deps in dep_graph.items() if not deps]
        
        while independents:
            phase = sorted(independents)
            phases.append(phase)
            visited.update(phase)
            new_independents = []
            for tid in list(dep_graph.keys()):
                if tid not in visited:
                    dep_graph[tid] -= set(phase)
                    if not dep_graph[tid]:
                        new_independents.append(tid)
            independents = new_independents
        
        parallel_groups = [phase for phase in phases if len(phase) > 1]
        critical_path = [tid for phase in phases for tid in phase[:1]]  # Simplified
        total_actions = sum(len(task.actions) for task in tasks)
        ordering = [tid for phase in phases for tid in phase]
        
        return ExecutionPlan(
            sequential_phases=phases,
            parallel_groups=parallel_groups,
            critical_path=critical_path,
            total_actions=total_actions,
            ordering=ordering
        )

# ================================================================================
# task_analyzer.py
import time
from typing import List, Dict, Any
from rich.console import Console

from agentic.core.agent import Agent, AgentConfig
from .models import Task, AnalysisResult, Resources, ActionStep, ExecutionMode
from .json_repair_agent import JsonSchemaRepairAgent
from .execution_planner import ExecutionPlanner
from .schema_validator import SchemaValidator

class TaskAnalyzer(Agent):
    """Task analyzer and decomposer for moderate to complex software engineering tasks"""

    def __init__(self, config: AgentConfig):
        super().__init__(config)
        self.console = Console()
        self.json_repair = JsonSchemaRepairAgent(config)

    @property
    def available_tools(self) -> List[str]:
        """Get available tools (removed code_interpreter)"""
        return SchemaValidator.AVAILABLE_TOOLS

    def analyze(self, user_input: str) -> AnalysisResult:
        """Analyze input and create task plan using LLM decomposition"""
        try:
            self.console.print("📋 Decomposing into tasks...")
            tasks = self._decompose_tasks(user_input)
            self.console.print(f"✅ Created {len(tasks)} tasks")

            self.console.print("🔄 Building execution plan...")
            execution_plan = ExecutionPlanner.build_execution_plan(tasks)
            self.console.print(f"✅ Execution plan ready with {execution_plan.total_actions} actions")

            tools_needed = list(set(tool for task in tasks for tool in task.tools))
            success_criteria = self._define_success_criteria(user_input, tasks)
            overall_resources = self._aggregate_resources(tasks)

            self.console.print("✅ Analysis complete!")

            return AnalysisResult(
                tasks=tasks,
                execution_plan=execution_plan,
                tools_needed=tools_needed,
                success_criteria=success_criteria,
                resources=overall_resources
            )

        except Exception as e:
            self.console.print(f"❌ Analysis error: {str(e)}")
            return self._create_fallback_result(user_input)

    def _decompose_tasks(self, user_input: str) -> List[Task]:
        """Decompose input into tasks using LLM with repair"""
        prompt = f"""
Decompose this software engineering task into a sequence of technical tasks: '{user_input}'

Available tools: {', '.join(self.available_tools)}

Rules:
- First task MUST be 'Requirement Analysis' using tools like introspect to parse and analyze the input technically.
- If the user input does not specify frameworks/libraries, in the Requirement Analysis task, propose a list of potential ones. Then, add a next task using 'debate_agent' to finalize selections based on technical criteria (e.g., performance, compatibility).
- Focus on technical decomposition only (e.g., code implementation, testing, deployment steps). No human-like actions like interviews.
- Prompts at subtask (action step) level: Each action step must have self-sufficient system_prompt (context, rules, prior progress) and user_prompt (instructions, details).
- After every subtask (action step), invoke 'introspect' with a structured introspect_prompt template including original task description, {{performed_action}}, evaluation criteria for correctness/completeness/alignment. If unsatisfactory, retry the action.
- For each task/subtask, identify dependencies/resources, sequence/parallel.
- Resources: Track previous created resources and required/helpful for current/next.

Generate a list of tasks in JSON format. Each task:
- id: string (e.g., T001)
- name: string (concise)
- description: string (detailed, technical)
- dependencies: list of strings (task IDs)
- tools: list of strings (from available tools)
- actions: list of objects with step (int), action (str), tool (str optional), purpose (str), sub_steps (list str), introspect_after (bool, default true), system_prompt (str), user_prompt (str), introspect_prompt (str template), resources (object with previous list str, required list str), execution_mode ("sequential"|"parallel")
- success_criteria: string (include retry if introspect fails)
- expected_outputs: list of strings
- resources: object with previous list str, required list str

Output as JSON array: [...]
"""
        response = self._call_llm_with_retry(prompt)
        self.console.print(f"[DEBUG] Raw LLM response: {response}")

        # Use JsonSchemaRepairAgent to check and repair
        task_data = self.json_repair.repair_json(response, user_input)
        
        tasks = []
        for data in task_data:
            tasks.append(Task(**data))
        return tasks if tasks else self._create_fallback_tasks(user_input)

    def _define_success_criteria(self, user_input: str, tasks: List[Task]) -> List[str]:
        """Define overall success criteria"""
        criteria = ["All technical subtasks completed with positive introspect feedback and retries if needed"]
        unique_criteria = set(task.success_criteria for task in tasks)
        criteria.extend(list(unique_criteria)[:5])
        return criteria

    def _aggregate_resources(self, tasks: List[Task]) -> Resources:
        """Aggregate overall resources"""
        previous = set()
        required = set()
        for task in tasks:
            previous.update(task.resources.previous)
            required.update(task.resources.required)
            for action in task.actions:
                previous.update(action.resources.previous)
                required.update(action.resources.required)
        return Resources(previous=list(previous), required=list(required))

    def _call_llm_with_retry(self, prompt: str, max_retries: int = 3) -> str:
        """Call LLM with retry on failure"""
        for attempt in range(max_retries):
            try:
                messages = [{"role": "user", "content": prompt}]
                response = self.llm_client.create_completion(messages=messages, stream=True)
                result = self.llm_client.handle_streaming_response(response)
                content = result.get("content", "") if isinstance(result, dict) else str(result)
                if content:
                    return content
            except Exception as e:
                self.console.print(f"⚠️ LLM call failed (attempt {attempt+1}): {str(e)}")
                time.sleep(1)
        return ""

    def _create_fallback_tasks(self, user_input: str) -> List[Task]:
        """Fallback tasks if decomposition fails"""
        return [Task(
            id="T001",
            name="Requirement Analysis and Execution",
            description=f"Analyze and execute the technical request: {user_input}",
            dependencies=[],
            tools=["introspect"],
            actions=[
                ActionStep(
                    step=1, 
                    action="Analyze requirements", 
                    tool="introspect", 
                    purpose="Parse technical needs", 
                    sub_steps=["Extract specs"], 
                    introspect_after=True,
                    system_prompt="You are a technical agent for software tasks. Focus on decomposition and tools.",
                    user_prompt=f"Analyze technical aspects of: {user_input}. Propose frameworks if unspecified.",
                    introspect_prompt="Evaluate {{performed_action}} against task '{user_input}'. Criteria: correctness, completeness, alignment. If unsatisfactory, retry.",
                    resources=Resources(previous=[], required=["user_input"]),
                    execution_mode=ExecutionMode.SEQUENTIAL
                )
            ],
            success_criteria="Technical requirements met with positive feedback; retry subtask if introspect fails",
            expected_outputs=["analysis", "implementation"],
            resources=Resources(previous=[], required=["user_input"])
        )]

    def _create_fallback_result(self, user_input: str) -> AnalysisResult:
        """Fallback result if analysis fails"""
        tasks = self._create_fallback_tasks(user_input)
        execution_plan = ExecutionPlanner.build_execution_plan(tasks)
        tools_needed = list(set(tool for task in tasks for tool in task.tools))
        success_criteria = self._define_success_criteria(user_input, tasks)
        overall_resources = self._aggregate_resources(tasks)
        return AnalysisResult(
            tasks=tasks,
            execution_plan=execution_plan,
            tools_needed=tools_needed,
            success_criteria=success_criteria,
            resources=overall_resources
        )

    def analyze_to_json(self, user_input: str) -> Dict[str, Any]:
        """Analyze and return JSON dict"""
        result = self.analyze(user_input)
        return result.model_dump(mode='json')

# ================================================================================
# __init__.py (Package initialization)
from .task_analyzer import TaskAnalyzer
from .models import Task, ActionStep, ExecutionPlan, AnalysisResult, Resources, ExecutionMode
from .json_repair_agent import JsonSchemaRepairAgent
from .schema_validator import SchemaValidator
from .execution_planner import ExecutionPlanner
from .json_utils import JSONRepairUtils

__all__ = [
    'TaskAnal