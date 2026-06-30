from src.rag.context_builder import ContextBuilder
from src.retrieval.retrieval_pipeline import RetrievalPipeline

query = "What is a current mirror?"
pipeline = RetrievalPipeline()
results = pipeline.retrieve(query)

builder = ContextBuilder()
context = builder.build(query,results)

print()
print("="*50)
print(context.context_text[:3000])
