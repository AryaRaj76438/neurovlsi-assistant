# tests/test_hybrid_metadata.py

from src.retrieval.retrieval_pipeline import RetrievalPipeline

pipeline = RetrievalPipeline()

results = pipeline.retrieve(
    "Explain current mirror bias generation"
)

for result in results:

    print("=" * 80)

    print(result.source)
    print("Page:", result.page)

    print(
        result.text[:600]
    )