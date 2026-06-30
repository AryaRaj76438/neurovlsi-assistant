from src.ingestion.registry import DocumentRegistry

registry = DocumentRegistry()

documents = registry.get_all_documents()

if documents:
    record = documents[0]

    print(record["file_name"])
    print(record["file_hash"])
    print(record["status"])

registry.close()