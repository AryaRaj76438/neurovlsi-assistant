import json

from src.embeddings.embedder import Embedder
from src.embeddings.embedding_store import (EmbeddingStore)


class EmbeddingPipeline:
    def __init__(self):
        self.embedder = Embedder()
        self.store = EmbeddingStore()

    def process(self,chunk_file,output_name):
        texts = []

        with open(
            chunk_file,
            "r",
            encoding="utf-8"
        ) as f:
            for line in f:
                record = json.loads(line)
                texts.append(record["text"])

        embeddings = self.embedder.embed_texts(texts)

        return self.store.save(embeddings,output_name)