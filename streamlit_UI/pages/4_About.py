import streamlit as st
from streamlit_extras.switch_page_button import switch_page

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
        background-color: #DCEAB2
}

</style>
""", unsafe_allow_html=True)


st.markdown(f"# About")
st.markdown(f"### Recipe Raccoon is an AI product that identify images of food ingredients \
            and suggest customised recipes")

for i in range(3):
    st.markdown("")
st.markdown(f"# Our Mission ")
col4, col5 = st.columns(2, gap="medium")
col4.markdown(f"#### :stew: Easier brainstorming of lunch/dinner/dessert")
col4.markdown(f"#### :bento: Allow users to experiment new recipes")
col5.markdown(f"#### :leafy_green: Better utilisation of ingredients")
col5.markdown(f"#### :wastebasket: Prevents food waste")

st.markdown("----")
st.markdown(f"### This product is built by [Candy](https://github.com/canndyy),\
    [Louis](https://github.com/JammyNinja), and [Paul](https://github.com/paulbridi)")
st.markdown(f"### Le Wagon Data Science bootcamp March 2023")
st.markdown("----")
