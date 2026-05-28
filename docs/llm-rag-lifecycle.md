# LLM/RAG Evaluation Lifecycle

LLM and RAG systems should be evaluated across the full lifecycle, from use-case definition to monitoring and change control.

## Lifecycle stages

1. Define use case and risk level
2. Define knowledge sources and retrieval strategy
3. Define prompt and response design
4. Build a representative evaluation set
5. Evaluate retrieval quality
6. Evaluate groundedness and source traceability
7. Review unsupported claims and hallucination risk
8. Test prompt robustness and misuse scenarios
9. Define human review and escalation rules
10. Monitor outputs, feedback, and failures after deployment
11. Re-evaluate after prompt, model, retrieval, or knowledge-base changes

## Review questions

- What is the intended use of the LLM/RAG workflow?
- What decisions or actions may be influenced by the generated output?
- What sources are allowed for answer generation?
- Are important claims traceable to source evidence?
- Are unsupported claims detected and reviewed?
- Are high-impact outputs subject to human review?
- What changes trigger re-evaluation?
