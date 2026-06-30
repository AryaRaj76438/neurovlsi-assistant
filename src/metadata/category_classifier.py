from src.metadata.category_dictionary import CATEGORY_RULES

class CategoryClassifier:
    def classify(self, concepts):
        categories = set()
        concept_set = {concept.lower() for concept in concepts}

        for category,  keywords in CATEGORY_RULES.items():
            for keyword in keywords:
                if keyword.lower() in concept_set:
                    categories.add(category)
                    break
        
        return sorted(list(categories))

