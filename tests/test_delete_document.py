from src.vector_store.chroma_store import (ChromaStore)

store = ChromaStore()

print("Before: ",store.count())

store.delete_document("/Users/arya/Desktop/Machine Learning/neurovlsi/data/raw/books/Lec-3.pdf")

print("After: ", store.count())