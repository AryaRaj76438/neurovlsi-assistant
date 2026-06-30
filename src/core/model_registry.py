from sentence_transformers import SentenceTransformer
from FlagEmbedding import FlagReranker

from src.core.config import load_settings


_embedding_model = None
_reranker_model = None

def get_embedding_model():
    global _embedding_model

    if _embedding_model is None:
        settings = load_settings()
        print("Loading embedding model...")
        _embedding_model = SentenceTransformer(
            settings["models"]["embedding"]["name"]
        )

    return _embedding_model


def get_reranker_model():
    global _reranker_model

    if _reranker_model is None:
        settings = load_settings()
        print("Loading reranker model...")
        _reranker_model = FlagReranker(
            settings["models"]["reranker"]["name"],
            use_fp16=False
        )
    return _reranker_model