from src.ingestion.discovery import DocumentDiscovery

class DocumentRegistrar:
    def __init__(self):
        self.discovery = DocumentDiscovery()
        self.registry = self.discovery.registry

    def run(self):
        results = self.discovery.discover()

        new_documents = results["new"]
        modified_documents = results["modified"]
        existing_documents = results["existing"]

        for doc in new_documents:
            self.registry.register_document(doc)
        
        for doc in modified_documents:
            self.registry.update_document_hash(
                file_path=doc["file_path"],
                new_hash=doc["file_hash"],
                file_size=doc["file_size"]
            )

        summary = {
            "new": len(new_documents),
            "modified": len(modified_documents),
            "existing": len(existing_documents)
        }
        return summary
    def close(self):
        self.discovery.close()