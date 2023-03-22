![alt text](https://raw.githubusercontent.com/canndyy/your_kitchen_ai/master/logo_1.jpeg)

# RECIPE RACCOON

Recipe Raccoon is a Computer Vision and NLP AI product built with Python that identify images of food ingredients and suggest customised recipes.

The product is a deep learning model that consists of:

1) Object detection Model - transfer learning from [Roboflow aicook](https://universe.roboflow.com/karel-cornelis-q2qqg/aicook-lcv4d)

2) Image Recognition Model - developed using Convolutional Neural Network (CNN) and Vision Transformer (ViT) with Tensorflow Keras

3) Recipe Processing Model - developed using Natural Language Processing (NLP) with Gensim Doc2vec

Built by [Candy](https://github.com/canndyy), [Louis](https://github.com/JammyNinja), and [Paul](https://github.com/paulbridi) in the Le Wagon Data Science bootcamp in March 2023.


## Demo
Feel free to explore our work, however as our CNN and NLP models are no longer available on a cloud platform, the application is no longer running :(

This is a streamlit link of our application's expected user experience if you are interested: [RECIPE RACCOON](https://bit.ly/3FHS2Gv)


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.txt.

```bash
pip install requirements.txt
```

To create a local web server run the following with uvicorn:

```bash
uvicorn api:app --reload --host 0.0.0.0
```

To run the frontend use streamlit to run our Home.py:

```bash
streamlit run app/Home.py
```

## Datasets 

### Image dataset
We manually went through and used some images in the following 3 datasets, with some images also obtained through image web scrapping from mainstream supermarket websites, Google Shopping and Google Image.

Our final image dataset contains 26 classes of food ingredients with at least 300 images in each class after data augmentation.

[Fruits-262](https://www.kaggle.com/datasets/aelchimminut/fruits262)

[Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset)

[Fruits and Vegetables Image Recognition Dataset](https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition) - As of 22 Mar 23 this dataset contains incorrect images, with test images also found inside validation and training set. Filtering is required before using.

### Recipe dataset
[Food.com - Recipes and Reviews](https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews)
