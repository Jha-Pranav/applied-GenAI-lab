"""
LLM-Powered Task Analysis and Decomposition System
Handles full procedure documents and creates visual flow diagrams
"""
import json
import requests
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum

class ComplexityLevel(Enum):
    TRIVIAL = "trivial"
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"
    ENTERPRISE = "enterprise"

@dataclass
class TaskNode:
    id: str
    name: str
    description: str
    complexity: ComplexityLevel
    estimated_hours: float
    dependencies: List[str]
    parallel_group: int
    agent_type: str
    validation_criteria: str
    risks: List[str]
    deliverables: List[str]

@dataclass
class AnalysisResult:
    overall_complexity: ComplexityLevel
    total_estimated_hours: float
    critical_path_hours: float
    parallel_opportunities: int
    risk_level: str
    technology_stack: List[str]
    resource_requirements: Dict[str, int]
    success_criteria: List[str]

class TaskAnalyzer:
    def __init__(self, ollama_url: str = "http://localhost:11434"):
        self.ollama_url = ollama_url
        self.model = "gpt-oss:20b"
    
    async def analyze_procedure_document(self, document: str) -> Dict[str, Any]:
        """Analyze full procedure document for complexity and requirements"""
        
        analysis_prompt = f"""
Analyze this complete procedure document and provide detailed analysis:

DOCUMENT:
{document}

Respond with JSON only:
{{
    "overall_complexity": "trivial/simple/moderate/complex/enterprise",
    "total_estimated_hours": number,
    "critical_path_hours": number,
    "parallel_opportunities": number,
    "risk_level": "low/medium/high/critical",
    "technology_stack": ["list", "of", "technologies"],
    "resource_requirements": {{
        "developers": number,
        "testers": number,
        "devops": number,
        "designers": number
    }},
    "success_criteria": ["list", "of", "criteria"],
    "key_challenges": ["list", "of", "challenges"],
    "recommended_approach": "description"
}}

Consider:
- Document length and detail level
- Technical complexity
- Integration requirements
- Testing needs
- Deployment complexity
"""
        
        response = await self._call_llm(analysis_prompt)
        return self._parse_json_response(response)
    
    async def decompose_into_tasks(self, document: str, analysis: Dict[str, Any]) -> List[TaskNode]:
        """Decompose procedure document into detailed task breakdown"""
        
        decomposition_prompt = f"""
Break down this procedure document into detailed atomic tasks:

DOCUMENT:
{document}

ANALYSIS CONTEXT:
{json.dumps(analysis, indent=2)}

Create a comprehensive task breakdown as JSON array:
[
    {{
        "id": "unique_task_id",
        "name": "Task Name",
        "description": "Detailed description of what needs to be done",
        "complexity": "trivial/simple/moderate/complex/enterprise",
        "estimated_hours": number,
        "dependencies": ["list_of_task_ids"],
        "parallel_group": number,
        "agent_type": "developer/tester/devops/designer/analyst",
        "validation_criteria": "How to verify completion",
        "risks": ["potential", "risks"],
        "deliverables": ["expected", "outputs"]
    }}
]

Requirements:
- Break into atomic, executable tasks
- Identify all dependencies correctly
- Group parallel tasks with same parallel_group number
- Include realistic time estimates
- Consider all aspects: development, testing, deployment, documentation
- Include risk assessment for each task
"""
        
        response = await self._call_llm(decomposition_prompt)
        tasks_data = self._parse_json_response(response)
        
        if isinstance(tasks_data, list):
            tasks = []
            for task_data in tasks_data:
                task = TaskNode(
                    id=task_data.get("id", f"task_{len(tasks)+1}"),
                    name=task_data.get("name", "Unnamed Task"),
                    description=task_data.get("description", ""),
                    complexity=ComplexityLevel(task_data.get("complexity", "simple")),
                    estimated_hours=float(task_data.get("estimated_hours", 1.0)),
                    dependencies=task_data.get("dependencies", []),
                    parallel_group=int(task_data.get("parallel_group", 0)),
                    agent_type=task_data.get("agent_type", "developer"),
                    validation_criteria=task_data.get("validation_criteria", "Task completed"),
                    risks=task_data.get("risks", []),
                    deliverables=task_data.get("deliverables", [])
                )
                tasks.append(task)
            return tasks
        
        return []
    
    async def create_execution_flow(self, tasks: List[TaskNode]) -> Dict[str, Any]:
        """Create execution flow with dependency visualization"""
        
        flow_prompt = f"""
Create an execution flow diagram for these tasks:

TASKS:
{json.dumps([{
    "id": task.id,
    "name": task.name,
    "dependencies": task.dependencies,
    "parallel_group": task.parallel_group,
    "estimated_hours": task.estimated_hours,
    "agent_type": task.agent_type
} for task in tasks], indent=2)}

Generate flow diagram as JSON:
{{
    "phases": [
        {{
            "phase_number": 1,
            "phase_name": "Phase Name",
            "parallel_tasks": [
                {{
                    "task_id": "task_id",
                    "task_name": "Task Name",
                    "estimated_hours": number,
                    "agent_type": "type"
                }}
            ],
            "phase_duration": number,
            "dependencies_from_previous": ["task_ids"]
        }}
    ],
    "critical_path": ["task_id_1", "task_id_2", "..."],
    "parallel_streams": [
        {{
            "stream_name": "Stream Name",
            "tasks": ["task_ids"],
            "total_duration": number
        }}
    ],
    "bottlenecks": ["task_ids_that_block_others"],
    "optimization_suggestions": ["suggestions"]
}}

Organize tasks into logical phases based on dependencies and parallel execution opportunities.
"""
        
        response = await self._call_llm(flow_prompt)
        return self._parse_json_response(response)
    
    async def _call_llm(self, prompt: str) -> str:
        """Call Ollama LLM with increased timeout"""
        try:
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.1,
                        "top_p": 0.9
                    }
                },
                timeout=180  # 3 minutes for complex analysis
            )
            
            if response.status_code == 200:
                return response.json().get("response", "")
            else:
                raise Exception(f"LLM call failed: {response.status_code}")
                
        except Exception as e:
            print(f"LLM call error: {e}")
            return "{}"
    
    def _parse_json_response(self, response: str) -> Dict[str, Any]:
        """Parse JSON from LLM response"""
        try:
            response = response.strip()
            if "```json" in response:
                start = response.find("```json") + 7
                end = response.find("```", start)
                response = response[start:end].strip()
            elif "```" in response:
                start = response.find("```") + 3
                end = response.find("```", start)
                response = response[start:end].strip()
            
            return json.loads(response)
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            print(f"Response: {response[:500]}...")
            return {}
    
    def calculate_metrics(self, tasks: List[TaskNode], flow: Dict[str, Any]) -> AnalysisResult:
        """Calculate project metrics"""
        total_hours = sum(task.estimated_hours for task in tasks)
        
        # Calculate critical path
        critical_path_tasks = flow.get("critical_path", [])
        critical_path_hours = sum(
            task.estimated_hours for task in tasks 
            if task.id in critical_path_tasks
        )
        
        # Count parallel opportunities
        parallel_groups = set(task.parallel_group for task in tasks)
        parallel_opportunities = len(parallel_groups) - 1  # Subtract 1 for sequential tasks
        
        # Determine overall complexity
        if not tasks:
            overall_complexity = ComplexityLevel.TRIVIAL
        else:
            complexity_scores = {
                ComplexityLevel.TRIVIAL: 1,
                ComplexityLevel.SIMPLE: 2,
                ComplexityLevel.MODERATE: 3,
                ComplexityLevel.COMPLEX: 4,
                ComplexityLevel.ENTERPRISE: 5
            }
            
            avg_complexity = sum(complexity_scores[task.complexity] for task in tasks) / len(tasks)
        if avg_complexity <= 1.5:
            overall_complexity = ComplexityLevel.TRIVIAL
        elif avg_complexity <= 2.5:
            overall_complexity = ComplexityLevel.SIMPLE
        elif avg_complexity <= 3.5:
            overall_complexity = ComplexityLevel.MODERATE
        elif avg_complexity <= 4.5:
            overall_complexity = ComplexityLevel.COMPLEX
        else:
            overall_complexity = ComplexityLevel.ENTERPRISE
        
        # Calculate resource requirements
        agent_counts = {}
        for task in tasks:
            agent_counts[task.agent_type] = agent_counts.get(task.agent_type, 0) + 1
        
        # Risk assessment
        total_risks = sum(len(task.risks) for task in tasks)
        if total_risks <= len(tasks) * 0.5:
            risk_level = "low"
        elif total_risks <= len(tasks) * 1.5:
            risk_level = "medium"
        elif total_risks <= len(tasks) * 2.5:
            risk_level = "high"
        else:
            risk_level = "critical"
        
        return AnalysisResult(
            overall_complexity=overall_complexity,
            total_estimated_hours=total_hours,
            critical_path_hours=critical_path_hours,
            parallel_opportunities=parallel_opportunities,
            risk_level=risk_level,
            technology_stack=[],  # Will be filled from document analysis
            resource_requirements=agent_counts,
            success_criteria=[]  # Will be filled from document analysis
        )
