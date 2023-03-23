![alt text](https://raw.githubusercontent.com/canndyy/your_kitchen_ai/master/logo_1.jpeg)

# RECIPE RACCOON

Recipe Raccoon is a Computer Vision and NLP AI product built with Python that identify images of food ingredients and suggest customised recipes.

The product is a deep learning model that consists of:

1) Object detection Model - transfer learning from [Roboflow aicook](https://universe.roboflow.com/karel-cornelis-q2qqg/aicook-lcv4d)

2) Image Recognition Model - developed using Convolutional Neural Network (CNN) and Vision Transformer (ViT) with Tensorflow Keras

3) Recipe Processing Model - developed using Natural Language Processing (NLP) with Gensim Doc2vec

Built by [Candy](https://github.com/canndyy), [Louis](https://github.com/JammyNinja), and [Paul](https://github.com/paulbridi) in the Le Wagon Data Science bootcamp in March 2023.

## Language and tools used
<p align="left"> <a href="https://cloud.google.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/> </a> <a target="_blank" rel="noreferrer"> <img src="https://upload.vectorlogo.zone/logos/streamlitio/images/1548df31-a8e4-409b-a034-f2ddaa80670a.svg" alt="streamlit" width="40" height="40"/> </a> <a target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/numpy/numpy-ar21.svg" alt="NumPy" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a><a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/> </a> </p>

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
