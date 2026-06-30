# import sys
# from pathlib import Path

# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.core.model_registry import (
    get_embedding_model,
    get_reranker_model
)

embedding_model = get_embedding_model()

reranker = get_reranker_model()

print("Models loaded successfully")