from transformers import pipeline

# load model once when server starts
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

labels = [
    "Roads",
    "Electricity",
    "Water",
    "Safety",
    "Healthcare",
    "Infrastructure"
]


def classify_issue(text: str):
    result = classifier(text, labels)
    return result["labels"][0]