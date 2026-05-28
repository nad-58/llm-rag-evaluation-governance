# Prompt Robustness

Prompt robustness evaluates whether an LLM/RAG system behaves consistently and safely when user prompts vary in wording, specificity, ambiguity, or intent.

## Test categories

- Rephrased questions
- Ambiguous questions
- Incomplete questions
- Out-of-scope questions
- Leading or biased prompts
- Conflicting user instructions
- Requests without enough evidence
- Attempts to bypass source-grounding rules

## Review questions

- Does the system ask for clarification when needed?
- Does the system refuse or escalate out-of-scope requests?
- Does the system remain grounded when prompts are leading?
- Does answer quality remain stable across rephrased prompts?
- Are prompt templates version-controlled?

## Evidence expectation

Prompt robustness evidence should include test cases, expected behaviour, actual behaviour, failure examples, mitigations, and re-test results after prompt changes.
