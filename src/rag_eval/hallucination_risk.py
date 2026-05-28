from __future__ import annotations

from typing import Sequence


def unsupported_claim_ratio(total_claims: int, unsupported_claims: int) -> dict:
    """Calculate unsupported-claim ratio for an LLM/RAG answer."""
    if total_claims < 0 or unsupported_claims < 0:
        raise ValueError("claim counts must be non-negative")
    if unsupported_claims > total_claims:
        raise ValueError("unsupported_claims cannot exceed total_claims")

    ratio = unsupported_claims / total_claims if total_claims else 0.0
    return {
        "total_claims": total_claims,
        "unsupported_claims": unsupported_claims,
        "unsupported_claim_ratio": ratio,
    }


def hallucination_risk_level(unsupported_ratio: float, high_threshold: float = 0.20, medium_threshold: float = 0.05) -> dict:
    """Map unsupported-claim ratio to a simple qualitative risk level."""
    if unsupported_ratio >= high_threshold:
        level = "high"
    elif unsupported_ratio >= medium_threshold:
        level = "medium"
    else:
        level = "low"
    return {
        "unsupported_claim_ratio": unsupported_ratio,
        "risk_level": level,
        "requires_review": level in {"medium", "high"},
    }


def unsupported_terms(answer_terms: Sequence[str], source_terms: Sequence[str]) -> list[str]:
    """Return answer terms that are not present in source terms."""
    source_set = {term.lower() for term in source_terms}
    return [term for term in answer_terms if term.lower() not in source_set]
