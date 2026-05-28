from __future__ import annotations


def human_review_decision(
    groundedness_passed: bool,
    retrieval_passed: bool,
    hallucination_requires_review: bool,
    high_impact_use: bool = False,
) -> dict:
    """Determine whether an LLM/RAG answer requires human review."""
    reasons = []
    if not groundedness_passed:
        reasons.append("groundedness_check_failed")
    if not retrieval_passed:
        reasons.append("retrieval_check_failed")
    if hallucination_requires_review:
        reasons.append("unsupported_claim_risk")
    if high_impact_use:
        reasons.append("high_impact_use")

    requires_review = len(reasons) > 0
    return {
        "requires_human_review": requires_review,
        "reasons": reasons,
        "decision": "review_required" if requires_review else "accepted_for_low_risk_use",
    }
