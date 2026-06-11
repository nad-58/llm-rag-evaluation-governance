import pytest

from rag_eval.hallucination_risk import hallucination_risk_level, unsupported_claim_ratio, unsupported_terms
from rag_eval.human_review import human_review_decision


def test_hallucination_and_review_logic():
    unsupported = unsupported_terms(["validation", "automatic release"], ["validation"])
    ratio = unsupported_claim_ratio(2, len(unsupported))
    risk = hallucination_risk_level(ratio["unsupported_claim_ratio"])
    review = human_review_decision(True, True, risk["requires_review"])
    assert unsupported == ["automatic release"]
    assert risk["risk_level"] == "high"
    assert review["requires_human_review"]


def test_invalid_claim_counts_raise():
    with pytest.raises(ValueError):
        unsupported_claim_ratio(1, 2)
