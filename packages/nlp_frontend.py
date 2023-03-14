import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from io import BytesIO
from urllib.request import urlopen

def print_recipe_names(df_path):
    """Take a dataframe of recipes and print df_path['Name]"""

    print(f"These are the top 5 recipes of closest match to your ingredients and preferences: \n")
    for i, index in df_path.iterrows():
        print(f"{i+1} - {index['Name']}")
    print("\n***************\n")


def list_all_recipes_info(df_path):
    """Take a dataframe of recipes and print out all info"""

    for i, index in df_path.iterrows():
        print(f"Recipe Name: {index['Name']}")
        print(f"Recipe ID: {index['index']}\n")

        print(f"Cook Time: {index['cook_time']}")
        print(f"Preparation Time: {index['prep_time']}")
        print(f"Total Time: {index['total_time']}")

        print(f"Serving(s): {index['recipe_servings']}")
        print(f"Calories: {index['Calories']} kcal\n")

        print("Ingredients and Quantities")
        for i, ingredient in enumerate(index["ingredients"]):
            # try:
                # print(f"{index['ingredient_quantities'][i]} {ingredient.capitalize()}")
                print(f"{ingredient.capitalize()}")
            # except:
            #     print(f"{ingredient.capitalize()}")
        print("")

        print("Instructions")
        for i, instruction in enumerate(index['instructions'],1):
            print(f"{i}. {instruction}")

        print("\n===============\n")


def show_recipe_images(df_path):
    """Take dataframe of recipes and number of images to display, function displays images of the recipes '"""

    rows = 5

    fig, axes = plt.subplots(rows, 1)
    fig.set_size_inches(3,15)
    fig.tight_layout(pad=1.0)

    for i,image in enumerate(df_path['images']):
        try:
            response = requests.get(image[0])
            img = Image.open(BytesIO(response.content))
        except:
            axes[i].set_yticklabels([])
            axes[i].set_xticklabels([])
            axes[i].axis('off')
            axes[i].text(0, 0.7,f"{df_path['Name'][i]}:\nImage Not Provided", fontsize = "large")
            continue
        axes[i].set_title(f"{df_path['Name'][i]}", fontsize = "large")
        axes[i].axis('off')
        axes[i].imshow(img)

if __name__ == "__main__":
    df_path = os.path.join("../docker_data", "final_cleaned_recipes_dataset.pkl")

    print_recipe_names(df_path)
    list_all_recipes_info(df_path)
    show_recipe_images(df_path)
