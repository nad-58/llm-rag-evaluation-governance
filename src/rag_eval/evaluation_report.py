from __future__ import annotations


def evaluation_summary(checks: dict[str, bool]) -> dict:
    """Summarise pass/fail checks for an LLM/RAG evaluation."""
    if not checks:
        raise ValueError("checks must not be empty")

    passed = sum(1 for value in checks.values() if value)
    total = len(checks)
    failed = [name for name, value in checks.items() if not value]
    return {
        "passed_checks": passed,
        "total_checks": total,
        "score": passed / total,
        "failed_checks": failed,
        "overall_decision": "accepted" if not failed else "review_required",
    }
