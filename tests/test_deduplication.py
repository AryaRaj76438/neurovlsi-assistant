from src.retrieval.query_analyzer import QueryAnalyzer
from src.retrieval.retriever import Retriever
from src.retrieval.deduplicator import Deduplicator

analysis = QueryAnalyzer().analyze("What is a current mirror?")
retriever = Retriever()
chunks = retriever.retrieve(analysis, top_k=20)
print("Before: ", len(chunks))
deduplicator = Deduplicator()
filtered = deduplicator.duplicate(chunks)
print("After: ", len(filtered))
for chunk in filtered:
    print(chunk.source)
    print(chunk.page)