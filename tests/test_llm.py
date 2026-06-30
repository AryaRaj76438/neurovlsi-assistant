from src.llm.local_llm import LocalLLM

llm = LocalLLM()

response = llm.generate(
    "What is the application of current biasing and mirror ?"
)

print(response)