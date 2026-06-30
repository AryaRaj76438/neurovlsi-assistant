from src.retrieval.retrieval_pipeline import RetrievalPipeline
from src.retrieval.source_expander import SourceExpander

pipeline = RetrievalPipeline()
expander = SourceExpander()

results = pipeline.retrieve(
    "What is a current mirror?"
)

expanded = expander.expand(
    retrieved_chunks=results,
    chunk_file="/Users/arya/Desktop/Machine Learning/neurovlsi/data/chunks/f4966d3f00e582f459896bc204ae11c1b5bef7323f8d42020d1ee364e619ab6f.jsonl",
    window=1
)

print("Retrieved:", len(results))
print("Expanded:", len(expanded))