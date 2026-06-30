from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DIR = DATA_DIR / "processed"

CHUNKS_DIR = DATA_DIR / "chunks"

VECTOR_STORE_DIR = PROJECT_ROOT / "vector_store"

REGISTRY_DIR = PROJECT_ROOT / "registry"

CONFIG_DIR = PROJECT_ROOT / "configs"

EMBEDDINGS_DIR = DATA_DIR / "embeddings"
