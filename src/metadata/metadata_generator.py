from src.metadata.concept_extractor import ConceptExtractor
from src.metadata.category_classifier import CategoryClassifier
from src.metadata.application_classifier import ApplicationClassifer

class MetadataGenerator:
    def __init__(self):
        self.extactor = ConceptExtractor()
        self.category_classifer = CategoryClassifier()
        self.application_classifier = ApplicationClassifer()
    
    def generate(self, chunk):
        concepts = self.extactor.extract(chunk.text)
        categories = self.category_classifer.classify(concepts)
        applications = self.application_classifier.classify(concepts)
        return {
            "concepts":concepts,
            "categories": categories,
            "applications": applications,
        }