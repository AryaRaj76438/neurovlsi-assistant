from src.ingestion.discovery import DocumentDiscovery
from src.ingestion.extractor import DocumentExtractor
from src.chunking.chunker import DocumentChunker

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

chunker = DocumentChunker()

chunks = chunker.chunk_pages(
    pages[:5]
)

print("Chunks:", len(chunks))

print("\nSample Chunk:\n")

print(chunks[0].text[:1000])

discovery.close()