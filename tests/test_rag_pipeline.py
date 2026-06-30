from src.rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

result = rag.ask(
    "Explain current mirrors and their applications"
)

print()

print("=" * 80)
print("ANSWER")
print("=" * 80)

print(
    result["answer"]
)

print()

print("=" * 80)
print("SOURCES")
print("=" * 80)

for source in result["sources"]:
    print(
        source.source,
        source.page
    )