# Hallucination Risk Management

Hallucination risk refers to generated output that includes unsupported, invented, misleading, or overconfident claims.

## Common causes

- Weak or missing retrieval evidence
- Ambiguous user questions
- Overly broad prompts
- Outdated or conflicting source documents
- Poor chunking or ranking
- Lack of answer abstention rules
- No requirement for source traceability

## Risk controls

- Require source-grounded responses
- Add answer abstention rules
- Use human review for high-impact outputs
- Define unsupported-claim thresholds
- Test prompt variation and edge cases
- Monitor user feedback and corrections
- Re-evaluate after knowledge-base updates

## Review questions

- Are unsupported claims identified during evaluation?
- Are hallucination examples documented and analysed?
- Are risky output categories defined?
- Is human review required where the answer may affect important decisions?
- Are model limitations clear to users?
