from pathlib import Path
from src.core.paths import RAW_DATA_DIR
import hashlib

SUPPORTED_EXTENSIONS = {".pdf"}

class DocumentScanner:
    def __init__(self):
        self.raw_data_dir = RAW_DATA_DIR
    
    def calculate_hash(self, file_path):
        sha256 = hashlib.sha256()

        with open(file_path, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                sha256.update(block)
        return sha256.hexdigest()
    
    def scan(self):
        documents = []

        for source_dir in self.raw_data_dir.iterdir():
            if not source_dir.is_dir():
                continue

            source_type = source_dir.name

            for file_path in source_dir.rglob("*"):
                if not file_path.is_file():
                    continue

                if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                    continue

                documents.append({
                    "file_name": file_path.name,
                    "file_path": str(file_path),
                    "file_size": file_path.stat().st_size,
                    "file_hash": self.calculate_hash(file_path),
                    "source_type": source_type
                })
        return documents
