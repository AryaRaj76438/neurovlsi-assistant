from src.core.model_registry import get_reranker_model
from src.schemas.reranking import RankedChunk

class Reranker:
    def __init__(self):
        self.model = get_reranker_model()

    def rerank(self, query, retrieved_chunks, top_k=5):
        pairs = []
        for chunk in retrieved_chunks:
            pairs.append([
                query.query,
                chunk.text
            ])
        scores = self.model.compute_score(pairs)

        ranked_pairs = sorted(
            zip(retrieved_chunks,scores),
            key=lambda x: x[1],
            reverse=True
        )

        results = []
        for chunk, score in ranked_pairs[:top_k]:
            results.append(
                RankedChunk(
                    chunk_id=chunk.chunk_id,
                    text=chunk.text,

                    source=chunk.source,
                    page=chunk.page,
                    document_path=chunk.document_path,

                    rerank_score=float(score),

                    chunk_index=chunk.chunk_index,

                    metadata=chunk.metadata
                )
            )
        return results