# Text and LLM Evaluation Workflow

Text and LLM systems require evaluation across relevance, groundedness, completeness, traceability, unsupported claims, robustness, and human review.

## Evaluation dataset

Each evaluation item should include:

- Prompt or user question
- System instruction version
- Retrieved source material where applicable
- Model output
- Expected key points or ideal answer
- Risk category
- Human review requirement

## Evaluation dimensions

| Dimension | Review question | Evidence |
|---|---|---|
| Relevance | Does the answer address the prompt? | Rubric score |
| Completeness | Are required key points included? | Key-point checklist |
| Groundedness | Are claims supported by sources? | Source-to-claim review |
| Traceability | Can key claims be linked to sources? | Citation/source IDs |
| Safety and scope | Does the model avoid unsupported or out-of-scope answers? | Refusal/escalation review |
| Robustness | Is behaviour stable under prompt variation? | Prompt test suite |
| Human oversight | Is review required before use? | Review policy |

## Workflow

1. Define the use case and risk level.
2. Define the evaluation dataset and expected key points.
3. Generate model outputs using fixed prompts and model versions.
4. Record retrieved sources and system prompts.
5. Apply automated metrics where appropriate.
6. Conduct manual review on a representative sample.
7. Compare automated metrics with human judgement.
8. Investigate failures and recurring error types.
9. Define monitoring and escalation rules.
10. Re-evaluate after prompt, model, retrieval, or source changes.

## Review outcome

The evaluation should conclude whether the system is ready for controlled use, requires further review, needs prompt or retrieval improvement, or requires stronger human oversight.
