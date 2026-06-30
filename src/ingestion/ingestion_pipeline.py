from src.ingestion.discovery import DocumentDiscovery
from src.ingestion.extractor import DocumentExtractor
from src.chunking.chunker import DocumentChunker
from src.chunking.chunk_store import ChunkStore
from src.vector_store.document_index_manager import DocumentIndexManager

from src.core.config import load_settings
from src.metadata.metadata_pipeline import MetadataPipeline

from src.ingestion.registry import (DocumentRegistry)

class IngestionPipeline:
    def __init__(self):
        self.discovery = DocumentDiscovery()
        self.extractor = DocumentExtractor()
        self.chunker = DocumentChunker()
        self.chunk_store = ChunkStore()
        self.index_manager = DocumentIndexManager()
        self.registry = DocumentRegistry()
        self.metadata_pipeline = MetadataPipeline()
        self.settings = load_settings()

    def process_document(self, document):
        try:
            existing = self.registry.get_document_by_path(document["file_path"])
            if existing is None:
                self.registry.register_document(document)
            self.registry.update_status(document["file_path"], "processing")
            pages = self.extractor.extract(document)
            chunks = self.chunker.chunk_pages(pages)
            chunks = self.metadata_pipeline.enrich(chunks)
            chunk_file = self.chunk_store.save(chunks, document["file_hash"])
            indexed_count = self.index_manager.index_document(chunk_file)
            model_name = self.settings["models"]["embedding"]["name"]
            self.registry.mark_completed(document["file_path"],indexed_count, model_name)
            
            return indexed_count

        except Exception as e:
            self.registry.mark_failed(document["file_path"], str(e))
            raise

    def process_modified_document(self, document):
        try:
            self.registry.update_status(document["file_path"], "processing")
            pages = self.extractor.extract(document)
            chunks = self.chunker.chunk_pages(pages)
            chunks = self.metadata_pipeline.enrich(chunks)
            chunk_file = self.chunk_store.save(chunks, document["file_hash"])
            indexed_count = self.index_manager.index_document(chunk_file)
            model_name = self.settings["models"]["embedding"]["name"]
            self.registry.mark_completed(document["file_path"],indexed_count, model_name)
            return indexed_count
        except Exception as e:
            self.registry.mark_failed(document["file_path"], str(e))
            raise

    def run(self):
        discovered = self.discovery.discover()

        total_processed = 0
        for document in discovered["new"]:
            count = self.process_document(document)
            total_processed += count
            print(f"Processed (New):"
                  f"{document['file_name']}")
        
        for document in discovered["modified"]:
            count = self.process_modified_document(document)
            total_processed += count
            print(f"Processed (Modified): "
                  f"{document['file_name']}")
        
        return total_processed

