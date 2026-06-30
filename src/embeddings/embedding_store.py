import numpy as np

from src.core.paths import EMBEDDINGS_DIR


class EmbeddingStore:
    def save(self,embeddings,file_name):
        output_path = (EMBEDDINGS_DIR /f"{file_name}.npy")
        np.save(output_path,embeddings)

        return output_path

    def load(self,file_name):
        path = (EMBEDDINGS_DIR / f"{file_name}.npy")

        return np.load(path)