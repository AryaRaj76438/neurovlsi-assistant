from pathlib import Path

from src.ingestion.pdf_loader import PDFLoader
from src.schemas.page import PageRecord


class DocumentExtractor:

    def __init__(self):
        self.pdf_loader = PDFLoader()

    def extract(self, document):

        file_path = Path(document["file_path"])

        if file_path.suffix.lower() != ".pdf":
            raise ValueError(
                f"Unsupported file type: {file_path.suffix}"
            )

        raw_pages = self.pdf_loader.load(file_path)

        return [
            PageRecord(
                document_path=document["file_path"],
                source=document["file_name"],
                page_number=page["page"],
                text=page["text"]
            )
            for page in raw_pages
        ]