import json
from pathlib import Path
from dataclasses import asdict

from src.core.paths import CHUNKS_DIR

class ChunkStore:
    def save(self, chunks, document_hash):
        output_path = CHUNKS_DIR/f"{document_hash}.jsonl"

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as f:
            for chunk in chunks:
                f.write(
                    json.dumps(
                        asdict(chunk),
                        ensure_ascii=False
                    )
                    + "\n"
                )

        return output_path