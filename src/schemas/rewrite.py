from dataclasses import dataclass

@dataclass
class RewrittenQuery:
    original_query: str
    rewritten_query: str
    rewritten: bool