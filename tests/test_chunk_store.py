from src.ingestion.discovery import DocumentDiscovery
from src.ingestion.extractor import DocumentExtractor
from src.chunking.chunker import DocumentChunker
from src.chunking.chunk_store import ChunkStore


discovery = DocumentDiscovery()

document = discovery.discover()["existing"][0]

extractor = DocumentExtractor()
pages = extractor.extract(document)

chunker = DocumentChunker()

chunks = chunker.chunk_pages(
    pages[:5]
)

store = ChunkStore()

path = store.save(
    chunks,
    "test_chunks"
)

print(path)