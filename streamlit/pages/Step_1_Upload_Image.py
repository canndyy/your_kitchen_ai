import streamlit as st

st.set_page_config(
            page_title="Your Kitchen AI",
            page_icon=":cooking:",
            # layout="centered",
            # initial_sidebar_state="auto"
            )

st.title("Upload an image of your food ingredients here!")
## image uploader tab
st.file_uploader("Upload your image here")

# preference drop down menu
prefs = ["Easy"
,"< 30 Mins"
,"< 60 Mins"
,"< 4 Hours"
,"Meat"
,"Vegetable"
,"Fruit"
,"Healthy"
,"Inexpensive"
,"Dessert"
,"Beverages"]

user_prefs = st.multiselect('Preferences:', prefs)

custom_input = st.text_input("Any other keywords you would like to add? (Separate each keyword with a whitespace)", label_visibility="visible")
