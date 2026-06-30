from src.metadata.application_dictionary import APPLICATION_RULES

class ApplicationClassifer:
    def classify(self, concepts):
        applications = set()
        concept_set = [concept.lower() for concept in concepts]

        for application, keywords in APPLICATION_RULES.items():
            for keyword in keywords:
                if keyword.lower() in concept_set:
                    applications.add(application)
                    break
        
        return sorted(list(applications))