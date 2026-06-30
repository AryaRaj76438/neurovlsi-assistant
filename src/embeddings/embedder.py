import numpy as np

from src.core.model_registry import get_embedding_model


class Embedder:
    def __init__(self):
        self.model = get_embedding_model()

    def embed_texts(self, texts):
        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=False
        )

        return np.asarray(embeddings)
    
    def embed_query(self, query):
        embedding = self.model.encode(
            query, 
            normalize_embeddings=True
        )
        return np.asarray(embedding)