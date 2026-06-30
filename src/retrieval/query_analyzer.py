from src.schemas.query import QueryAnalysis
from src.metadata.concept_extractor import ConceptExtractor
from src.metadata.application_classifier import ApplicationClassifer
from src.metadata.category_classifier import CategoryClassifier

class QueryAnalyzer:
    def __init__(self):
        self.concept_extractor = ConceptExtractor()
        self.application_classifier = ApplicationClassifer()
        self.category_classifier = CategoryClassifier()

    def analyze(self, query:str):
        lower_query = query.lower()
        concepts = self.concept_extractor.extract(lower_query)
        applications = self.application_classifier.classify(concepts)
        categories = self.category_classifier.classify(concepts)

        return QueryAnalysis(
            query=query,
            concepts=concepts,
            categories=categories,
            applications=applications
        )
    