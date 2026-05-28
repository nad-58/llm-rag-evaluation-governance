from __future__ import annotations

from typing import Sequence


def retrieval_recall(retrieved_ids: Sequence[str], expected_relevant_ids: Sequence[str]) -> dict:
    """Calculate recall of expected relevant documents in retrieved results."""
    retrieved = set(retrieved_ids)
    expected = set(expected_relevant_ids)
    found = sorted(retrieved.intersection(expected))
    score = len(found) / len(expected) if expected else 0.0
    return {
        "retrieved_ids": list(retrieved_ids),
        "expected_relevant_ids": list(expected_relevant_ids),
        "found_relevant_ids": found,
        "retrieval_recall": score,
    }


def top_k_contains_relevant(retrieved_ids: Sequence[str], expected_relevant_ids: Sequence[str], k: int = 3) -> dict:
    """Check whether at least one expected relevant source appears in the top-k results."""
    top_k = list(retrieved_ids[:k])
    expected = set(expected_relevant_ids)
    found = [doc_id for doc_id in top_k if doc_id in expected]
    return {
        "k": k,
        "top_k_ids": top_k,
        "found_relevant_ids": found,
        "passed": len(found) > 0,
    }
