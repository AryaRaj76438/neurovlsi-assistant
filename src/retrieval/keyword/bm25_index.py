from rank_bm25 import BM25Okapi
from src.chunking.chunk_loader import ChunkLoader
from src.core.paths import CHUNKS_DIR

class BM25Index:
    def __init__(self):
        self.loader = ChunkLoader()
        self.documents = []
        self.tokenzied_documents = []
        self.index = None
    
    def build(self):
        chunk_files = list(CHUNKS_DIR.glob("*.jsonl"))
        chunks = []
        for file in chunk_files:
            chunks.extend(self.loader.load(file))
        
        self.documents = chunks

        self.tokenized_documents = [
            chunk.text.lower().split()
            for chunk in chunks
        ]
        self.index = BM25Okapi(self.tokenized_documents)
    
    def is_ready(self):
        return self.index is not None
