from dataclasses import dataclass, field

@dataclass
class RetrievedChunk:
    chunk_id: str
    text: str

    source: str
    page: int
    document_path: str

    distance: float

    chunk_index: int = -1

    metadata: dict = field(
        default_factory=dict
    )

    