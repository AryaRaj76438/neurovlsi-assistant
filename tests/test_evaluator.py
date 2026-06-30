from src.evaluation.benchmark_loader import BenchmarkLoader
from src.evaluation.retrieval_evaluator import RetrievalEvaluator

loader = BenchmarkLoader()

benchmark = loader.load(
    "/Users/arya/Desktop/Machine Learning/neurovlsi/src/evaluation/benchmark_questions.json"
)

evaluator = RetrievalEvaluator()

result = evaluator.evaluate(
    benchmark
)

print(result)