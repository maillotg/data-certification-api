
from fastapi import FastAPI

app = FastAPI()


# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}

@app.get("/predict")
def predict():
    prediction = {'artist':None, 'song_name':None, 'popularity':None}
    return prediction


# Implement a /predict endpoint
