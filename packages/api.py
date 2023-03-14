from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
import numpy as np
import pandas as pd
import cv2
import io

from nlp_main import front_end_display
from cnn_model import make_predictions


app = FastAPI()

# Allow all requests (optional, good for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

df_path = "docker_data/final_cleaned_recipes_dataset.pkl"
model_path = "docker_data/pickle_nlp_model"


@app.get('/')
def index():
    return {'status': True}


@app.post("/predict_ingredient")
def predict_ingredient():
    return make_predictions()


@app.post('/upload_image')
async def receive_image(img: UploadFile=File(...)):
    ### Receiving and decoding the image
    contents = await img.read()

    nparr = np.fromstring(contents, np.uint8)
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray

    ### Do cool stuff with your image.... For example face detection
    ingredients = make_predictions(cv2_img)

    ### Encoding and responding with the image

@app.get("/suggest_recipes")
def predict(ingredients: str, preferences: str):
    ingredients_list = [ingred.strip() for ingred in ingredients.split(",")]
    preferences_list = [pref.strip() for pref in preferences.split(",")]
    suggestions = input_to_recipes_df(ingredients_list, preferences_list, df_path, model_path)
    # predictions = front_end_display(ingredients_list, preferences_list, df_path, model_path)
    return {"suggest_recipes": suggestions}
