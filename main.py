from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Loading a model that acts as our Anxiety Classifier (BERT-based)
# In a full project, this would be your 'bert_anxiety_model.pt'
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

class AnxietyRequest(BaseModel):
    text: str

@app.post("/predict")
def predict_anxiety(request: AnxietyRequest):
    result = classifier(request.text)[0]
    
    # Logic to map sentiment to anxiety levels
    label = result['label']
    score = result['score']
    
    status = "Low Anxiety"
    if label == "NEGATIVE" and score > 0.7:
        status = "High Anxiety Detected"
    elif label == "NEGATIVE":
        status = "Moderate Anxiety"
        
    return {"status": status, "confidence": round(score, 4)}