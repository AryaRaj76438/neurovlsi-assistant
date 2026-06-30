from src.retrieval.query_analyzer import QueryAnalyzer


analyzer = QueryAnalyzer()

result = analyzer.analyze(
    "Explain current mirror operation"
)

print(result)