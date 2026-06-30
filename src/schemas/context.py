from dataclasses import dataclass


@dataclass
class ContextDocument:
    chunk_id: str
    source: str
    page: int
    content: str



@dataclass
class BuiltContext:
    query: str
    documents: list[ContextDocument]
    context_text: str



@dataclass
class CompressedChunk:
    chunk_id: str
    source: str
    page: int
    content: str