from src.rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

response1 = rag.ask(
    "What is a current mirror?"
)
print(response1["answer"])

response2 = rag.ask(
    "What are its disadvantages?"
)

print(response2["answer"])