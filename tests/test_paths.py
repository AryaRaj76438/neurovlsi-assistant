from src.ingestion.registry import DocumentRegistry
from src.ingestion.scanner import DocumentScanner

registry = DocumentRegistry()

print("\nDATABASE RECORDS")
print("-" * 50)

for row in registry.get_all_documents():
    print(row["file_path"])

print("\nSCANNER RECORDS")
print("-" * 50)

scanner = DocumentScanner()

for doc in scanner.scan():
    print(doc["file_path"])