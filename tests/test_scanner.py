from src.ingestion.scanner import DocumentScanner

scanner = DocumentScanner()

documents = scanner.scan()

print(f"Found {len(documents)} documents")

for doc in documents[:5]:
    print("-" * 80)
    print("Name:", doc["file_name"])
    print("Type:", doc["source_type"])
    print("Size:", doc["file_size"])