import streamlit as st
import requests

#### set favicon and title of the page in the browser tab
st.set_page_config(
            page_title="RECIPE RACCOON",
            page_icon=":raccoon:",
            layout="wide",
            initial_sidebar_state="collapsed")


url = 'http://0.0.0.0:8000'


if 'ings' not in st.session_state:
    st.session_state['ings'] = 0

if 'prefs' not in st.session_state:
    st.session_state['prefs'] = 0


parameters = {"ingredients": st.session_state['ings'],
              "preferences": st.session_state['prefs']}


################### NLP MODEL FUNCTIONS ####################

# call and get response for recipes
response_recipes = requests.get(url + "/suggest_recipes", params=parameters).json()

#converting response json to readable format
def get_recipes_expand(response_recipes):
    """ Returning top 5 recipes each in an st.expander """
    index_list = list(response_recipes['suggest_recipes'].keys())
    st.markdown(f"# These are the top 5 recipes we suggest based on your inputs  :cooking:")

    for i, index in enumerate(index_list):
        column_names = response_recipes['suggest_recipes'][index]
        with st.expander(f"{i+1} - {column_names['Name']}"):
            st.header(f":red[{column_names['Name']}]")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Recipe ID:** {index} \n")
                # st.markdown("")
                st.markdown(f"**Serving(s):** {column_names['recipe_servings']}")
                st.markdown(f"**Calories:** {column_names['Calories']} kcal \n")
                # st.markdown("")
            with col2:
                st.markdown(f"**Cook time:** {column_names['cook_time']}")
                st.markdown(f"**Preparation time:** {column_names['prep_time']}")
                st.markdown(f"**Total time:** {column_names['total_time']}\n")
                # st.markdown("")

            st.markdown(f"#### Ingredients")
            st.markdown(', '.join(column_names['ingredients']))

            st.markdown(f"\n#### Instructions")
            for i, step in enumerate(column_names['instructions'],1):
                st.markdown(f"{i}. {step}")
            st.markdown("")

            try:
                st.image(column_names["images"][0], caption = column_names['Name'], width=300)
            except:
                st.markdown(f"**Image not provided**")

    st.markdown(f"# HAPPY COOKING !")
try:
    get_recipes_expand(response_recipes)
except:
    st.markdown(f"Please upload fridge first!")
