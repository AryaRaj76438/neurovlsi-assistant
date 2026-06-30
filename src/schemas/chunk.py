from dataclasses import dataclass, field


@dataclass
class ChunkRecord:
    chunk_id: str
    text: str
    source: str
    document_path: str
    page_number: int
    chunk_index:int
    metadata: dict = field(default_factory=dict)
