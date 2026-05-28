from rag_eval.hallucination_risk import hallucination_risk_level, unsupported_claim_ratio, unsupported_terms


def main() -> None:
    answer_terms = ["validation", "approval", "automatic release", "monitoring"]
    source_terms = ["validation", "approval", "monitoring", "impact analysis"]

    unsupported = unsupported_terms(answer_terms, source_terms)
    ratio = unsupported_claim_ratio(total_claims=len(answer_terms), unsupported_claims=len(unsupported))
    risk = hallucination_risk_level(ratio["unsupported_claim_ratio"])

    print("Hallucination risk report")
    print("=========================")
    print("\nUnsupported terms")
    print(unsupported)
    print("\nUnsupported claim ratio")
    print(ratio)
    print("\nRisk level")
    print(risk)

    if risk["requires_review"]:
        print("\nInterpretation: the answer should be reviewed because it includes unsupported content.")
    else:
        print("\nInterpretation: unsupported-claim risk is low in this synthetic example.")


if __name__ == "__main__":
    main()
