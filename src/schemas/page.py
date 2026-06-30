from dataclasses import dataclass


@dataclass
class PageRecord:
    document_path: str
    source: str
    page_number: int
    text: str