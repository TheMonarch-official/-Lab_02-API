import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(
    title="Sentiment Analysis API",
    description="API phân tích cảm xúc câu tiếng Anh bằng DistilBERT (Hugging Face).",
)

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
)

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {
        "name": "Sentiment Analysis API",
        "description": "Gửi một câu tiếng Anh, nhận về cảm xúc POSITIVE hoặc NEGATIVE.",
        "model": "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
        "endpoints": ["GET /", "GET /health", "POST /predict"],
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: TextInput):
    text = data.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text must not be empty.")
    if len(text) > 2000:
        raise HTTPException(status_code=400, detail="Text too long (max 2000 characters).")
    try:
        result = classifier(text, truncation=True)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model inference failed: {e}")
    return {
        "input": text,
        "label": result["label"],
        "score": round(result["score"], 4),
    }