from src.vector_store.indexing_pipeline import (
    IndexingPipeline
)

pipeline = IndexingPipeline()

count = pipeline.index(
    "data/chunks/test_chunks.jsonl"
)

print(
    f"Indexed {count} chunks"
)