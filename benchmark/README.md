# Multi-Agent Software Development Benchmark

This benchmark suite contains 100 comprehensive problem statements designed to test the autonomy and capabilities of AI agents in software development, with focus on data science, data engineering, DevOps, MLOps, GitOps, and Kubernetes.

## Structure

- **01-project-analysis/**: Project understanding and code analysis tasks (1-15)
- **02-bug-fixing/**: Issue resolution and debugging tasks (16-30)  
- **03-feature-enhancement/**: Feature addition and system enhancement tasks (31-50)
- **04-data-science-ml/**: Data science and ML engineering tasks (51-70)
- **05-devops-infrastructure/**: DevOps and infrastructure tasks (71-85)
- **06-advanced-scenarios/**: Complex multi-agent scenarios (86-100)

## Usage

Each folder contains procedural documents with:
- Problem statement
- Detailed requirements
- Success criteria
- Expected deliverables
- Complexity indicators

## Complexity Levels

- **Beginner**: Single-domain tasks with clear requirements
- **Intermediate**: Multi-domain tasks requiring coordination
- **Advanced**: Complex systems with real-time requirements
- **Expert**: Enterprise-scale with safety/compliance requirements

## Testing Framework

Use these benchmarks to evaluate:
- Agent autonomy and decision-making
- Multi-agent coordination capabilities
- Technical depth and accuracy
- Problem-solving approaches
- Code quality and best practices



## Key Dimensions to Evaluate

Here are the features you’ll want your benchmarking setup to test:

1. **Retrieval quality** — ability to fetch relevant documents / data given a user query (or command).
2. **Answer correctness / completeness** — is the answer accurate, complete, and meets the user’s query?
3. **Groundedness / hallucination** — are answers supported by retrieved material (or known data)?
4. **Tool / command invocation / function calling** — does the system correctly decide when to call tools, which ones, with the correct parameters?
5. **CLI / shell interactions** — ability to run commands, chain commands, handle errors, parse outputs, possibly escalate privileges, etc.
6. **Conversational & multi‑step context** — follow‑ups, clarifying questions, context retention across multiple steps.
7. **Latency / response time / resource usage** — important for CLI UX.
8. **Safety / robustness** — what happens with invalid/malicious input, edge‑cases.
9. **User experience / interpretability** — clarity of responses, error messages, prompts, logs etc.

---

## Datasets / Benchmarks to Use

Here are existing datasets / benchmarks that align (partially or largely) with these dimensions, which you can repurpose or adapt for your CLI Q product evaluation:

| Name                                                                         | What it Tests / Relevant for CLI‑Q Type                                                                                                             | Key Features / Why It Helps                                                                                                                                       |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CRAG (Comprehensive RAG Benchmark)**                                       | Very relevant: it’s directly aimed at RAG (retrieval augmented generation) systems, includes multiple domains & question types. ([OPEA Project][1]) | You can use this to test answer quality, retrieval, possibly some function/API calling (mock APIs) to simulate tool invocation. Good for correctness / reasoning. |
| **InfiAgent‑DA‑Bench**                                                       | Data analysis queries over CSVs. Useful if your CLI agent is expected to answer questions about tabular data or do analytics, etc. ([InfiAgent][2]) | Tests grounding (CSV), correctness, ability to parse structured data. Might be a component of your suite.                                                         |
| **Terminal‑Bench**                                                           | CLI/terminal‑style tasks: seems specifically designed for evaluating agents in CLI/terminal environments. ([Terminal-Bench][3])                     | This likely matches your use case quite closely: testing CLI workflows, command usage, error handling in terminal. Very helpful.                                  |
| **ALMITA Dataset (customer‑support / tool‑augmented conversational agents)** | Evaluates API/tool usage, conversation, correctness of replies and APIs called. ([Simple Science][4])                                               | Even though not exactly CLI, the infrastructure of deciding when to call a tool or respond is similar. Useful for tool invocation evaluation.                     |
| **Tiny QA Benchmark++ (TQB++)**                                              | Smaller QA dataset, useful for testing correctness / regression / smoke‑testing. ([GitHub][5])                                                      | Helps in catching small mistakes quickly; good for continuous integration.                                                                                        |

---
