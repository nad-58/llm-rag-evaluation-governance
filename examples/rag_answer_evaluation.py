from rag_eval.evaluation_report import evaluation_summary
from rag_eval.groundedness import groundedness_decision, keyword_groundedness_score
from rag_eval.hallucination_risk import hallucination_risk_level, unsupported_claim_ratio
from rag_eval.human_review import human_review_decision
from rag_eval.retrieval_quality import top_k_contains_relevant


def main() -> None:
    question = "What evidence is needed before deploying an AI model update?"
    answer = "A model update should be supported by impact analysis, validation evidence, monitoring review, and approval."
    sources = [
        "The change process requires impact analysis before release.",
        "Validation evidence and monitoring review should be documented before approval.",
    ]
    expected_terms = ["impact analysis", "validation", "monitoring", "approval"]

    groundedness = keyword_groundedness_score(answer, sources, expected_terms)
    groundedness_result = groundedness_decision(groundedness["groundedness_score"], threshold=0.80)

    retrieval_result = top_k_contains_relevant(
        retrieved_ids=["change-control", "validation-plan", "user-guide"],
        expected_relevant_ids=["change-control", "validation-plan"],
        k=3,
    )

    unsupported = unsupported_claim_ratio(total_claims=4, unsupported_claims=0)
    hallucination = hallucination_risk_level(unsupported["unsupported_claim_ratio"])

    review = human_review_decision(
        groundedness_passed=groundedness_result["passed"],
        retrieval_passed=retrieval_result["passed"],
        hallucination_requires_review=hallucination["requires_review"],
        high_impact_use=True,
    )

    summary = evaluation_summary(
        {
            "groundedness": groundedness_result["passed"],
            "retrieval": retrieval_result["passed"],
            "unsupported_claims": not hallucination["requires_review"],
            "human_review_policy": review["requires_human_review"],
        }
    )

    print("RAG answer evaluation")
    print("=====================")
    print("Question:", question)
    print("Answer:", answer)
    print("\nGroundedness")
    print(groundedness)
    print(groundedness_result)
    print("\nRetrieval")
    print(retrieval_result)
    print("\nUnsupported claim risk")
    print(unsupported)
    print(hallucination)
    print("\nHuman review")
    print(review)
    print("\nSummary")
    print(summary)


if __name__ == "__main__":
    main()
