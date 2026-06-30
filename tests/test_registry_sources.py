# tests/test_registry_sources.py

from src.ingestion.registry import (
    DocumentRegistry
)

registry = DocumentRegistry()

for row in registry.get_all_documents():
    print(
        row
    )