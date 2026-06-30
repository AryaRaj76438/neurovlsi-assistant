from src.retrieval.retrieval_pipeline import RetrievalPipeline

pipeline = RetrievalPipeline()
results = pipeline.retrieve("What is current mirror?")

for result in results:
    print("="*50)
    print(result.source)
    print(result.page)
    print(f"Rerank score: {result.rerank_score}")
    print()
    print(result.text[:1000])