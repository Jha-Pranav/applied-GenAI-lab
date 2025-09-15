#!/usr/bin/env python3
"""
Task Analysis and Decomposition System
Main interface for analyzing procedure documents
"""
import asyncio
import sys
import os
import json
from pathlib import Path
from typing import Dict, Any
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from analyzer import TaskAnalyzer, TaskNode, AnalysisResult
from visualizer import FlowVisualizer

class TaskAnalysisSystem:
    def __init__(self):
        self.analyzer = TaskAnalyzer()
        self.visualizer = FlowVisualizer()
    
    async def analyze_document(self, document_path: str = None, document_text: str = None) -> Dict[str, Any]:
        """Analyze procedure document and create comprehensive breakdown"""
        
        # Load document
        if document_path:
            with open(document_path, 'r') as f:
                document = f.read()
        elif document_text:
            document = document_text
        else:
            raise ValueError("Either document_path or document_text must be provided")
        
        print("🧠 LLM Analyzing Procedure Document...")
        print("=" * 60)
        print(f"📄 Document Length: {len(document)} characters")
        print(f"📝 Lines: {len(document.split(chr(10)))}")
        print()
        
        # Step 1: Overall Analysis
        print("🔍 Step 1: Complexity Analysis...")
        analysis = await self.analyzer.analyze_procedure_document(document)
        
        # Step 2: Task Decomposition
        print("📋 Step 2: Task Decomposition...")
        tasks = await self.analyzer.decompose_into_tasks(document, analysis)
        
        # Step 3: Flow Creation
        print("🔄 Step 3: Execution Flow Creation...")
        flow = await self.analyzer.create_execution_flow(tasks)
        
        # Step 4: Metrics Calculation
        print("📊 Step 4: Metrics Calculation...")
        metrics = self.analyzer.calculate_metrics(tasks, flow)
        
        return {
            "document": document,
            "analysis": analysis,
            "tasks": tasks,
            "flow": flow,
            "metrics": metrics
        }
    
    def generate_reports(self, results: Dict[str, Any]) -> Dict[str, str]:
        """Generate all visualization reports"""
        
        tasks = results["tasks"]
        flow = results["flow"]
        metrics = results["metrics"]
        analysis = results["analysis"]
        
        reports = {}
        
        # Executive Dashboard
        reports["dashboard"] = self.visualizer.create_summary_dashboard(metrics, tasks, flow)
        
        # Flow Diagram
        reports["flow_diagram"] = self.visualizer.create_flow_diagram(tasks, flow)
        
        # Task Matrix
        reports["task_matrix"] = self.visualizer.create_task_matrix(tasks)
        
        # Gantt Chart
        reports["gantt_chart"] = self.visualizer.create_gantt_chart(tasks, flow)
        
        # Resource Allocation
        reports["resource_allocation"] = self.visualizer.create_resource_allocation(tasks, metrics)
        
        # Risk Assessment
        reports["risk_assessment"] = self.visualizer.create_risk_assessment(tasks)
        
        return reports
    
    def save_analysis(self, results: Dict[str, Any], reports: Dict[str, str], output_dir: str = "./analysis_output"):
        """Save analysis results and reports"""
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Save raw data
        with open(f"{output_dir}/analysis_data.json", "w") as f:
            # Convert TaskNode objects to dict for JSON serialization
            serializable_results = {
                "analysis": results["analysis"],
                "tasks": [
                    {
                        "id": task.id,
                        "name": task.name,
                        "description": task.description,
                        "complexity": task.complexity.value,
                        "estimated_hours": task.estimated_hours,
                        "dependencies": task.dependencies,
                        "parallel_group": task.parallel_group,
                        "agent_type": task.agent_type,
                        "validation_criteria": task.validation_criteria,
                        "risks": task.risks,
                        "deliverables": task.deliverables
                    }
                    for task in results["tasks"]
                ],
                "flow": results["flow"],
                "metrics": {
                    "overall_complexity": results["metrics"].overall_complexity.value,
                    "total_estimated_hours": results["metrics"].total_estimated_hours,
                    "critical_path_hours": results["metrics"].critical_path_hours,
                    "parallel_opportunities": results["metrics"].parallel_opportunities,
                    "risk_level": results["metrics"].risk_level,
                    "resource_requirements": results["metrics"].resource_requirements
                }
            }
            json.dump(serializable_results, f, indent=2)
        
        # Save reports
        for report_name, report_content in reports.items():
            with open(f"{output_dir}/{report_name}.txt", "w") as f:
                f.write(report_content)
        
        # Create comprehensive report
        comprehensive_report = []
        comprehensive_report.append("📊 COMPREHENSIVE TASK ANALYSIS REPORT")
        comprehensive_report.append("=" * 80)
        comprehensive_report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        comprehensive_report.append("")
        
        for report_name, report_content in reports.items():
            comprehensive_report.append(f"\n{report_content}\n")
            comprehensive_report.append("=" * 80)
        
        with open(f"{output_dir}/comprehensive_report.txt", "w") as f:
            f.write("\n".join(comprehensive_report))
        
        print(f"📁 Analysis saved to: {output_dir}")
        return output_dir

async def main():
    """Main CLI interface"""
    system = TaskAnalysisSystem()
    
    print("📊 Task Analysis and Decomposition System")
    print("=" * 60)
    
    if len(sys.argv) > 1:
        # File mode
        document_path = sys.argv[1]
        if not os.path.exists(document_path):
            print(f"❌ File not found: {document_path}")
            return
        
        print(f"📄 Analyzing document: {document_path}")
        results = await system.analyze_document(document_path=document_path)
        
    else:
        # Interactive mode
        print("Enter your procedure document (end with '###' on a new line):")
        lines = []
        while True:
            try:
                line = input()
                if line.strip() == "###":
                    break
                lines.append(line)
            except EOFError:
                break
        
        document_text = "\n".join(lines)
        if not document_text.strip():
            print("❌ No document provided")
            return
        
        results = await system.analyze_document(document_text=document_text)
    
    # Generate reports
    print("\n📊 Generating Analysis Reports...")
    reports = system.generate_reports(results)
    
    # Display results
    print("\n" + reports["dashboard"])
    print("\n" + reports["flow_diagram"])
    print("\n" + reports["task_matrix"])
    
    # Save analysis
    output_dir = system.save_analysis(results, reports)
    
    print(f"\n✅ Analysis Complete!")
    print(f"📁 Full reports saved to: {output_dir}")
    print(f"📊 Tasks identified: {len(results['tasks'])}")
    print(f"⏱️ Total estimated time: {results['metrics'].total_estimated_hours:.1f} hours")
    print(f"🎯 Critical path: {results['metrics'].critical_path_hours:.1f} hours")

if __name__ == "__main__":
    asyncio.run(main())
