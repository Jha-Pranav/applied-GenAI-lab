#!/usr/bin/env python3
"""
Comprehensive Buddy AI Test Suite
Tests all tools, scenarios, and edge cases with 50 diverse prompts
Captures input/output in JSON format for evaluation
"""

import subprocess
import time
import json
import os
from datetime import datetime

# 50 comprehensive test prompts covering all tools and scenarios
TEST_PROMPTS = [
    # === fs_read Tool Tests (8 prompts) ===
    {"id": 1, "prompt": "list all files in current directory", "expected_tool": "fs_read", "category": "file_operations"},
    {"id": 2, "prompt": "show me the contents of main.py", "expected_tool": "fs_read", "category": "file_operations"},
    {"id": 3, "prompt": "find all .py files in the project", "expected_tool": "fs_read", "category": "file_operations"},
    {"id": 4, "prompt": "search for 'import' in all python files", "expected_tool": "fs_read", "category": "file_operations"},
    {"id": 5, "prompt": "read the first 10 lines of README.md", "expected_tool": "fs_read", "category": "file_operations"},
    {"id": 6, "prompt": "show directory structure with depth 2", "expected_tool": "fs_read", "category": "file_operations"},
    {"id": 7, "prompt": "check if pyproject.toml exists", "expected_tool": "fs_read", "category": "file_operations"},
    {"id": 8, "prompt": "count total lines in all .toml files", "expected_tool": "fs_read", "category": "file_operations"},

    # === fs_write Tool Tests (8 prompts) ===
    {"id": 9, "prompt": "create a file called test_hello.py with print('Hello World')", "expected_tool": "fs_write", "category": "file_creation"},
    {"id": 10, "prompt": "write a simple calculator function and save to calculator.py", "expected_tool": "fs_write", "category": "file_creation"},
    {"id": 11, "prompt": "create a JSON config file with sample data", "expected_tool": "fs_write", "category": "file_creation"},
    {"id": 12, "prompt": "write a class Person with name and age attributes to person.py", "expected_tool": "fs_write", "category": "file_creation"},
    {"id": 13, "prompt": "create a requirements.txt file with common packages", "expected_tool": "fs_write", "category": "file_creation"},
    {"id": 14, "prompt": "write a factorial function using recursion to factorial.py", "expected_tool": "fs_write", "category": "file_creation"},
    {"id": 15, "prompt": "create a simple Flask app and save to app.py", "expected_tool": "fs_write", "category": "file_creation"},
    {"id": 16, "prompt": "write a CSV parser function to csv_parser.py", "expected_tool": "fs_write", "category": "file_creation"},

    # === execute_bash Tool Tests (8 prompts) ===
    {"id": 17, "prompt": "show current working directory", "expected_tool": "execute_bash", "category": "system_operations"},
    {"id": 18, "prompt": "list all processes with 'python' in name", "expected_tool": "execute_bash", "category": "system_operations"},
    {"id": 19, "prompt": "check available disk space", "expected_tool": "execute_bash", "category": "system_operations"},
    {"id": 20, "prompt": "show current date and time", "expected_tool": "execute_bash", "category": "system_operations"},
    {"id": 21, "prompt": "check if git is installed", "expected_tool": "execute_bash", "category": "system_operations"},
    {"id": 22, "prompt": "show system memory usage", "expected_tool": "execute_bash", "category": "system_operations"},
    {"id": 23, "prompt": "list environment variables containing PATH", "expected_tool": "execute_bash", "category": "system_operations"},
    {"id": 24, "prompt": "create a new directory called test_folder", "expected_tool": "execute_bash", "category": "system_operations"},

    # === code_interpreter Tool Tests (6 prompts) ===
    {"id": 25, "prompt": "calculate 127 * 89 + 456", "expected_tool": "code_interpreter", "category": "calculations"},
    {"id": 26, "prompt": "generate fibonacci sequence first 15 numbers", "expected_tool": "code_interpreter", "category": "calculations"},
    {"id": 27, "prompt": "create a plot of sine wave from 0 to 2π", "expected_tool": "code_interpreter", "category": "calculations"},
    {"id": 28, "prompt": "calculate statistics for list [1,2,3,4,5,6,7,8,9,10]", "expected_tool": "code_interpreter", "category": "calculations"},
    {"id": 29, "prompt": "solve quadratic equation: x² + 5x + 6 = 0", "expected_tool": "code_interpreter", "category": "calculations"},
    {"id": 30, "prompt": "generate random numbers and calculate their mean", "expected_tool": "code_interpreter", "category": "calculations"},

    # === task_planner Tool Tests (6 prompts) ===
    {"id": 31, "prompt": "build a complete web application with authentication and database", "expected_tool": "task_planner", "category": "complex_tasks"},
    {"id": 32, "prompt": "create a machine learning pipeline for data classification", "expected_tool": "task_planner", "category": "complex_tasks"},
    {"id": 33, "prompt": "setup a CI/CD pipeline with testing and deployment", "expected_tool": "task_planner", "category": "complex_tasks"},
    {"id": 34, "prompt": "develop a REST API with multiple endpoints and documentation", "expected_tool": "task_planner", "category": "complex_tasks"},
    {"id": 35, "prompt": "create a microservices architecture with Docker containers", "expected_tool": "task_planner", "category": "complex_tasks"},
    {"id": 36, "prompt": "build a data processing system with ETL pipeline", "expected_tool": "task_planner", "category": "complex_tasks"},

    # === introspect Tool Tests (4 prompts) ===
    {"id": 37, "prompt": "analyze the quality of code in this project", "expected_tool": "introspect", "category": "analysis"},
    {"id": 38, "prompt": "review the project structure and suggest improvements", "expected_tool": "introspect", "category": "analysis"},
    {"id": 39, "prompt": "validate the current configuration and settings", "expected_tool": "introspect", "category": "analysis"},
    {"id": 40, "prompt": "assess the completeness of this implementation", "expected_tool": "introspect", "category": "analysis"},

    # === Multiple Tools / Complex Scenarios (5 prompts) ===
    {"id": 41, "prompt": "create a Python script, test it, and document the results", "expected_tool": "multiple", "category": "multi_tool"},
    {"id": 42, "prompt": "analyze existing code and create an improved version", "expected_tool": "multiple", "category": "multi_tool"},
    {"id": 43, "prompt": "setup project structure and create sample files", "expected_tool": "multiple", "category": "multi_tool"},
    {"id": 44, "prompt": "read configuration, modify it, and save changes", "expected_tool": "multiple", "category": "multi_tool"},
    {"id": 45, "prompt": "generate test data, process it, and create visualization", "expected_tool": "multiple", "category": "multi_tool"},

    # === Edge Cases & Error Handling (5 prompts) ===
    {"id": 46, "prompt": "read a file that doesn't exist: nonexistent.txt", "expected_tool": "fs_read", "category": "edge_cases"},
    {"id": 47, "prompt": "execute invalid command: invalidcommand123", "expected_tool": "execute_bash", "category": "edge_cases"},
    {"id": 48, "prompt": "calculate division by zero: 10/0", "expected_tool": "code_interpreter", "category": "edge_cases"},
    {"id": 49, "prompt": "create file with invalid path: /root/restricted/file.txt", "expected_tool": "fs_write", "category": "edge_cases"},
    {"id": 50, "prompt": "hello world", "expected_tool": "none", "category": "simple_response"}
]

def extract_tool_usage(stdout_text):
    """Extract which tools were actually used from stdout"""
    tools_used = []
    
    # Look for tool execution indicators
    tool_indicators = {
        "fs_read": ["✅ fs_read completed", "Executing fs_read"],
        "fs_write": ["✅ fs_write completed", "Executing fs_write"],
        "execute_bash": ["✅ execute_bash completed", "Executing execute_bash"],
        "code_interpreter": ["✅ code_interpreter completed", "Executing code_interpreter"],
        "task_planner": ["✅ task_planner completed", "Executing task_planner"],
        "introspect": ["✅ introspect completed", "Executing introspect"],
        "debate_agent": ["✅ debate_agent completed", "Executing debate_agent"]
    }
    
    for tool, indicators in tool_indicators.items():
        if any(indicator in stdout_text for indicator in indicators):
            tools_used.append(tool)
    
    return tools_used if tools_used else ["none"]

def evaluate_test_result(test_case, cleaned_stdout, stderr, returncode, execution_time):
    """Evaluate test result and assign score"""
    
    # Extract tools used from cleaned stdout
    tools_used = extract_tool_usage(cleaned_stdout)
    expected_tool = test_case["expected_tool"]
    
    # Basic scoring
    score = 0
    status = "FAILED"
    issues = []
    
    # Check if execution succeeded
    if returncode != 0:
        issues.append("Non-zero exit code")
        return {
            "score": 0,
            "status": "FAILED",
            "tools_used": tools_used,
            "expected_tool": expected_tool,
            "tool_match": False,
            "issues": issues,
            "execution_time": execution_time
        }
    
    # Check if expected tool was used
    tool_match = False
    if expected_tool == "none":
        tool_match = tools_used == ["none"]
    elif expected_tool == "multiple":
        tool_match = len(tools_used) > 1
    else:
        tool_match = expected_tool in tools_used
    
    # Score based on tool usage
    if tool_match:
        score += 5
    else:
        issues.append(f"Expected {expected_tool}, got {tools_used}")
    
    # Check output quality
    if cleaned_stdout and len(cleaned_stdout.strip()) > 20:
        score += 3
    else:
        issues.append("Insufficient output")
    
    # Check for errors in output
    error_keywords = ["error:", "failed:", "exception:", "traceback"]
    if any(keyword in cleaned_stdout.lower() for keyword in error_keywords):
        score -= 2
        issues.append("Errors in output")
    
    # Performance scoring
    if execution_time < 30:
        score += 2
    elif execution_time > 60:
        score -= 1
        issues.append("Slow execution")
    
    # Determine status
    if score >= 8:
        status = "SUCCESS"
    elif score >= 5:
        status = "PARTIAL"
    else:
        status = "FAILED"
    
    return {
        "score": max(0, min(10, score)),
        "status": status,
        "tools_used": tools_used,
        "expected_tool": expected_tool,
        "tool_match": tool_match,
        "issues": issues,
        "execution_time": execution_time
    }

def clean_stdout(stdout_text):
    """Clean stdout from ANSI escape sequences and special characters"""
    import re
    
    # Remove ANSI escape sequences (colors, formatting)
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    cleaned = ansi_escape.sub('', stdout_text)
    
    # Remove other control characters but keep newlines and tabs
    cleaned = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', cleaned)
    
    return cleaned

def run_single_test(test_case):
    """Run a single test case"""
    print(f"\n{'='*80}")
    print(f"TEST {test_case['id']}/50: {test_case['prompt']}")
    print(f"Expected Tool: {test_case['expected_tool']} | Category: {test_case['category']}")
    print('='*80)
    
    start_time = time.time()
    
    try:
        result = subprocess.run(
            ["uv", "run", "main.py", "-c", test_case["prompt"]],
            cwd="/home/pranav-pc/projects/applied-GenAI-lab",
            capture_output=True,
            text=True,
            timeout=120  # 2 minute timeout
        )
        
        execution_time = time.time() - start_time
        
        # Clean stdout from ANSI escape sequences completely
        cleaned_stdout = clean_stdout(result.stdout)
        cleaned_stderr = clean_stdout(result.stderr)
        
        # Evaluate result
        evaluation = evaluate_test_result(
            test_case, cleaned_stdout, cleaned_stderr, result.returncode, execution_time
        )
        
        # Display result
        status_emoji = {"SUCCESS": "✅", "PARTIAL": "⚠️", "FAILED": "❌"}
        print(f"{status_emoji[evaluation['status']]} {evaluation['status']} "
              f"(Score: {evaluation['score']}/10, Time: {execution_time:.1f}s)")
        print(f"Tools Used: {evaluation['tools_used']}")
        
        if evaluation['issues']:
            print(f"Issues: {', '.join(evaluation['issues'])}")
        
        # Show output sample (but save full cleaned output)
        if cleaned_stdout:
            lines = [line.strip() for line in cleaned_stdout.split('\n') if line.strip()]
            if lines:
                sample = lines[-1][:100] + "..." if len(lines[-1]) > 100 else lines[-1]
                print(f"Output Sample: {sample}")
        
        return {
            "test_id": test_case["id"],
            "prompt": test_case["prompt"],
            "expected_tool": test_case["expected_tool"],
            "category": test_case["category"],
            "execution_time": execution_time,
            "returncode": result.returncode,
            "stdout": cleaned_stdout,  # Clean stdout without ANSI codes
            "stderr": cleaned_stderr,  # Clean stderr without ANSI codes
            "evaluation": evaluation,
            "timestamp": datetime.now().isoformat()
        }
        
    except subprocess.TimeoutExpired:
        print("⏰ TIMEOUT - Test exceeded 2 minutes")
        return {
            "test_id": test_case["id"],
            "prompt": test_case["prompt"],
            "expected_tool": test_case["expected_tool"],
            "category": test_case["category"],
            "execution_time": 120,
            "returncode": -1,
            "stdout": "",
            "stderr": "Test timeout after 120 seconds",
            "evaluation": {
                "score": 0,
                "status": "TIMEOUT",
                "tools_used": [],
                "expected_tool": test_case["expected_tool"],
                "tool_match": False,
                "issues": ["Timeout"],
                "execution_time": 120
            },
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        print(f"💥 EXCEPTION: {e}")
        return {
            "test_id": test_case["id"],
            "prompt": test_case["prompt"],
            "expected_tool": test_case["expected_tool"],
            "category": test_case["category"],
            "execution_time": 0,
            "returncode": -1,
            "stdout": "",
            "stderr": str(e),
            "evaluation": {
                "score": 0,
                "status": "EXCEPTION",
                "tools_used": [],
                "expected_tool": test_case["expected_tool"],
                "tool_match": False,
                "issues": [str(e)],
                "execution_time": 0
            },
            "timestamp": datetime.now().isoformat()
        }

def generate_summary_report(results):
    """Generate comprehensive summary report"""
    
    total_tests = len(results)
    success_count = sum(1 for r in results if r['evaluation']['status'] == 'SUCCESS')
    partial_count = sum(1 for r in results if r['evaluation']['status'] == 'PARTIAL')
    failed_count = sum(1 for r in results if r['evaluation']['status'] == 'FAILED')
    timeout_count = sum(1 for r in results if r['evaluation']['status'] == 'TIMEOUT')
    
    avg_score = sum(r['evaluation']['score'] for r in results) / total_tests
    avg_time = sum(r['execution_time'] for r in results) / total_tests
    
    # Tool usage analysis
    tool_accuracy = {}
    for result in results:
        expected = result['expected_tool']
        if expected not in tool_accuracy:
            tool_accuracy[expected] = {"correct": 0, "total": 0}
        tool_accuracy[expected]["total"] += 1
        if result['evaluation']['tool_match']:
            tool_accuracy[expected]["correct"] += 1
    
    # Category analysis
    category_stats = {}
    for result in results:
        category = result['category']
        if category not in category_stats:
            category_stats[category] = {"success": 0, "total": 0, "avg_score": 0}
        category_stats[category]["total"] += 1
        if result['evaluation']['status'] == 'SUCCESS':
            category_stats[category]["success"] += 1
        category_stats[category]["avg_score"] += result['evaluation']['score']
    
    for category in category_stats:
        category_stats[category]["avg_score"] /= category_stats[category]["total"]
        category_stats[category]["success_rate"] = (
            category_stats[category]["success"] / category_stats[category]["total"] * 100
        )
    
    return {
        "summary": {
            "total_tests": total_tests,
            "success_count": success_count,
            "partial_count": partial_count,
            "failed_count": failed_count,
            "timeout_count": timeout_count,
            "success_rate": success_count / total_tests * 100,
            "average_score": avg_score,
            "average_execution_time": avg_time
        },
        "tool_accuracy": tool_accuracy,
        "category_performance": category_stats,
        "failed_tests": [
            {
                "id": r['test_id'],
                "prompt": r['prompt'],
                "issues": r['evaluation']['issues']
            }
            for r in results if r['evaluation']['status'] in ['FAILED', 'TIMEOUT']
        ]
    }

def main():
    """Run comprehensive Buddy AI test suite"""
    
    print("🚀 BUDDY AI COMPREHENSIVE TEST SUITE")
    print("="*80)
    print(f"Total Tests: {len(TEST_PROMPTS)}")
    print(f"Coverage: All tools, scenarios, and edge cases")
    print(f"Output: JSON format for easy evaluation")
    print("="*80)
    
    start_time = time.time()
    results = []
    output_file = "buddy_test_results_comprehensive.json"
    
    # Run all tests
    for i, test_case in enumerate(TEST_PROMPTS, 1):
        result = run_single_test(test_case)
        results.append(result)
        
        # Update output file after each test
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        # Generate current summary
        summary = generate_summary_report(results)
        
        # Create current output
        current_output = {
            "test_suite_info": {
                "name": "Buddy AI Comprehensive Test Suite",
                "version": "1.0",
                "total_tests": len(TEST_PROMPTS),
                "completed_tests": len(results),
                "execution_date": datetime.now().isoformat(),
                "elapsed_time": elapsed_time,
                "progress_percentage": (len(results) / len(TEST_PROMPTS)) * 100
            },
            "summary_report": summary,
            "detailed_results": results
        }
        
        # Save current state to JSON file
        with open(output_file, "w") as f:
            json.dump(current_output, f, indent=2)
        
        print(f"📄 Progress saved: {i}/{len(TEST_PROMPTS)} tests completed")
        time.sleep(1)  # Brief pause between tests
    
    total_time = time.time() - start_time
    
    # Final summary report
    final_summary = generate_summary_report(results)
    
    # Create final output
    final_output = {
        "test_suite_info": {
            "name": "Buddy AI Comprehensive Test Suite",
            "version": "1.0",
            "total_tests": len(TEST_PROMPTS),
            "completed_tests": len(results),
            "execution_date": datetime.now().isoformat(),
            "total_execution_time": total_time,
            "progress_percentage": 100.0,
            "status": "COMPLETED"
        },
        "summary_report": final_summary,
        "detailed_results": results
    }
    
    # Save final results
    with open(output_file, "w") as f:
        json.dump(final_output, f, indent=2)
    
    # Print final summary
    print(f"\n{'='*80}")
    print("🏁 TEST SUITE COMPLETED")
    print('='*80)
    print(f"Total Tests: {final_summary['summary']['total_tests']}")
    print(f"✅ Success: {final_summary['summary']['success_count']} ({final_summary['summary']['success_rate']:.1f}%)")
    print(f"⚠️  Partial: {final_summary['summary']['partial_count']}")
    print(f"❌ Failed: {final_summary['summary']['failed_count']}")
    print(f"⏰ Timeout: {final_summary['summary']['timeout_count']}")
    print(f"📊 Average Score: {final_summary['summary']['average_score']:.1f}/10")
    print(f"⏱️  Average Time: {final_summary['summary']['average_execution_time']:.1f}s")
    print(f"🕐 Total Time: {total_time:.1f}s")
    print(f"\n📄 Final results saved to: {output_file}")
    
    # Show tool accuracy
    print(f"\n🔧 TOOL ACCURACY:")
    for tool, stats in final_summary['tool_accuracy'].items():
        accuracy = stats['correct'] / stats['total'] * 100
        print(f"  {tool}: {stats['correct']}/{stats['total']} ({accuracy:.1f}%)")
    
    # Show category performance
    print(f"\n📂 CATEGORY PERFORMANCE:")
    for category, stats in final_summary['category_performance'].items():
        print(f"  {category}: {stats['success_rate']:.1f}% success, {stats['avg_score']:.1f} avg score")

if __name__ == "__main__":
    main()
