# Automated vs Manual Evaluation

Automated metrics can support LLM/RAG evaluation, but they should not fully replace human review for important or high-impact workflows.

## Automated evaluation

Automated evaluation can help scale review across many examples. It may assess:

- Relevance
- Completeness
- Groundedness
- Source traceability
- Unsupported claims
- Conciseness
- Refusal behaviour
- Retrieval quality

Automated metrics are useful for screening, trend monitoring, and regression testing, but they can miss context-specific issues.

## Manual evaluation

Manual evaluation is important when outputs require domain judgement, user-safety assessment, policy interpretation, clinical or legal context, or subjective preference review.

Manual review should use a defined rubric, such as:

| Metric | Scale | Description |
|---|---|---|
| Relevance | 0-2 | Whether the answer addresses the prompt |
| Groundedness | 0-2 | Whether claims are supported by sources |
| Completeness | 0-2 | Whether required key points are included |
| Traceability | 0-2 | Whether claims can be checked against sources |
| Review need | Yes/No | Whether human approval is required before use |

## Alignment between automated and manual review

The evaluation should compare automated metric results against human annotations. Useful checks include:

- Agreement rate
- Confusion matrix of pass/fail decisions
- Correlation between automated and manual scores
- Review of cases where automated metrics pass but humans fail
- Review of cases where humans pass but automated metrics fail

## Governance decision

Automated evaluation may be sufficient for low-risk trend monitoring, but manual review should remain part of release decisions where generated outputs influence important decisions or user-facing workflows.
