from src.ingestion.scanner import DocumentScanner
from src.ingestion.registry import DocumentRegistry


class DocumentDiscovery:

    def __init__(self):
        self.scanner = DocumentScanner()
        self.registry = DocumentRegistry()

    def discover(self):

        documents = self.scanner.scan()

        new_documents = []
        existing_documents = []
        modified_documents = []

        for document in documents:

            db_record = self.registry.get_document_by_path(
                document["file_path"]
            )

            if db_record is None:
                new_documents.append(document)
                continue

            # update the document record with the latest hash
            # stored_hash = db_record[3]
            stored_hash = db_record["file_hash"]

            if stored_hash == document["file_hash"]:
                existing_documents.append(document)
            else:
                modified_documents.append(document)

        return {
            "new": new_documents,
            "existing": existing_documents,
            "modified": modified_documents
        }

    def close(self):
        self.registry.close()