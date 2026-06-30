# src/retrieval/retrieval_fusion.py

class RetrievalFusion:
    """
    Reciprocal Rank Fusion (RRF)

    Inputs
    ------
    vector_results : List[RetrievedChunk]
    bm25_results : List[RetrievedChunk]
    metadata_results : List[RetrievedChunk]

    Returns
    -------
    List[FusionChunk]
    """

    def fuse(
        self,
        vector_results,
        bm25_results,
        metadata_results,
        top_k=20,
        rrf_k=60
    ):
        fusion_scores = {}
        chunk_lookup = {}

        result_sets = [
            vector_results,
            bm25_results,
            metadata_results
        ]

        for results in result_sets:

            for rank, chunk in enumerate(results, start=1):

                score = 1 / (rrf_k + rank)

                fusion_scores[chunk.chunk_id] = (
                    fusion_scores.get(
                        chunk.chunk_id,
                        0.0
                    )
                    + score
                )

                chunk_lookup[chunk.chunk_id] = chunk

        ranked = sorted(
            fusion_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        final_results = []

        for chunk_id, score in ranked[:top_k]:

            chunk = chunk_lookup[chunk_id]
            chunk.fusion_score = score

            final_results.append(chunk)

        return final_results