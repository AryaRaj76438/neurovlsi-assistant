from src.retrieval.retrieval_pipeline import (
    RetrievalPipeline
)

from src.rag.answer_grounder import (
    AnswerGrounder
)

from src.rag.prompt_builder import (
    PromptBuilder
)

pipeline = RetrievalPipeline()

results = pipeline.retrieve(
    "What is a current mirror?"
)

grounder = AnswerGrounder()

grounded = grounder.ground(
    query="What is a current mirror?",
    chunks=results
)

builder = PromptBuilder()

prompt = builder.build(
    grounded
)

print(prompt.full_prompt)