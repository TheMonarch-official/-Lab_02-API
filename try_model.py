from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
)

texts = [
    "I love this movie!",
    "This is the worst day ever.",
    "The weather is okay.",
]

for t in texts:
    print(t, "->", classifier(t))
