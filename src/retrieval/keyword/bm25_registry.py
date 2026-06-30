from src.retrieval.keyword.bm25_index import BM25Index

_bm25_index = None

def get_bm25_index():
    global _bm25_index 
    if _bm25_index is None:
        print("Building BM25 index")
        _bm25_index = BM25Index()
        _bm25_index.build()
    return _bm25_index