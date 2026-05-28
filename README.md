# LLM RAG Evaluation Governance

A practical portfolio project for evaluating and governing large language model (LLM) and retrieval-augmented generation (RAG) systems.

This repository demonstrates how to assess groundedness, retrieval quality, source traceability, unsupported claims, prompt robustness, human review requirements, and release readiness for generative AI workflows.

> **Note:** This repository uses synthetic examples and generic templates only. It does not contain confidential client data, private prompts, proprietary documents, or production system logs.

## Why this project exists

LLM and RAG systems can produce fluent answers that appear correct but may be incomplete, unsupported, poorly grounded, or unsuitable for high-impact workflows. Governance requires structured evaluation evidence, human oversight, monitoring, and clear acceptance criteria.

This project provides lightweight utilities, examples, and templates for reviewing whether an LLM/RAG system is ready for controlled use.

## Relevant domains

- LLM and RAG evaluation
- Generative AI governance
- Hallucination and unsupported-claim review
- Source traceability and evidence grounding
- Prompt robustness and misuse testing
- Human-in-the-loop AI workflows
- AI-assisted summarisation and question answering
- Enterprise and healthcare workflow automation

## Evaluation lifecycle

```text
Use case and risk classification
      ↓
Knowledge base and retrieval design
      ↓
Prompt and response design
      ↓
Groundedness and traceability evaluation
      ↓
Retrieval quality review
      ↓
Unsupported-claim and hallucination analysis
      ↓
Human review and escalation design
      ↓
Monitoring and feedback loop
      ↓
Change control and re-evaluation
```

## Repository structure

```text
llm-rag-evaluation-governance/
├── README.md
├── LICENSE
├── requirements.txt
├── src/
│   └── rag_eval/
│       ├── groundedness.py
│       ├── retrieval_quality.py
│       ├── hallucination_risk.py
│       ├── human_review.py
│       └── evaluation_report.py
├── examples/
│   ├── rag_answer_evaluation.py
│   ├── retrieval_quality_report.py
│   └── hallucination_risk_report.py
├── docs/
│   ├── llm-rag-lifecycle.md
│   ├── groundedness-and-traceability.md
│   ├── hallucination-risk-management.md
│   ├── prompt-robustness.md
│   ├── human-oversight-for-genai.md
│   └── monitoring-and-feedback.md
└── templates/
    ├── rag-evaluation-checklist.md
    ├── prompt-risk-register.md
    ├── genai-model-card.md
    └── human-review-policy.md
```

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
- Create a lightweight governance report for GenAI release readiness

## Professional positioning

This repository demonstrates practical LLM/RAG governance thinking: combining evaluation metrics, source traceability, human oversight, and risk-based release decisions. It is designed for AI assurance, AI governance, technical AI review, and Principal AI/ML engineering portfolios.

## Disclaimer

This repository is for educational and professional portfolio purposes. It is not legal, regulatory, safety, or clinical advice. Real-world LLM/RAG evaluation requires system-specific test data, domain experts, security review, privacy assessment, and operational monitoring.

## Licence

MIT Licence. See `LICENSE` for details.
