from src.retrieval.query_analyzer import (
    QueryAnalyzer
)

from src.retrieval.hybrid_retriever import (
    HybridRetriever
)

analysis = (
    QueryAnalyzer()
    .analyze(
        "What is a current mirror?"
    )
)

retriever = HybridRetriever()

results = retriever.retrieve(
    analysis,
    top_k=10
)

for item in results:

    print("=" * 80)

    print(
        f"Fusion Score: "
        f"{item.fusion_score:.6f}"
    )

    print(item.source)

    print(item.page)

    print()

    print(item.text[:400])