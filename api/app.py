
from fastapi import FastAPI
import joblib


import pandas as pd

from sklearn.preprocessing import StandardScaler

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression

app = FastAPI()

model = joblib.load('./model.joblib', mmap_mode=None)

# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}

@app.get("/predict")
def predict(acousticness, danceability, duration_ms, energy, explicit ,id , instrumentalness, key, liveness, loudness, mode,name, release_date, speechiness, tempo, valence, artist):

    ### TODO

    prediction = {'artist':None, 'song_name':None, 'popularity':None}
    return prediction


# Implement a /predict endpoint
