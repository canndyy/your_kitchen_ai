![alt text](https://raw.githubusercontent.com/canndyy/your_kitchen_ai/master/logo_1.jpeg)

# RECIPE RACCOON

Recipe Raccoon is a Computer Vision and NLP AI product built with Python that identify images of food ingredients and suggest customised recipes.

The product is a deep learning model that consists of:

1) Object detection Model - transfer learning from [Roboflow aicook](https://universe.roboflow.com/karel-cornelis-q2qqg/aicook-lcv4d)

2) Image Recognition Model - developed using Vision Transformer (ViT)

3) Recipe Processing Model - developed using Natural Language Processing (NLP)

Built by [Candy](https://github.com/canndyy), [Louis](https://github.com/JammyNinja), and [Paul](https://github.com/paulbridi) in the Le Wagon Data Science bootcamp in March 2023.

## Aim
We want to create a product that can allow users to explore new recipe ideas and better utilise their food ingredients to reduce food waste.

## Language and Tools used
<p align="left">
<a href="https://www.python.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" title="python" width="40" height="40"/></a>
<a href="https://cloud.google.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" title="google cloud platform" width="40" height="40"/> </a> 
<a href="https://streamlit.io/" target="_blank" rel="noreferrer"> <img src="https://upload.vectorlogo.zone/logos/streamlitio/images/1548df31-a8e4-409b-a034-f2ddaa80670a.svg" alt="streamlit" title="streamlit" width="40" height="40"/> </a> 
<a href="https://numpy.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/numpy/numpy-ar21.svg" alt="NumPy" title="numpy" width="40" height="40"/> </a> 
<a href="https://git-scm.com/" target="_blank" rel="noreferrer"><img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png" alt="Git" title="Git" width="40" height="40"/> </a> 
<a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" title="pandas" width="40" height="40"/> </a> 
<a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> 
<img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" title="tensorflow" width="40" height="40"/> </a>  
<a href="https://radimrehurek.com/gensim/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/RaRe-Technologies/gensim/develop/docs/src/readme_images/rare.png" alt="gensim" title="gensim" width="40" height="40"/> </a>
<a href="https://matplotlib.org/" target="_blank" rel="noreferrer">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo.svg.png" alt="Matplotlib" title="matplotlib" width="40" height="40"/></a> 
<a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> 
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8ncV_JyWU0rI630Inb4rx6rbkAncme53QTc3yfzpvqUvcKzPAypFeAyv8XjkNj5Okt28&usqp=CAU " alt="seaborn" title="seaborn" width="40" height="40"/></a>    
<a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer">
<img src="https://pbs.twimg.com/profile_images/1417542931209199621/fWMEIB5j_400x400.jpg" alt="fastapi" title="FastAPI" width="40" height="40"/></a> 
<a href="https://www.uvicorn.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png" alt="uvicorn" title="uvicorn" width="40" height="40"/></a> <a target="_blank" rel="noreferrer"></a>
<a href="https://opencv.org/" target="_blank" rel="noreferrer">
<img src="https://upload.wikimedia.org/wikipedia/commons/3/32/OpenCV_Logo_with_text_svg_version.svg" alt="opencv" title="OpenCV" width="40" height="40"/></a> 
<a href="https://jupyter.org/" target="_blank" rel="noreferrer"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1200px-Jupyter_logo.svg.png" alt="jupyter" title="jupyter" width="40" height="40"/></a> 
<a href="https://www.selenium.dev/" target="_blank" rel="noreferrer"> 
<img src="https://camo.githubusercontent.com/4b95df4d6ca7a01afc25d27159804dc5a7d0df41d8131aaf50c9f84847dfda21/68747470733a2f2f73656c656e69756d2e6465762f696d616765732f73656c656e69756d5f6c6f676f5f7371756172655f677265656e2e706e67" alt="selenium" title="selenium" width="40" height="40"/></a>    
</p>


## Demo
Feel free to explore our work, however as our models are no longer available on a cloud platform, the application is no longer running :(

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
