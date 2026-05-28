# Human Review Policy Template

## Purpose

Define when generated outputs require human review before use.

## Review triggers

- High-impact use case
- Low groundedness score
- Missing or weak source traceability
- Unsupported claim detected
- Ambiguous user request
- Out-of-scope request
- Conflicting evidence
- User or reviewer uncertainty

## Reviewer responsibilities

- Check source evidence
- Confirm answer relevance
- Remove unsupported claims
- Add limitations where needed
- Escalate unresolved issues
- Record review decision

## Review outcome

| Outcome | Meaning | Action |
|---|---|---|
| Accept | Output is suitable for use | Release or send |
| Edit | Output needs correction | Revise before use |
| Escalate | Domain expert needed | Hold output |
| Reject | Output is unsuitable | Do not use |
