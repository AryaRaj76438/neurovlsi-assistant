
from src.ingestion.registry import (
    DocumentRegistry
)

registry = DocumentRegistry()

record = registry.get_document_by_path(
    "/Users/arya/Desktop/Machine Learning/neurovlsi/data/raw/books/Digital Design, 5th Edition Morris Mano and Michael Ciletti.pdf"
)

print(record)