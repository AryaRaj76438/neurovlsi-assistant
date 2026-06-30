# tests/test_collection_sources.py

from src.vector_store.chroma_store import (
    ChromaStore
)

store = ChromaStore()

results = store.collection.get()

sources = set()

for metadata in results["metadatas"]:

    sources.add(
        metadata["source"]
    )

for source in sorted(sources):

    print(source)