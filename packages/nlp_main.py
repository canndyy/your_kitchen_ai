import os
import pandas as pd
import numpy as np
import gensim.downloader
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import requests
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from packages.nlp_model import input_to_recipes_df
from packages.nlp_frontend import print_recipe_names, list_all_recipes_info, show_recipe_images


def front_end_display(input_ingred:list, input_tags:list, df_path, model_path):
    df = input_to_recipes_df(input_ingred, input_tags, df_path, model_path)
    print_recipe_names(df)
    list_all_recipes_info(df)
    show_recipe_images(df)


if __name__ == "__main__":
    input_ingred = ["chicken", "potato", "spinach"]
    input_tags = ["dinner", "easy"]
    df_path = os.path.join("docker_data", "final_cleaned_recipes_dataset.pkl")
    model_path = os.path.join("docker_data", "final_nlp_model_cit_model.pkl")
    front_end_display(input_ingred, input_tags, df_path, model_path)
