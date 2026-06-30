import numpy as np

from src.retrieval.keyword.bm25_registry import get_bm25_index
from src.schemas.retrieval import RetrievedChunk

class BM25Retriever:
    def __init__(self):
        self.index = get_bm25_index()

    def retrieve(self, query, top_k=20):
        tokens = (
            query.query.lower().split()
        )
        scores = (
            self.index.index.get_scores(tokens)
        )

        ranked_indices = np.argsort(scores)[::-1][:top_k]
        results = []
        
        for id in ranked_indices:
            chunk = self.index.documents[id]
            results.append(
                RetrievedChunk(
                    chunk_id=chunk.chunk_id,
                    text=chunk.text,
                    distance=float(scores[id]),
                    source=chunk.source,
                    page=chunk.page_number,
                    document_path=chunk.document_path
                )
            )

        return results

    
