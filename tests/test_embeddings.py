from src.embeddings.embedding_pipeline import (EmbeddingPipeline)

pipeline = EmbeddingPipeline()

path = pipeline.process(
    "data/chunks/test_chunks.jsonl",
    "test_chunks"
)

print(path)