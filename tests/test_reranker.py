from src.retrieval.query_analyzer import (QueryAnalyzer)

from src.retrieval.retriever import (Retriever)

from src.retrieval.reranker import (Reranker)


query = (
    QueryAnalyzer()
    .analyze(
        "What is a current mirror?"
    )
)

retriever = Retriever()

chunks = retriever.retrieve(
    query,
    top_k=20
)

reranker = Reranker()

results = reranker.rerank(
    query,
    chunks,
    top_k=5
)

for item in results:

    print("=" * 80)

    print(
        "Score:",
        item.rerank_score
    )

    print(
        item.source
    )

    print(
        "Page:",
        item.page
    )

    print()

    print(
        item.text[:500]
    )