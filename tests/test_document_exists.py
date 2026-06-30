from src.vector_store.chroma_store import (ChromaStore)

store = ChromaStore()

exist2 = store.document_exists("tmp/arya.pdf")
exist1 = store.document_exists("/Users/arya/Desktop/Machine Learning/neurovlsi/data/raw/books/Design-of-Analog-CMOS-Integrated-Circuits.pdf")

print(f" {exist2} , {exist1}")
