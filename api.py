from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
import numpy as np
import pandas as pd
from gensim.utils import unpickle, pickle

from packages.cnn_model import make_predictions, load_best_model, load_vit_model
from PIL import Image
from packages.crop_fridge import crop_fridge
from pydantic import BaseModel
from packages.nlp_model import input_to_recipes_df

app = FastAPI(max_request_size=1000 * 1024 * 1024)

# Allow all requests (optional, good for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

#app.state.cnn_model =  load_best_model("cherry_picked_1500")

app.state.cnn_model =  load_vit_model()

@app.get('/')
def index():
    return {'status': True}

@app.post("/predict_ingredient")
def predict_ingredient():
    return make_predictions()


@app.post('/predict_ingreds')
def file_upload(
        my_file: bytes = File(...),
        shape: str = Form(...),
        dtype: str = Form(...)):

    from_bytes = np.frombuffer(my_file, dtype = dtype)
    reshape = from_bytes.reshape(eval(shape))

    list_images = [tuple_[0] for tuple_ in crop_fridge()[1]]

    results = make_predictions(list_images, app.state.cnn_model)

    return {"list": results}

df_path = "data/final_cleaned_recipes_dataset.pkl"
model_path = 'models/pickle_nlp_model'
df=pd.read_pickle(df_path)
model=unpickle(model_path)

@app.get("/suggest_recipes")
def predict(ingredients: str, preferences: str):
    ingredients_list = [ingred.strip() for ingred in ingredients.split(",")]
    preferences_list = [pref.strip() for pref in preferences.split(",")]
    suggestions = input_to_recipes_df(ingredients_list, preferences_list, df, model)
    return {"suggest_recipes": suggestions}
