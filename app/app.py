import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import cv2
from packages.crop_fridge import crop_fridge
from pydantic import BaseModel
import requests
from PIL import Image
import os

url = 'http://127.0.0.1:8003'
url = 'http://localhost:8000'

# url = "https://kitchen-api-hebwau5dkq-ew.a.run.app"
res = requests.get(url + "/")


# Load local css file to apply custom styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("app/style.css")

# Store user prefs, custom text input
prefs = ['healthy', 'quick', 'mexican','..']

user_prefs = st.sidebar.multiselect(
    'Preferences:',
    prefs,
    [])

custom_input = ""
custom_input = st.sidebar.text_input('Freestyle:')

# Upload fridge photo and return cropped photos of ingredients
uploaded_file = st.sidebar.file_uploader("Fridge:", type=['jpg','jpeg'])
if uploaded_file is not None:
    MAX_SIZE = (2000,2000)

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    image = Image.open(uploaded_file)
    image.thumbnail(MAX_SIZE)
    image.save(os.path.join("fridge_results","results.jpg"))

    st.image(image)

    # Crop ingredients from fridge using roboflow model and display
    cropped_images_data = crop_fridge()
    roboflow_ingredients = [item['class'] for item in cropped_images_data[0]['predictions']]
    roboflow_confidences = [item['confidence'] for item in cropped_images_data[0]['predictions']]

    ## make request to predict ingredients
    img_shape=opencv_image.shape
    dtype_arr=opencv_image.dtype
    byte_arr=opencv_image.tobytes()
    from_bytes = np.frombuffer(byte_arr, dtype = opencv_image.dtype)
    files = {'my_file': byte_arr}

    # send the POST request with the request body as multipart/form-data
    response = requests.post(
    url + '/predict_ingreds',
    files=files,
    data={'shape': str(img_shape), 'dtype': str(dtype_arr)}
    )

    # Get ingredients returned from model and prefences, store both as strings
    ingredients_list = [ingredient_data[0] for ingredient_data in response.json()['list']]
    ingredients_list_str = ','.join(ingredients_list)

    preferences_list = user_prefs + custom_input.split()
    preferences_list_str = ','.join(preferences_list)

    params = {"ingredients": ingredients_list_str, "preferences": preferences_list_str}

    # Loop through cropped images, returning image, ingredient, and confidence

    for ing, conf, cnn_data, image  in zip(roboflow_ingredients,roboflow_confidences, response.json()['list'], cropped_images_data[1]):
        st.write(f"CNN prediction: {cnn_data[0].capitalize()} ({cnn_data[1]}%)")
        st.write(f"Roboflow prediction: {ing.capitalize()}, {'{:.2%}'.format(conf)}")
        st.image(image[0])

    # Return recipes using NLP model
    response_nlp = requests.get(url + '/suggest_recipes',params=params)
    st.write(response_nlp)
