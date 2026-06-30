from src.retrieval.retriever import Retriever
from src.retrieval.keyword.bm25_retriever import BM25Retriever
from src.retrieval.metadata_retriever import MetadataRetriever
from src.retrieval.retrieval_fusion import RetrievalFusion


class HybridRetriever:
    """
    Inputs
    ------
    query : str

    Returns
    -------
    List[FusionChunk]
    """

    def __init__(self):
        self.vector_retriever = Retriever()
        self.bm25_retriever = BM25Retriever()
        self.metadata_retriever = MetadataRetriever()
        self.fusion = RetrievalFusion()

    def retrieve(
        self,
        query,
        top_k=20
    ):
        vector_results = self.vector_retriever.retrieve(
            query=query,
            top_k=top_k
        )

        bm25_results = self.bm25_retriever.retrieve(
            query=query,
            top_k=top_k
        )

        metadata_results = self.metadata_retriever.retrieve(
            query,
            top_k
        )

        return self.fusion.fuse(
            vector_results=vector_results,
            bm25_results=bm25_results,
            metadata_results=metadata_results,
            top_k=top_k
        )