from src.retrieval.metadata_retriever import (
    MetadataRetriever
)

from src.retrieval.query_analyzer import (
    QueryAnalyzer
)

query = "What is a current mirror?"

analysis = QueryAnalyzer().analyze(
    query
)

retriever = MetadataRetriever()

results = retriever.retrieve(
    analysis
)

print(
    "Results:",
    len(results)
)

for item in results[:5]:

    print("=" * 80)

    print(
        item["metadata"]["source"]
    )

    print(
        item["metadata"]["page"]
    )

    print(
        item["text"][:500]
    )