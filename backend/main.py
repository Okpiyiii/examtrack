from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Exam Anxiety Detector API", description="API for predicting exam-related anxiety from text.")

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Based Exam Anxiety Detector API"}

@app.post("/predict")
def predict_anxiety(request: TextRequest):
    # TODO: Load and integrate the trained BERT model here
    # For now, this is a mock implementation
    return {"anxiety_level": "Moderate", "confidence": 0.85}
