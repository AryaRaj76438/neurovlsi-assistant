from dataclasses import dataclass, field


@dataclass
class QueryAnalysis:
    query: str
    concepts: list[str] = field(
        default_factory=list
    )
    categories: list[str] = field(
        default_factory=list
    )
    applications: list[str] = field(
        default_factory=list
    )