from src.retrieval.retrieval_pipeline import RetrievalPipeline
from src.evaluation.metrics import RetrievalMetrics

class RetrievalEvaluator:

    def __init__(self):
        self.pipeline = RetrievalPipeline()

    def evaluate(
        self,
        benchmark
    ):
        total = len(benchmark)

        hits = 0

        for item in benchmark:

            results = self.pipeline.retrieve(
                item["question"]
            )

            context = "\n".join(
                [
                    r.text
                    for r in results
                ]
            )

            if RetrievalMetrics.concept_hit(
                context,
                item["expected_concepts"]
            ):
                hits += 1

        return {
            "total": total,
            "hits": hits,
            "accuracy":
            hits / total
        }