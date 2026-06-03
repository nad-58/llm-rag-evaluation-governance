# LLM RAG Evaluation Governance

A practical portfolio project for evaluating and governing large language model (LLM) and retrieval-augmented generation (RAG) systems.

This repository demonstrates how to assess groundedness, retrieval quality, source traceability, unsupported claims, prompt robustness, human review requirements, monitoring, and release readiness for generative AI workflows.

This repository uses **synthetic examples and generic templates only**. It does **not** contain confidential client data, private prompts, proprietary documents, customer material, production system logs, or employer-specific information.

## Why this project exists

LLM and RAG systems can produce fluent answers that appear correct but may be incomplete, unsupported, poorly grounded, or unsuitable for high-impact workflows. Governance requires structured evaluation evidence, human oversight, monitoring, and clear acceptance criteria.

This project provides lightweight utilities, examples, documents, and templates for reviewing whether an LLM/RAG system is ready for controlled use.

## Evaluation lifecycle

```text
Use case and risk classification
      ↓
Knowledge base and retrieval design
      ↓
Prompt and response design
      ↓
Evaluation dataset and annotation rubric
      ↓
Groundedness and traceability evaluation
      ↓
Retrieval quality review
      ↓
Unsupported-claim and hallucination analysis
      ↓
Automated versus manual review comparison
      ↓
Human review and escalation design
      ↓
Monitoring, feedback, and re-evaluation
```

## Repository structure

```text
llm-rag-evaluation-governance/
├── README.md
├── LICENSE
├── requirements.txt
├── src/rag_eval/
│   ├── groundedness.py
│   ├── retrieval_quality.py
│   ├── hallucination_risk.py
│   ├── human_review.py
│   └── evaluation_report.py
├── examples/
│   ├── rag_answer_evaluation.py
│   ├── retrieval_quality_report.py
│   └── hallucination_risk_report.py
├── docs/
│   ├── llm-rag-lifecycle.md
│   ├── text-llm-evaluation-workflow.md
│   ├── automated-vs-manual-evaluation.md
│   ├── groundedness-and-traceability.md
│   ├── hallucination-risk-management.md
│   ├── prompt-robustness.md
│   ├── human-oversight-for-genai.md
│   └── monitoring-and-feedback.md
└── templates/
    ├── rag-evaluation-checklist.md
    ├── metric-threshold-pass-rate-template.md
    ├── human-annotation-template.md
    ├── prompt-risk-register.md
    ├── genai-model-card.md
    └── human-review-policy.md
```

## Documentation guide

| Document | Purpose |
|---|---|
| [`docs/llm-rag-lifecycle.md`](docs/llm-rag-lifecycle.md) | End-to-end lifecycle for LLM/RAG evaluation and governance |
| [`docs/text-llm-evaluation-workflow.md`](docs/text-llm-evaluation-workflow.md) | Evaluation workflow for prompts, outputs, key points, and review criteria |
| [`docs/automated-vs-manual-evaluation.md`](docs/automated-vs-manual-evaluation.md) | How to compare automated metrics against human annotation |
| [`docs/groundedness-and-traceability.md`](docs/groundedness-and-traceability.md) | Source support, source-to-claim review, and traceability expectations |
| [`docs/hallucination-risk-management.md`](docs/hallucination-risk-management.md) | Unsupported claims, overconfident outputs, and mitigation controls |
| [`docs/prompt-robustness.md`](docs/prompt-robustness.md) | Rephrasing, ambiguity, prompt variation, and out-of-scope testing |
| [`docs/human-oversight-for-genai.md`](docs/human-oversight-for-genai.md) | Human review, escalation, and reviewer responsibilities |
| [`docs/monitoring-and-feedback.md`](docs/monitoring-and-feedback.md) | Feedback signals, reviewer rejection rate, and re-evaluation triggers |

## Templates

| Template | Use |
|---|---|
| [`templates/rag-evaluation-checklist.md`](templates/rag-evaluation-checklist.md) | Structured RAG evaluation checklist |
| [`templates/metric-threshold-pass-rate-template.md`](templates/metric-threshold-pass-rate-template.md) | Metric thresholds, pass rates, and failure review |
| [`templates/human-annotation-template.md`](templates/human-annotation-template.md) | Manual annotation rubric and review table |
| [`templates/prompt-risk-register.md`](templates/prompt-risk-register.md) | Prompt and response risk tracking |
| [`templates/genai-model-card.md`](templates/genai-model-card.md) | Generative AI system card |
| [`templates/human-review-policy.md`](templates/human-review-policy.md) | Human review and escalation policy |

## Key evaluation dimensions

| Dimension | Review focus |
|---|---|
| Relevance | Does the answer address the user question? |
| Groundedness | Are claims supported by retrieved evidence? |
| Traceability | Can important claims be linked to sources? |
| Retrieval quality | Are relevant documents retrieved and ranked well? |
| Unsupported claims | Does the model introduce facts not found in evidence? |
| Completeness | Does the answer include required key points? |
| Robustness | Does behaviour remain stable under prompt variation? |
| Human oversight | Does the workflow require review, escalation, or approval? |
| Monitoring | Are feedback, failures, and drift signals reviewed after release? |

## Quick start

```bash
pip install -r requirements.txt
PYTHONPATH=src python examples/rag_answer_evaluation.py
PYTHONPATH=src python examples/retrieval_quality_report.py
PYTHONPATH=src python examples/hallucination_risk_report.py
```

## Example use cases

- Evaluate whether a RAG answer is grounded in retrieved sources
- Check whether retrieved documents cover expected evidence
- Flag unsupported claims and high-risk responses
- Define human review rules for high-impact outputs
- Compare automated review with manual annotation
- Create a lightweight governance report for GenAI release readiness

## Professional positioning

This repository demonstrates practical LLM/RAG governance: combining evaluation metrics, source traceability, manual review, human oversight, monitoring, and risk-based release decisions. It is designed for AI assurance, AI governance, technical AI review, and Principal AI/ML engineering portfolios.

## Disclaimer

This repository is for educational and professional portfolio purposes. It is not legal, regulatory, safety, or clinical advice. Real-world LLM/RAG evaluation requires system-specific test data, domain experts, security review, privacy assessment, and operational monitoring.

## Licence

MIT Licence. See [`LICENSE`](LICENSE) for details.
