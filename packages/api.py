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

df_path = "docker_data/nlp_model_cit.pkl"
model_path = "docker_data/final_cleaned_recipes_dataset.pkl"

@app.get('/')
def index():
    return {'status': True}


# @app.post('/upload_image')
# async def receive_image(img: UploadFile=File(...)):
#     ### Receiving and decoding the image
#     contents = await img.read()

#     nparr = np.fromstring(contents, np.uint8)
#     cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray

#     ### Do cool stuff with your image.... For example face detection
#     annotated_img = annotate_face(cv2_img)

#     ### Encoding and responding with the image
#     im = cv2.imencode('.png', annotated_img)[1] # extension depends on which format is sent from Streamlit
#     return Response(content=im.tobytes(), media_type="image/png")

@app.get("/predict")
def predict(ingredients: list, *preferences):
    df_path = "../docker_data/final_nlp_model_cit.model"
    model_path = "../docker_data/final_cleaned_recipes_dataset.pkl"
    predictions = nlp_main.front_end_display(ingredients, preferences, df_path, model_path)
    return {"predictions": predictions}

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



@app.get("/predict")
def predict(ingredients: str, preferences: str):
    ingredients_list = [ingred.strip() for ingred in ingredients.split(",")]
    preferences_list = [pref.strip() for pref in preferences.split(",")]

    predictions = input_to_recipes_df(ingredients_list, preferences_list, df_path, model_path)
    # predictions = front_end_display(ingredients_list, preferences_list, df_path, model_path)
    return {"predictions": predictions}

@app.get("/test")
def hello(ingredients:str, preferences:str):
    return{"ingred": ingredients,
           "pref": preferences }

    return ingredients

