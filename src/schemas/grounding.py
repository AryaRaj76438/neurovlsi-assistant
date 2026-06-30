from dataclasses import dataclass

@dataclass
class GroundedSource:
    source: str
    page: int
    evidence: str

@dataclass
class GroundedContext:
    query: str
    sources: list[GroundedSource]