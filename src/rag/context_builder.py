from src.schemas.context import (
    ContextDocument,
    BuiltContext
)
from src.rag.context_compressor import ContextCompressor

class ContextBuilder:
    def __init__(self, max_chunks=5):
        self.max_chunks = max_chunks
        self.compressor = ContextCompressor()

    def build(self, query, ranked_chunks):
        compressed_chunks = self.compressor.compress(
            query=query,
            chunks=ranked_chunks[:self.max_chunks]
        )

        documents = []
        context_parts = []

        for chunk in compressed_chunks:

            documents.append(
                ContextDocument(
                    chunk_id=chunk.chunk_id,
                    source=chunk.source,
                    page=chunk.page,
                    content=chunk.content
                )
            )

            context_parts.append(
                f"""
                [DOCUMENT]

                Source: {chunk.source}
                Page: {chunk.page}

                {chunk.content}
                """
            )

        context_text = "\n\n".join(
            context_parts
        )

        return BuiltContext(
            query=query,
            documents=documents,
            context_text=context_text
        )