from src.retrieval.retrieval_pipeline import (
    RetrievalPipeline
)

from src.rag.answer_grounder import (
    AnswerGrounder
)

pipeline = RetrievalPipeline()

results = pipeline.retrieve(
    "What is current mirror?"
)

grounder = AnswerGrounder()

grounded = grounder.ground(
    query="What is current mirror?",
    chunks=results
)

for source in grounded.sources:

    print("=" * 80)

    print(source.source)
    print("Page:", source.page)

    print()
    print(source.evidence)