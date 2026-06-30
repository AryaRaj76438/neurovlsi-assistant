from src.retrieval.retrieval_pipeline import RetrievalPipeline
from src.rag.context_compressor import ContextCompressor

pipeline = RetrievalPipeline()
compressor = ContextCompressor()

results = pipeline.retrieve(
    "What is a current mirror?"
)

compressed = compressor.compress(
    query="What is a current mirror?",
    chunks=results
)

for chunk in compressed:

    print("=" * 80)
    print(chunk.source)
    print(chunk.page)
    print()
    print(chunk.content[:500])