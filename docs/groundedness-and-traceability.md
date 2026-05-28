# Groundedness and Traceability

Groundedness evaluates whether generated answers are supported by retrieved evidence. Traceability evaluates whether key claims can be linked back to specific sources.

## Evaluation focus

- Are all important claims supported by retrieved sources?
- Are sources relevant to the question?
- Are source references shown to the user where needed?
- Does the answer avoid claims not present in the evidence?
- Are uncertain or incomplete answers handled appropriately?

## Example acceptance criteria

```text
Groundedness score >= 0.80
Important claims must be source traceable
Unsupported claims must be zero for high-impact use
```

## Review questions

- Does each answer include source references?
- Are source references specific enough to verify?
- Are retrieved documents current and appropriate?
- Does the model distinguish evidence from inference?
- Are weak-evidence cases escalated for review?
