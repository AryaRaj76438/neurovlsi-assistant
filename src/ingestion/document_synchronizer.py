from pathlib import Path

from src.ingestion.discovery import DocumentDiscovery
from src.ingestion.registry import DocumentRegistry
from src.vector_store.document_index_manager import DocumentIndexManager

class DocumentSynchronizer:
    def __init__(self):
        self.discovery = DocumentDiscovery()
        self.registry = DocumentRegistry()
        self.index_manager = DocumentIndexManager()

    def get_deleted_documents(self):
        deleted = []
        records = self.registry.get_all_documents()

        for record in records:
            file_path = record["file_path"]
            if not Path(file_path).exists():
                deleted.append(record)
            
        return deleted
    
    def sync_deleted_documents(self):
        deleted = self.get_deleted_documents()
        for document in deleted:
            self.index_manager.remove_document(document["file_path"])
            self.registry.delete_document(document["file_path"])

            print("Deleted->", document["file_name"])

        return len(deleted)



