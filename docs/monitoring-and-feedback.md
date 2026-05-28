# Monitoring and Feedback

LLM/RAG systems should be monitored after release to detect quality issues, unsupported outputs, retrieval failures, user corrections, and changes in source documents.

## Monitoring signals

- User feedback and corrections
- Reviewer rejection rate
- Unsupported-claim rate
- Retrieval failure rate
- Missing citation or weak-traceability rate
- Out-of-scope question rate
- Escalation rate
- Knowledge-base update frequency
- Prompt or model version changes

## Investigation triggers

- Increase in reviewer rejection rate
- Repeated unsupported claims
- Retrieval misses for known questions
- High number of unclear or incomplete answers
- New source documents or changed source documents
- Prompt, model, embedding, or retrieval pipeline update

## Review questions

- Are monitoring signals linked to action thresholds?
- Are user corrections reviewed and categorised?
- Are recurring failures used to improve prompts or retrieval?
- Are changes version-controlled and re-evaluated?
