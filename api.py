from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
import numpy as np
import pandas as pd
import cv2
import io
# from nlp_main import front_end_display
from packages.cnn_model import make_predictions
from PIL import Image
from packages.crop_fridge import crop_fridge
from pydantic import BaseModel


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
    return {'status': False}

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
