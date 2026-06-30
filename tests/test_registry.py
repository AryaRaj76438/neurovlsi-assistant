from src.ingestion.registry import DocumentRegistry


registry = DocumentRegistry()

print("Registry initialized successfully")

documents = registry.get_all_documents()

print("Documents:", len(documents))

registry.close()