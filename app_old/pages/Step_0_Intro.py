import streamlit as st

#background image links
# "https://images.pexels.com/photos/616401/pexels-photo-616401.jpeg"

st.set_page_config(
            page_title="RECIPE RACCOON",
            page_icon=":raccoon:",
            layout="wide",
            initial_sidebar_state="collapsed")

st.markdown("""
<meta charset="UTF-8">
<style>
.stApp {
    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("https://images.pexels.com/photos/616401/pexels-photo-616401.jpeg");
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
col_b.markdown(f'# :one:\n ## Upload an image of your fridge and our AI will identify the food ingredients inside')
col_c.markdown(f"# :two:\n ## Specify your preferences")
col_d.markdown(f'# :three:\n ## Our app will suggest recipes based on ingredients and preferences you provide!')

st.markdown("----")
columns = st.columns((2, 1, 2))
get_started = columns[1].button("Upload Your Image Here  :raccoon: :raccoon: :raccoon:")
if get_started:
    switch_page("Step_1_Upload_Image")
st.markdown("----")

url_back = 'http://localhost:8502/'
st.markdown("[Back To Homepage](%s)" % url_back)