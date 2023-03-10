import streamlit as st

import numpy as np
import pandas as pd
from io import StringIO
import cv2

uploaded_file = st.file_uploader("Choose a file", type='jpg')
if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # Now do something with the image! For example, let's display it:
    st.image(opencv_image, channels="BGR")
