import streamlit as st
from streamlit_extras.switch_page_button import switch_page


#### set favicon and title of the page in the browser tab
st.set_page_config(
            page_title="RECIPE RACCOON",
            page_icon=":raccoon:",
            layout="wide",
            initial_sidebar_state="collapsed")

st.title("Upload an image of your food ingredients here!")

## image uploader tab
uploaded_file = st.file_uploader("Upload your image here", type=['jpg','jpeg','png'])
#show image
if st.button('Uploading is not available in this version - Click here to use our sample image'):
    st.image("https://raw.githubusercontent.com/canndyy/your_kitchen_ai/master/streamlit_UI/st_ui_images/my_ingredients_copy.jpg", width = 500)


# preference drop down menu
prefs = ["Easy" ,"< 30 Mins","< 60 Mins","< 4 Hours","Meat","Vegetable",\
    "Fruit","Healthy","Inexpensive","Dessert","Beverages"]

user_prefs = st.multiselect('Preferences:', prefs)
custom_input = st.text_input("Any other keywords you would like to add? ")


# col1, col2, col3 = st.columns(3)
if st.button('Ready, steady, cook!'):
    st.image("https://raw.githubusercontent.com/canndyy/your_kitchen_ai/master/streamlit_UI/st_ui_images/my_ingredients_copy.jpg", width = 500)

    st.markdown("")
    st.markdown(f"Please note the actual model is not available for public access")
    st.markdown(f"The following is just an example display image of what the model is expected to return")
    st.markdown(f"Work is still being done on improving accuracy")

    st.image("https://raw.githubusercontent.com/canndyy/your_kitchen_ai/master/streamlit_UI/st_ui_images/model_prediction.jpeg")

for i in range(9):
    st.markdown("")

columns = st.columns((2, 1, 2))
get_recipes = columns[1].button("Click here to get your recipes! ")

if get_recipes:
    switch_page("recipes")
