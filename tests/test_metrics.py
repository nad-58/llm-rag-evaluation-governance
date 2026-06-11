from rag_eval.groundedness import groundedness_decision, keyword_groundedness_score
from rag_eval.retrieval_quality import retrieval_recall, top_k_contains_relevant


def test_groundedness_metric():
    result = keyword_groundedness_score(
        "Validation and monitoring are required.",
        ["Validation and monitoring are required before release."],
        ["validation", "monitoring"],
    )
    assert result["groundedness_score"] == 1.0
    assert groundedness_decision(1.0)["passed"]


def test_retrieval_metrics():
    recall = retrieval_recall(["doc-1", "doc-2"], ["doc-2", "doc-3"])
    top_k = top_k_contains_relevant(["doc-1", "doc-2"], ["doc-2"], k=2)
    assert recall["retrieval_recall"] == 0.5
    assert top_k["passed"]
