from src.retrieval.query_analyzer import (
    QueryAnalyzer
)

from src.retrieval.retriever import (
    Retriever
)


query = (
    QueryAnalyzer()
    .analyze(
        "What is a current mirror?"
    )
)

retriever = Retriever()

results = retriever.retrieve(
    query,
    top_k=5
)

for item in results:

    print("=" * 80)

    print(item.source)

    print(item.page)

    print(item.text[:300])