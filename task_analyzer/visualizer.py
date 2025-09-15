"""
Flow Diagram Visualizer for Task Analysis
Creates ASCII and structured visual representations
"""
from typing import Dict, List, Any
from analyzer import TaskNode, AnalysisResult

class FlowVisualizer:
    def __init__(self):
        self.colors = {
            "trivial": "🟢",
            "simple": "🔵", 
            "moderate": "🟡",
            "complex": "🟠",
            "enterprise": "🔴"
        }
        
        self.agent_icons = {
            "developer": "👨‍💻",
            "tester": "🧪",
            "devops": "⚙️",
            "designer": "🎨",
            "analyst": "📊"
        }
    
    def create_flow_diagram(self, tasks: List[TaskNode], flow: Dict[str, Any]) -> str:
        """Create ASCII flow diagram"""
        diagram = []
        diagram.append("📊 TASK EXECUTION FLOW DIAGRAM")
        diagram.append("=" * 80)
        
        phases = flow.get("phases", [])
        
        for phase in phases:
            phase_num = phase.get("phase_number", 1)
            phase_name = phase.get("phase_name", "Unknown Phase")
            phase_duration = phase.get("phase_duration", 0)
            
            diagram.append(f"\n🔸 PHASE {phase_num}: {phase_name}")
            diagram.append(f"   Duration: {phase_duration}h")
            diagram.append("   " + "─" * 60)
            
            parallel_tasks = phase.get("parallel_tasks", [])
            
            if len(parallel_tasks) == 1:
                # Single task
                task = parallel_tasks[0]
                icon = self.agent_icons.get(task.get("agent_type", "developer"), "👤")
                diagram.append(f"   │")
                diagram.append(f"   ├─ {icon} {task.get('task_name', 'Unknown')} ({task.get('estimated_hours', 0)}h)")
                diagram.append(f"   │")
            else:
                # Parallel tasks
                diagram.append(f"   │")
                diagram.append(f"   ├─ PARALLEL EXECUTION ({len(parallel_tasks)} tasks)")
                for i, task in enumerate(parallel_tasks):
                    icon = self.agent_icons.get(task.get("agent_type", "developer"), "👤")
                    connector = "├─" if i < len(parallel_tasks) - 1 else "└─"
                    diagram.append(f"   │  {connector} {icon} {task.get('task_name', 'Unknown')} ({task.get('estimated_hours', 0)}h)")
                diagram.append(f"   │")
        
        # Add critical path
        critical_path = flow.get("critical_path", [])
        if critical_path:
            diagram.append(f"\n🎯 CRITICAL PATH:")
            diagram.append("   " + " → ".join(critical_path))
        
        # Add parallel streams
        parallel_streams = flow.get("parallel_streams", [])
        if parallel_streams:
            diagram.append(f"\n🔀 PARALLEL STREAMS:")
            for stream in parallel_streams:
                stream_name = stream.get("stream_name", "Unknown")
                duration = stream.get("total_duration", 0)
                diagram.append(f"   • {stream_name}: {duration}h")
        
        # Add bottlenecks
        bottlenecks = flow.get("bottlenecks", [])
        if bottlenecks:
            diagram.append(f"\n⚠️ BOTTLENECKS:")
            for bottleneck in bottlenecks:
                diagram.append(f"   • {bottleneck}")
        
        return "\n".join(diagram)
    
    def create_task_matrix(self, tasks: List[TaskNode]) -> str:
        """Create task dependency matrix"""
        matrix = []
        matrix.append("📋 TASK DEPENDENCY MATRIX")
        matrix.append("=" * 100)
        
        # Header
        header = f"{'ID':<15} {'Name':<25} {'Complexity':<12} {'Hours':<8} {'Agent':<12} {'Dependencies':<20}"
        matrix.append(header)
        matrix.append("-" * 100)
        
        # Tasks
        for task in tasks:
            complexity_icon = self.colors.get(task.complexity.value, "⚪")
            agent_icon = self.agent_icons.get(task.agent_type, "👤")
            deps = ", ".join(task.dependencies) if task.dependencies else "None"
            
            row = f"{task.id:<15} {task.name[:24]:<25} {complexity_icon} {task.complexity.value:<10} {task.estimated_hours:<8.1f} {agent_icon} {task.agent_type:<10} {deps[:19]:<20}"
            matrix.append(row)
        
        return "\n".join(matrix)
    
    def create_gantt_chart(self, tasks: List[TaskNode], flow: Dict[str, Any]) -> str:
        """Create ASCII Gantt chart representation"""
        gantt = []
        gantt.append("📅 GANTT CHART VISUALIZATION")
        gantt.append("=" * 80)
        
        phases = flow.get("phases", [])
        total_duration = sum(phase.get("phase_duration", 0) for phase in phases)
        
        if total_duration == 0:
            return "No timeline data available"
        
        # Create timeline
        timeline_width = 60
        current_time = 0
        
        gantt.append(f"Timeline: 0h {'─' * (timeline_width-10)} {total_duration}h")
        gantt.append("")
        
        for phase in phases:
            phase_name = phase.get("phase_name", "Unknown")
            phase_duration = phase.get("phase_duration", 0)
            
            # Calculate bar length
            bar_length = int((phase_duration / total_duration) * timeline_width)
            bar = "█" * bar_length
            
            gantt.append(f"{phase_name[:20]:<20} │{bar:<{timeline_width}}│ {phase_duration}h")
            
            # Show parallel tasks within phase
            parallel_tasks = phase.get("parallel_tasks", [])
            for task in parallel_tasks:
                task_name = task.get("task_name", "Unknown")[:18]
                task_hours = task.get("estimated_hours", 0)
                task_bar_length = int((task_hours / total_duration) * timeline_width)
                task_bar = "▓" * task_bar_length
                
                gantt.append(f"  └─ {task_name:<16} │{task_bar:<{timeline_width}}│ {task_hours}h")
            
            gantt.append("")
        
        return "\n".join(gantt)
    
    def create_resource_allocation(self, tasks: List[TaskNode], analysis: AnalysisResult) -> str:
        """Create resource allocation visualization"""
        resource = []
        resource.append("👥 RESOURCE ALLOCATION")
        resource.append("=" * 50)
        
        # Agent workload
        agent_hours = {}
        for task in tasks:
            agent_hours[task.agent_type] = agent_hours.get(task.agent_type, 0) + task.estimated_hours
        
        total_hours = sum(agent_hours.values())
        
        for agent_type, hours in agent_hours.items():
            icon = self.agent_icons.get(agent_type, "👤")
            percentage = (hours / total_hours) * 100 if total_hours > 0 else 0
            bar_length = int(percentage / 5)  # Scale to 20 chars max
            bar = "█" * bar_length
            
            resource.append(f"{icon} {agent_type.capitalize():<12} │{bar:<20}│ {hours:>6.1f}h ({percentage:>5.1f}%)")
        
        # Complexity distribution
        resource.append(f"\n🎯 COMPLEXITY DISTRIBUTION")
        resource.append("-" * 30)
        
        complexity_count = {}
        for task in tasks:
            complexity_count[task.complexity.value] = complexity_count.get(task.complexity.value, 0) + 1
        
        total_tasks = len(tasks)
        for complexity, count in complexity_count.items():
            icon = self.colors.get(complexity, "⚪")
            percentage = (count / total_tasks) * 100 if total_tasks > 0 else 0
            bar_length = int(percentage / 5)
            bar = "█" * bar_length
            
            resource.append(f"{icon} {complexity.capitalize():<12} │{bar:<20}│ {count:>3} tasks ({percentage:>5.1f}%)")
        
        return "\n".join(resource)
    
    def create_risk_assessment(self, tasks: List[TaskNode]) -> str:
        """Create risk assessment visualization"""
        risk = []
        risk.append("⚠️ RISK ASSESSMENT")
        risk.append("=" * 50)
        
        # Collect all risks
        all_risks = []
        for task in tasks:
            for risk_item in task.risks:
                all_risks.append({
                    "task": task.name,
                    "risk": risk_item,
                    "complexity": task.complexity.value
                })
        
        if not all_risks:
            risk.append("✅ No specific risks identified")
            return "\n".join(risk)
        
        # Group by risk level
        high_risk_tasks = [task for task in tasks if task.complexity.value in ["complex", "enterprise"]]
        medium_risk_tasks = [task for task in tasks if task.complexity.value == "moderate"]
        low_risk_tasks = [task for task in tasks if task.complexity.value in ["simple", "trivial"]]
        
        if high_risk_tasks:
            risk.append("🔴 HIGH RISK TASKS:")
            for task in high_risk_tasks:
                risk.append(f"   • {task.name} ({task.estimated_hours}h)")
                for risk_item in task.risks:
                    risk.append(f"     - {risk_item}")
        
        if medium_risk_tasks:
            risk.append("\n🟡 MEDIUM RISK TASKS:")
            for task in medium_risk_tasks:
                risk.append(f"   • {task.name} ({task.estimated_hours}h)")
        
        if low_risk_tasks:
            risk.append(f"\n🟢 LOW RISK TASKS: {len(low_risk_tasks)} tasks")
        
        return "\n".join(risk)
    
    def create_summary_dashboard(self, analysis: AnalysisResult, tasks: List[TaskNode], flow: Dict[str, Any]) -> str:
        """Create executive summary dashboard"""
        dashboard = []
        dashboard.append("📊 PROJECT ANALYSIS DASHBOARD")
        dashboard.append("=" * 80)
        
        # Key metrics
        dashboard.append("🎯 KEY METRICS:")
        dashboard.append(f"   • Overall Complexity: {analysis.overall_complexity.value.upper()}")
        dashboard.append(f"   • Total Estimated Hours: {analysis.total_estimated_hours:.1f}h")
        dashboard.append(f"   • Critical Path Duration: {analysis.critical_path_hours:.1f}h")
        dashboard.append(f"   • Parallel Opportunities: {analysis.parallel_opportunities}")
        dashboard.append(f"   • Risk Level: {analysis.risk_level.upper()}")
        dashboard.append(f"   • Total Tasks: {len(tasks)}")
        
        # Time savings
        sequential_time = analysis.total_estimated_hours
        parallel_time = analysis.critical_path_hours
        time_saved = sequential_time - parallel_time
        savings_percentage = (time_saved / sequential_time) * 100 if sequential_time > 0 else 0
        
        dashboard.append(f"\n⚡ PARALLELIZATION BENEFITS:")
        dashboard.append(f"   • Sequential Execution: {sequential_time:.1f}h")
        dashboard.append(f"   • Parallel Execution: {parallel_time:.1f}h")
        dashboard.append(f"   • Time Saved: {time_saved:.1f}h ({savings_percentage:.1f}%)")
        
        # Resource requirements
        dashboard.append(f"\n👥 RESOURCE REQUIREMENTS:")
        for agent_type, count in analysis.resource_requirements.items():
            icon = self.agent_icons.get(agent_type, "👤")
            dashboard.append(f"   • {icon} {agent_type.capitalize()}: {count} tasks")
        
        return "\n".join(dashboard)
