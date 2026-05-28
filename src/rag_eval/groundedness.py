from __future__ import annotations

from typing import Sequence


def keyword_groundedness_score(answer: str, sources: Sequence[str], expected_terms: Sequence[str]) -> dict:
    """Calculate a simple groundedness score based on expected terms appearing in sources.

    This is a transparent demonstration metric. Real evaluations should use
    human review, source-to-claim checking, and domain-specific rubrics.
    """
    source_text = " ".join(sources).lower()
    answer_text = answer.lower()

    found_in_answer = [term for term in expected_terms if term.lower() in answer_text]
    grounded_terms = [term for term in found_in_answer if term.lower() in source_text]

    score = len(grounded_terms) / len(expected_terms) if expected_terms else 0.0
    return {
        "expected_terms": list(expected_terms),
        "terms_found_in_answer": found_in_answer,
        "terms_grounded_in_sources": grounded_terms,
        "groundedness_score": score,
    }


def groundedness_decision(score: float, threshold: float = 0.80) -> dict:
    """Apply a simple acceptance threshold to groundedness score."""
    return {
        "score": score,
        "threshold": threshold,
        "passed": score >= threshold,
        "decision": "accepted" if score >= threshold else "review_required",
    }
