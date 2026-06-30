from src.vector_store.chroma_store import ChromaStore
from src.schemas.retrieval import RetrievedChunk
class MetadataRetriever:
    def __init__(self):
        self.store = ChromaStore()

    def retrieve_by_concepts(self, concepts, limit=20):
        results = []
        collection = self.store.collection

        for concept in concepts:
            response = collection.get(
                where={
                    "concepts_text": concept
                },limit=limit
            )
            results.extend(self._convert_results(response))
        
        return results
    
    def retrieve_by_categories(self, categories, limit = 20):
        results = []
        collection = self.store.collection

        for category in categories:
            response = collection.get(
                where={
                    "categories_text": category
                },
                limit=limit
            )
            results.extend(self._convert_results(response))
        
        return results
    
    def retrieve(self, analysis, limit=20):
        results = []
        results.extend(self.retrieve_by_concepts(analysis.concepts, limit))
        results.extend(self.retrieve_by_categories(analysis.categories, limit))
        results.extend(self.retrieve_by_applications(analysis.applications, limit))
        
        return results

    def retrieve_by_applications(self, applications, limit=20):
        results = []
        collection = self.store.collection

        for application in applications:
            response = collection.get(
                where={
                    "applications_text": application
                },
                limit=limit
            )
            results.extend(self._convert_results(response))
        
        return results
    
    def _convert_results(self, response):
        chunks = []
        documents = response.get("documents", [])
        metadatas = response.get("metadatas", [])
        ids = response.get("ids", [])

        for chunk_id, text, metadata in zip(
            ids,
            documents,
            metadatas
        ):
            chunks.append(
                RetrievedChunk(
                    chunk_id=chunk_id,
                    text=text,

                    source=metadata.get(
                        "source",
                        ""
                    ),

                    page=metadata.get(
                        "page",
                        -1
                    ),

                    document_path=metadata.get(
                        "document_path",
                        ""
                    ),

                    distance=0.0,

                    chunk_index=metadata.get(
                        "chunk_index",
                        -1
                    ),

                    metadata={
                        "concepts": metadata.get(
                            "concepts_text",
                            ""
                        ),

                        "categories": metadata.get(
                            "categories_text",
                            ""
                        ),

                        "applications": metadata.get(
                            "applications_text",
                            ""
                        )
                    }
                )
            )
        return chunks