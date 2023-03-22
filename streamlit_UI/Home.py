import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import requests

################## WEBPAGE LAYOUT ###########################
# set favicon and title of the page in the browser tab
st.set_page_config(
            page_title="RECIPE RACCOON",
            page_icon=":raccoon:",
            layout="wide",
            initial_sidebar_state="collapsed")

#### CSS Styles ####
st.markdown("""
<meta charset="UTF-8">
<style>
.stApp {
    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("https://images.pexels.com/photos/2074130/pexels-photo-2074130.jpeg");
    background-size: 1500px 1000px;
    position: fixed;
    background-color: #77AF9C
}
.header {
    font-size:100px;
    text-align:center;
    color: #F1E9DA
}
.sub_header {
    font-size:50px;
    text-align:center;
    color: #F1E9DA
}
</style>
""", unsafe_allow_html=True)

# Title
for i in range(6):
    st.markdown("")
col = st.columns((0.5,0.5,3,0.5,0.5))
col[2].image("hhttps://raw.githubusercontent.com/canndyy/your_kitchen_ai/master/logo_1.jpeg")

st.markdown("----")
columns = st.columns((2, 1, 2))
get_started = columns[1].button("Let's Get Started !")
if get_started:
    switch_page("Intro")
st.markdown("----")
