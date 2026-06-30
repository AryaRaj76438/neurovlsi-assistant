from uuid import uuid4
import hashlib
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
from src.chunking.id_generator import generate_chunk_id
from src.core.config import load_settings
from src.schemas.chunk import ChunkRecord


class DocumentChunker:
    def __init__(self):
        settings = load_settings()

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings["chunking"]["chunk_size"],
            chunk_overlap=settings["chunking"]["chunk_overlap"],
            length_function=len
        )

    def chunk_pages(self, pages):
        chunks = []
        global_chunk_index = 0
        for page in pages:
            splits = self.splitter.split_text(
                page.text
            )
            
            for split in splits:
                chunks.append(
                    ChunkRecord(
                        chunk_id=generate_chunk_id(
                            page.document_path,
                            page.page_number, 
                            split
                        ),
                        text=split,
                        source=page.source,
                        document_path=page.document_path,
                        chunk_index=global_chunk_index,
                        page_number=page.page_number,
                    )
                )
                global_chunk_index+=1

        return chunks