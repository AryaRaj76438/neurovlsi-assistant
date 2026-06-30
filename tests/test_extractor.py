from src.ingestion.discovery import DocumentDiscovery
from src.ingestion.extractor import DocumentExtractor

discovery = DocumentDiscovery()

results = discovery.discover()

documents = (
    results["new"]
    + results["modified"]
    + results["existing"]
)

document = documents[0]

extractor = DocumentExtractor()

pages = extractor.extract(document)

print("Document:", document["file_name"])
print("Pages:", len(pages))

print("\nFirst Page Preview:\n")
print(pages[0]["text"][:1000])

discovery.close()