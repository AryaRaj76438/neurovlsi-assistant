from src.chunking.chunk_loader import ChunkLoader


class SourceExpander:
    """
    Expands retrieved chunks with neighboring chunks
    from the same document.
    """

    def __init__(self):
        self.loader = ChunkLoader()

    def expand(
        self,
        retrieved_chunks,
        chunk_file,
        window=1
    ):
        all_chunks = self.loader.load(
            chunk_file
        )

        chunk_lookup = {
            chunk.chunk_id: chunk
            for chunk in all_chunks
        }

        expanded = {}

        for chunk in retrieved_chunks:

            expanded[
                chunk.chunk_id
            ] = chunk

            current_index = (
                chunk.chunk_index
            )

            for candidate in all_chunks:

                if (
                    candidate.document_path
                    != chunk.document_path
                ):
                    continue

                if abs(
                    candidate.chunk_index
                    - current_index
                ) <= window:

                    expanded[
                        candidate.chunk_id
                    ] = candidate

        return list(
            expanded.values()
        )