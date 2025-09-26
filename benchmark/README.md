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
Here's a **consolidated list** of all the datasets we've discussed so far, grouped by **task type**, with descriptions and sources:

---

## 🧠 A. **Project-Level Code Generation Datasets**

| Dataset                    | Description                                                                                                                                                        | Source / Link                                                                                                            |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| **ProjectEval**            | Benchmark for *end-to-end project generation* tasks. Each task has natural language prompts, checklists, optional skeletons, and test suites.                      | [📄 Paper](https://arxiv.org/abs/2503.07010) · [💻 GitHub (planned)](https://projecteval.github.io)                      |
| **CoderEval**              | 460 programming tasks (Python & Java) with varying context dependencies — larger than isolated functions, but not full projects.                                   | [📄 Paper](https://arxiv.org/abs/2302.00288)                                                                             |
| **TransCoder / TransRepo** | Repository-level code translation tasks (e.g. Java → C#), includes structure, comments, and build config — not gen-from-scratch but useful for project-scale eval. | [📄 TransCoder](https://arxiv.org/abs/2006.03511) · [📄 TransRepo](https://arxiv.org/abs/2501.16050)                     |
| **OpenCodeInstruct**       | Massive multi-task dataset with problems, solutions, and test cases. Mostly function-level, but supports composing tasks into projects.                            | [📄 Paper](https://arxiv.org/abs/2504.04030) · [🤗 HF Dataset](https://huggingface.co/datasets/Intel/open-code-instruct) |

---

## 🧪 B. **Bug Fixing / Software Maintenance (SWE-bench Family)**

| Dataset                    | Description                                                                                                                    | Source / Link                                                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **SWE-bench**              | ~2.3K GitHub issues with test cases and patches. Models must generate a patch to fix the issue and pass the test suite.        | [🌐 Website](https://www.swebench.com) · [🤗 Dataset](https://huggingface.co/datasets/princeton-nlp/SWE-bench)            |
| **SWE-bench_Lite**         | Smaller, faster-to-evaluate version (534 issues).                                                                              | [Same source as above](https://www.swebench.com/SWE-bench/guides/datasets/)                                               |
| **SWE-bench_Verified**     | Human-curated subset (~500) with verified issue/patch pairs and reliable test coverage. Used by Amazon Q Developer and others. | [🤗 Dataset](https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified)                                            |
| **SWE-bench_Multilingual** | SWE-bench extension for multiple programming languages (e.g., Java, JS, TS).                                                   | [🌐 Info](https://www.swebench.com/multilingual)                                                                          |
| **SWE-bench_Multimodal**   | Tasks with UI elements/screenshots (i.e. multimodal inputs).                                                                   | [🌐 Info](https://www.swebench.com/SWE-bench/guides/datasets/)                                                            |
| **SWE-PolyBench**          | Multilingual repo-level benchmark with multiple task types (bug fix, feature add, refactoring). Created by Amazon Science.     | [📄 Paper](https://arxiv.org/abs/2504.08703) · [🤗 Dataset](https://huggingface.co/datasets/amazon-science/swe-polybench) |

---

## 🔍 C. **RAG / Retrieval & Knowledge Benchmarks (Used by Amazon Q Business)**

| Dataset                         | Description                                                                                                             | Source / Link                                                                                           |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **KILT**                        | Unified benchmark for knowledge-intensive NLP tasks (QA, fact-checking, etc.) using Wikipedia as retrieval base.        | [📄 Paper](https://arxiv.org/abs/2009.02252) · [📁 GitHub](https://github.com/facebookresearch/KILT)    |
| **RAGChecker**                  | Tests hallucination and attribution for RAG models. Measures grounding vs. hallucination. Used in Amazon Q’s RAG evals. | [📄 Paper](https://arxiv.org/abs/2310.03659) · [📁 GitHub](https://github.com/sileod/rag-checker)       |
| **BBQ (Bias Benchmark for QA)** | Evaluates social bias in QA models using ambiguous/disambiguated questions.                                             | [📁 GitHub](https://github.com/nyu-mll/BBQ) · [🤗 Dataset](https://huggingface.co/datasets/nyu-mll/BBQ) |
| **OpenAI Moderation Dataset**   | Dataset used to test model refusal/safety performance. Amazon Q Business uses this to evaluate content moderation.      | [📁 GitHub](https://github.com/openai/openai-content-moderation)                                        |

---

## 📌 Summary by Task Type

| Task Type                     | Datasets                                            |
| ----------------------------- | --------------------------------------------------- |
| **Project Generation**        | ProjectEval, CoderEval, TransRepo, OpenCodeInstruct |
| **Bug Fixing / Maintenance**  | SWE-bench, SWE-bench_Verified, SWE-PolyBench        |
| **Multilingual / Multimodal** | SWE-bench_Multilingual, SWE-bench_Multimodal        |
| **Bias / Safety / RAG**       | KILT, RAGChecker, BBQ, OpenAI Moderation            |

---

