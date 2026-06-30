from dataclasses import dataclass


@dataclass
class FusionChunk:
    chunk_id: str
    text: str
    source: str
    page: int
    document_path: str
    fusion_score: float