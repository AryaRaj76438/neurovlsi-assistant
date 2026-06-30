class RetrievalMetrics:

    @staticmethod
    def concept_hit(
        retrieved_text,
        expected_concepts
    ):
        text = retrieved_text.lower()

        for concept in expected_concepts:
            if concept.lower() in text:
                return True

        return False