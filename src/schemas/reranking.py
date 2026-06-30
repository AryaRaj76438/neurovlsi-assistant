from dataclasses import dataclass, field

@dataclass
class RankedChunk:
    chunk_id: str
    text: str

    source: str
    page: int
    document_path: str

    rerank_score: float

    chunk_index: int = -1

    metadata: dict = field(
        default_factory=dict
    )