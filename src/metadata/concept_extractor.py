from src.metadata.concept_dictionary import CONCEPTS

class ConceptExtractor:
    def extract(self, text):
        text_lower = text.lower()
        found = []
        for concept in CONCEPTS:
            if concept.lower() in text_lower:
                found.append(concept.lower())
        return sorted(list(set(found)))
