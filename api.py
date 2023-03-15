from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
import numpy as np


from packages.cnn_model import make_predictions
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

@app.get('/')
def index():
    return {'status': True}

@app.post("/predict_ingredient")
def predict_ingredient():
    return make_predictions()


@app.post('/file')
def file_upload(
        my_file: bytes = File(...),
        shape: str = Form(...),
        dtype: str = Form(...)):
    from_bytes = np.frombuffer(my_file, dtype = dtype)
    reshape = from_bytes.reshape(eval(shape))
    list_images = crop_fridge(reshape,50)
    results = make_predictions(list_images)

    return {"list": results}

df_path = "docker_data/final_cleaned_recipes_dataset.pkl"
model_path = "docker_data/pickle_nlp_model"

@app.get("/suggest_recipes")
def predict(ingredients: str, preferences: str):
    ingredients_list = [ingred.strip() for ingred in ingredients.split(",")]
    preferences_list = [pref.strip() for pref in preferences.split(",")]
    suggestions = input_to_recipes_df(ingredients_list, preferences_list, df_path, model_path)
    return {"suggest_recipes": suggestions}
