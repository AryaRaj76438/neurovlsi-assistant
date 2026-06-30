from src.schemas.grounding import GroundedSource

class CitationInjector:
    """
    Adds numbered citations
    to generated answers.
    """

    def inject(
        self,
        answer,
        sources
    ):
        references = []

        for index, source in enumerate(
            sources,
            start=1
        ):
            references.append(
                f"[{index}] "
                f"{source.source} "
                f"(Page {source.page})"
            )

        reference_block = "\n".join(
            references
        )

        return (
            answer
            + "\n\n"
            + "Sources\n"
            + "--------\n"
            + reference_block
        )