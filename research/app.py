import pandas as pd
import pickle
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Load the saved pipeline
with open('ipl_score_model.pkl', 'rb') as f:
    model_pipeline = pickle.load(f)

class MatchInput(BaseModel):
    venue: str
    batting_team: str
    bowling_team: str
    current_score: int
    wickets_lost: int
    overs_completed: float
    recent_overs_score: int

@app.post("/predict")
def predict(data: MatchInput):
    # 1. Convert input to DataFrame (Must match the order of your training columns)
    input_df = pd.DataFrame([data.dict()])
    
    # 2. Predict using the pipeline (Encoding is handled automatically!)
    prediction = model_pipeline.predict(input_df)
    
    return {"predicted_final_score": int(prediction[0])}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
