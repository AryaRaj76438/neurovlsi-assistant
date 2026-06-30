# tests/test_chroma_count.py

from src.vector_store.chroma_store import ChromaStore

store = ChromaStore()

print(
    "Collection Count:",
    store.count()
)