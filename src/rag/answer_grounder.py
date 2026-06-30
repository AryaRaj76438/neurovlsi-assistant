from src.schemas.grounding import (GroundedContext, GroundedSource)

class AnswerGrounder:
    """
    Converts retrieved chunks into
    source-aware evidence blocks.
    """
    def __init__(self, evidence_length = 500):
        self.evidence_length = evidence_length

    def ground(self, query, chunks):
        sources = []
        seen = set()


        for chunk in chunks:
            key = (
                chunk.source,
                chunk.page
            )

            if key in seen:
                continue

            seen.add(key)

            evidence = chunk.content[:self.evidence_length]
            
            sources.append(
                GroundedSource(
                    source=chunk.source,
                    page=chunk.page,
                    evidence=evidence
                )
            )
        return GroundedContext(
            query=query,
            sources=sources
        )
        