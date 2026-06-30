from src.retrieval.query_analyzer import (
    QueryAnalyzer
)

from src.retrieval.keyword.bm25_retriever import (
    BM25Retriever
)

analysis = (
    QueryAnalyzer()
    .analyze(
        "What is a current mirror?"
    )
)

retriever = BM25Retriever()

results = retriever.retrieve(
    analysis,
    top_k=5
)

for item in results:
    print("=" * 80)
    print(item.source)
    print(item.page)
    print()
    print(item.text[:500])