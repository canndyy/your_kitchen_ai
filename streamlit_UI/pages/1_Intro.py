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
    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("https://raw.githubusercontent.com/canndyy/your_kitchen_ai/master/intro_bg%20_large.jpeg");
    background-size: 1500px 1000px;
    position: fixed;
}
.how_it_works {
    font-size: 60px;
    color: #F0FFFF;
    text-align: center;
}
.css-10trblm {
    font-size: 30px;
    color: #F0FFFF
}

</style>
""", unsafe_allow_html=True)

###### webpage contents########

st.markdown("")
# How it works
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown('<p class="how_it_works"><b>How it works<b></p>', unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
col_a, col_b, col_c, col_d, col_e = st.columns((0.5,2,1.5,2,0.5), gap="medium")
col_b.markdown(f'# :one:\n ## Upload an image of your food ingredients and our AI will identify what is inside')
col_c.markdown(f"# :two:\n ## Specify your preferences")
col_d.markdown(f'# :three:\n ## Our app will suggest recipes based on ingredients and preferences you provide!')

st.markdown("----")
columns = st.columns((1,2, 2, 1))
get_started = columns[1].button("I want to upload an image !! ")
if get_started:
    switch_page("upload")

about_us = columns[2].button(" About Us ")
if about_us:
    switch_page("about")
st.markdown("----")
