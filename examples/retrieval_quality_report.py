from rag_eval.retrieval_quality import retrieval_recall, top_k_contains_relevant


def main() -> None:
    retrieved_ids = [
        "clinical-summary",
        "validation-plan",
        "change-control",
        "user-guide",
    ]
    expected_relevant_ids = ["validation-plan", "change-control", "monitoring-plan"]

    recall = retrieval_recall(retrieved_ids, expected_relevant_ids)
    top_k = top_k_contains_relevant(retrieved_ids, expected_relevant_ids, k=3)

    print("Retrieval quality report")
    print("========================")
    print("\nRecall")
    print(recall)
    print("\nTop-k relevance")
    print(top_k)

    if recall["retrieval_recall"] < 0.80:
        print("\nInterpretation: retrieval coverage should be improved before relying on generated answers.")
    else:
        print("\nInterpretation: retrieval coverage meets the example threshold.")


if __name__ == "__main__":
    main()
