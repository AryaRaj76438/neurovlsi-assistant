from src.retrieval.query_analyzer import QueryAnalyzer
from src.retrieval.reranker import Reranker
from src.retrieval.retriever import Retriever
from src.retrieval.deduplicator import Deduplicator
from src.retrieval.hybrid_retriever import HybridRetriever


class RetrievalPipeline:
    def __init__(self):
        self.analyzer = QueryAnalyzer()
        self.reranker = Reranker()
        self.retriever = HybridRetriever()
        self.deduplicator = Deduplicator()
    
    def retrieve(self, query, retrieve_k = 20, rerank_k = 5):
        analysis = self.analyzer.analyze(query)
        candidates = self.retriever.retrieve(analysis, top_k=retrieve_k)
        deduplicated = self.deduplicator.deduplicate(candidates)
        results = self.reranker.rerank(analysis, deduplicated, top_k=rerank_k)

        return results