from src.metadata.metadata_generator import MetadataGenerator

class MetadataPipeline:
    def __init__(self):
        self.generator = MetadataGenerator()

    def enrich(self, chunks):
        for chunk in chunks:
            metadata = self.generator.generate(chunk)
            chunk.metadata.update(metadata)
        
        return chunks
