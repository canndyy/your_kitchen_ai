from roboflow import Roboflow
from PIL import Image
import os
import numpy as np

def crop_fridge(fp, confidence):

    MAX_SIZE = (2000,2000)

    rf = Roboflow(api_key=os.environ['ROBOFLOW_API'])
    project = rf.workspace().project("aicook-lcv4d")
    model = project.version(3).model

    im = Image.open(fp)
    im.thumbnail(MAX_SIZE)

    image_array = np.array(im)

    output_json = model.predict(image_array, confidence=confidence, overlap=30).json()
    image_list = []
    for items in output_json['predictions']:
        image_list.append(im.crop((items['x'] - (items['width']/2),\
                                   items['y'] - (items['height']/2),\
                                   items['x'] + (items['width']/2),\
                                   items['y'] + (items['height']/2)
                                  )))

    return image_list
