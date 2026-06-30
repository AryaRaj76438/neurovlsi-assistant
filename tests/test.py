from src.metadata.category_classifier import CategoryClassifier

classifier = CategoryClassifier()

print(
    classifier.classify(
        ["current mirror"]
    )
)