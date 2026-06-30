from src.ingestion.document_synchronizer import DocumentSynchronizer

sync = DocumentSynchronizer()
count = sync.sync_deleted_documents()
print(f"Deleted documents: {count}")