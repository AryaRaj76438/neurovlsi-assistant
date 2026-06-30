from src.core.model_registry import get_embedding_model

print("First call")
m1 = get_embedding_model()

print("Second call")
m2 = get_embedding_model()

print("Third call")
m3 = get_embedding_model()

print(m1 is m2)
print(m2 is m3)