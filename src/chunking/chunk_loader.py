import json
from src.schemas.chunk import ChunkRecord

class ChunkLoader:
    def load(self, file_path):
        chunks = []
        
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                record = json.loads(line)
                chunks.append(ChunkRecord(**record))
        
        return chunks