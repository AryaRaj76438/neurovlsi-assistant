from src.retrieval.query_analyzer import QueryAnalyzer
from src.retrieval.retriever import Retriever

query = QueryAnalyzer().analyze(
    "What is a current mirror?"
)

retriever = Retriever()

results = retriever.retrieve(
    query,
    top_k=10
)

for r in results:

    print("=" * 80)
    print("Source:", r.source)
    print("Page:", r.page)
    print("Distance:", r.distance)
    print()
    print(r.text[:400])