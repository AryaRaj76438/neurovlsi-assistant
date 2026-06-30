from src.embeddings.embedder import Embedder
from src.vector_store.chroma_store import ChromaStore
from src.schemas.retrieval import RetrievedChunk

class Retriever:
    def __init__(self):
        self.embedder = Embedder()
        self.store = ChromaStore()

    def retrieve(self, query, top_k=20):
        query_embedding = self.embedder.embed_query(query.query)
        
        results = (
            self.store.collection.query(
                query_embeddings=[
                    query_embedding.tolist()
                ],
                n_results=top_k,
                include=[
                    "documents",
                    "metadatas",
                    "distances"
                ]
            )
        )

        retrieved = []
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]
        ids = results["ids"][0]

        for idx in range(len(documents)):
            retrieved.append(
                RetrievedChunk(
                    chunk_id=ids[idx],
                    text=documents[idx],

                    source=metadatas[idx]["source"],
                    page=metadatas[idx]["page"],
                    document_path=metadatas[idx]["document_path"],

                    distance=distances[idx],

                    chunk_index=metadatas[idx].get(
                        "chunk_index",
                        -1
                    ),

                    metadata={
                        "concepts": metadatas[idx].get(
                            "concepts_text",
                            ""
                        ),

                        "categories": metadatas[idx].get(
                            "categories_text",
                            ""
                        ),

                        "applications": metadatas[idx].get(
                            "applications_text",
                            ""
                        )
                    }
                )
            )            
        return retrieved