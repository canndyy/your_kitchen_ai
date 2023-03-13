import os
import pandas as pd
import numpy as np
import gensim.downloader
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from textblob import TextBlob, Word
import collections
import requests
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from nlp_model import input_to_recipes_df
import nlp_frontend

def front_end_display(input_ingred, input_tags, df_path, model_path):
    df = input_to_recipes_df(input_ingred, input_tags, df_path, model_path)
    nlp_frontend.print_recipe_names(df)
    nlp_frontend.list_all_recipes_info(df)
    nlp_frontend.show_recipe_images(df)

if __name__ == "__main__":
    input_ingred = "chicken, potato, spinach"
    input_tags = "dinner, easy"
    df_path = os.path.join("../test_data/kaggle_recipes", "r_cleaned_recipes_3.pkl")
    model_path = os.path.join("../../nlp_models", "nlp_model_cit.model")

    front_end_display(input_ingred, input_tags, df_path, model_path)
