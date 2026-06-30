from src.retrieval.keyword.bm25_index import BM25Index

index = BM25Index()

index.build()

print(
    "Documents:",
    len(index.documents)
)

print(
    "Index Ready:",
    index.is_ready()
)