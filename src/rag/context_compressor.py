from src.schemas.context import CompressedChunk


class ContextCompressor:
    """
    Extracts only the most relevant
    paragraphs from retrieved chunks.
    """

    def __init__(
        self,
        max_paragraphs=2
    ):
        self.max_paragraphs = max_paragraphs

    def compress(
        self,
        query,
        chunks
    ):
        query_words = {
            word.lower()
            for word in query.split()
        }

        compressed = []

        for chunk in chunks:

            paragraphs = [
                p.strip()
                for p in chunk.text.split("\n\n")
                if p.strip()
            ]

            scored = []

            for paragraph in paragraphs:

                paragraph_words = {
                    word.lower()
                    for word in paragraph.split()
                }

                overlap = len(
                    query_words &
                    paragraph_words
                )

                scored.append(
                    (
                        overlap,
                        paragraph
                    )
                )

            scored.sort(
                reverse=True,
                key=lambda x: x[0]
            )

            selected = [
                p
                for _, p in scored[
                    :self.max_paragraphs
                ]
            ]

            compressed.append(
                CompressedChunk(
                    chunk_id=chunk.chunk_id,
                    source=chunk.source,
                    page=chunk.page,
                    content="\n\n".join(
                        selected
                    )
                )
            )

        return compressed