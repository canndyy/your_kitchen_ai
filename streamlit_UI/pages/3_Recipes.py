import streamlit as st
import requests

#### set favicon and title of the page in the browser tab
st.set_page_config(
            page_title="RECIPE RACCOON",
            page_icon=":raccoon:",
            layout="wide",
            initial_sidebar_state="collapsed")


# url = 'http://0.0.0.0:8000'


# if 'ings' not in st.session_state:
#     st.session_state['ings'] = 0

# if 'prefs' not in st.session_state:
#     st.session_state['prefs'] = 0


# parameters = {"ingredients": st.session_state['ings'],
#               "preferences": st.session_state['prefs']}

#####dummy data######
response_recipes = {'suggest_recipes': {'360027': {'Name': 'Fragrant Orange and Lemon Cake', 'RecipeCategory': 'Dessert', 'Calories': 476.1, 'images': ['Not Provided'], 'cook_time': '55 Minute(s) ', 'prep_time': '25 Minute(s) ', 'total_time': '1 Hour(s) 20 Minute(s) ', 'recipe_servings': 'Not Provided', 'tags': ['lemon', 'oranges', 'citrus', 'fruit', '< 4 hours'], 'instructions': ['Preheat oven to 350 degrees.', 'Evenly coat the interior of a 10-inch bundt pan with butter;dust lightly with flour.', 'Shaking out the excess flour;set aside.', 'Sift the flour.', 'Baking powder.', 'Baking soda,and salt into a large bowl.', 'Stir in the orange and lemon zests.', 'Combine the orange and lemon juices and the milk and set aside to \"sour\" the milk.', 'Toss the vanilla with the sugar in a small bowl until the vanilla is mixed in well(it will make the sugar look fluffy).', 'In a large bowl.', 'Using a hand-held electric mixer at high speed.', 'Beat the butter and vanilla sugar until light and fluffy.', 'About 2 minutes.', 'One at a time.', 'Beat in the eggs.', 'Mixing well after each addition.', "The mixture will look curdled- don't worry.", 'Alternating in thirds.', 'Add the flour and milk mixtures.', 'Beating well after each addition.', 'And scraping down the sides of the bowl with a spatula as needed.', 'Pour the batter into the prepared pan and place in the center of the oven.', 'Bake until the cake is an even golden brown and a toothpick inserted in the center comes out clean.', '45 to 55 minutes.', "(don't worry if the cracks in the top of the cake don't look dry-use the toothpick test to test for doneness.).", 'Transfer to a wire rack to cool in the pan for 10 minutes.', 'Turn out onto the serving plate.', "Cool completely and sift confectioner's sugar over top.", 'Slice into wedges and serve.'], 'ingredient_quantities': ['na', 'na', '3', '1 1/2', '1/2', '1/4', '1', '1', '3/4', '8', '1 1/2', '1', '5', 'na'], 'ingredients': ['unsalted butter', 'all-purpose flour', 'all-purpose flour', 'baking powder', 'baking soda', 'salt', 'orange', 'lemon', 'milk', 'unsalted butter', 'sugar', 'vanilla', 'eggs', "confectioners' sugar"], 'ingredients_cleaned': ['orange', 'lemon', 'milk', '', 'egg', 'confectioner'], 'ingred_and_tags': ['orange', 'lemon', 'milk', '', 'egg', 'confectioner', 'lemon', 'oranges', 'citrus', 'fruit', '< 4 hours'], 'name_cat_ingred_tag': ['Fragrant', 'Orange', 'and', 'Lemon', 'Cake', 'Dessert', 'orange', 'lemon', 'milk', '', 'egg', 'confectioner', 'lemon', 'oranges', 'citrus', 'fruit', '< 4 hours'], 'cat_ingred_tag': ['Dessert', 'orange', 'lemon', 'milk', '', 'egg', 'confectioner', 'lemon', 'oranges', 'citrus', 'fruit', '< 4 hours']}, '66621': {'Name': 'Paradise Pear Jam', 'RecipeCategory': 'Fruit', 'Calories': 681.9, 'images': ['https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/71/18/6/picaawsax.jpg'], 'cook_time': '1 Minute(s) ', 'prep_time': '30 Minute(s) ', 'total_time': '31 Minute(s) ', 'recipe_servings': 'Not Provided', 'tags': ['free of...', '< 60 mins'], 'instructions': ['Remove rinds from orange and lemon in quarters; discard about half the white part of rinds.', '(scrape off with a spoon) slice rinds thinly.', 'Chop orange and lemon.', 'And discard seeds.', 'Peel.', 'Core and grind pears.', 'Combine all the fruits.', 'Including cherries and pineapple and its juice.', 'Measure 4 1/2 cups of fruit into a large pan.', 'Stir pectin into fruit.', 'Place over high heat.', 'Stirring until mixture comes to a hard boil.', 'At once stir in sugar.', 'Bring to a full rolling boil and boil hard for 1 minute.', 'Stirring constantly.', 'Remove from heat and skim.', 'Stir and skim for 5 minutes to cool slightly.', 'And prevent floating fruit.', 'Ladle quickly into jars.', 'Seal.'], 'ingredient_quantities': ['1', '1', '2', '1/4', '1', '1', '5'], 'ingredients': ['orange', 'lemon', 'pears', 'maraschino cherry', 'crushed pineapple', 'sugar'], 'ingredients_cleaned': ['orange', 'lemon', 'pear', 'maraschino cherry', 'pineapple'], 'ingred_and_tags': ['orange', 'lemon', 'pear', 'maraschino cherry', 'pineapple', 'free of...', '< 60 mins'], 'name_cat_ingred_tag': ['Paradise', 'Pear', 'Jam', 'Fruit', 'orange', 'lemon', 'pear', 'maraschino cherry', 'pineapple', 'free of...', '< 60 mins'], 'cat_ingred_tag': ['Fruit', 'orange', 'lemon', 'pear', 'maraschino cherry', 'pineapple', 'free of...', '< 60 mins']}, '245113': {'Name': 'Ambrosia Sweet Potato Bake', 'RecipeCategory': 'Yam/Sweet Potato', 'Calories': 388.8, 'images': ['Not Provided'], 'cook_time': '30 Minute(s) ', 'prep_time': '20 Minute(s) ', 'total_time': '50 Minute(s) ', 'recipe_servings': 8, 'tags': ['potato', 'vegetable', 'low protein', '< 60 mins'], 'instructions': ['Thinly slice 1/2 lemon and 1/2 orange with peels. alternate with 6 or 7 cups of .', 'Cooked sweet potatoes in a 11 1/2 x 7 1/2 x 1 1/2 buttered casserol dish.', 'Combine crushed pineapple.', 'Brown sugar.', 'Melted butter and salt. pour over all sweet potatoes.', 'Sprinkle with 1/2 cup shredded coconut. trim with maraschino cherries.', 'Bake in a moderate oven for about 30 minutes.'], 'ingredient_quantities': ['na', 'na', '6 -7', '9', '1/2', '1/2', '1/2', '1/2', 'na'], 'ingredients': ['lemon', 'orange', 'crushed pineapple', 'brown sugar', 'butter', 'salt', 'maraschino cherry'], 'ingredients_cleaned': ['lemon', 'orange', 'pineapple', 'maraschino cherry'], 'ingred_and_tags': ['lemon', 'orange', 'pineapple', 'maraschino cherry', 'potato', 'vegetable', 'low protein', '< 60 mins'], 'name_cat_ingred_tag': ['Ambrosia', 'Sweet', 'Potato', 'Bake', 'Yam/Sweet', 'Potato', 'lemon', 'orange', 'pineapple', 'maraschino cherry', 'potato', 'vegetable', 'low protein', '< 60 mins'], 'cat_ingred_tag': ['Yam/Sweet', 'Potato', 'lemon', 'orange', 'pineapple', 'maraschino cherry', 'potato', 'vegetable', 'low protein', '< 60 mins']}, '439658': {'Name': 'Cabbage and Corned Beef in Coconut Cream (Kapisi Pula)', 'RecipeCategory': 'Meat', 'Calories': 190.1, 'images': ['https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/45/59/15/piczwpmir.jpg', 'https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/45/59/15/picbxmifg.jpg'], 'cook_time': '1 Hour(s) 30 Minute(s) ', 'prep_time': '20 Minute(s) ', 'total_time': '1 Hour(s) 50 Minute(s) ', 'recipe_servings': 8, 'tags': ['polynesian', '< 4 hours'], 'instructions': ['Place cabbages leaves on foil to make a cup shape. (it would help to put all these in a round cake tin.).', 'Into the cup-shaped cabbage leaves.', 'Put the corned beef.', 'Onion.', 'Tomato.', 'Some shredded cabbage and coconut cream.', 'Wrap the foil around and bake at 350* for 1 -1 1/2 hours.', 'Serve hot.'], 'ingredient_quantities': ['8', '1', '1', '1', '1', '8'], 'ingredients': ['cabbage leaves', 'cabbage', 'corned beef', 'onion', 'tomatoes', 'coconut cream'], 'ingredients_cleaned': ['cabbage leaf', 'cabbage', 'beef', 'tomato', 'coconut cream'], 'ingred_and_tags': ['cabbage leaf', 'cabbage', 'beef', 'tomato', 'coconut cream', 'polynesian', '< 4 hours'], 'name_cat_ingred_tag': ['Cabbage', 'and', 'Corned', 'Beef', 'in', 'Coconut', 'Cream', '(Kapisi', 'Pula)', 'Meat', 'cabbage leaf', 'cabbage', 'beef', 'tomato', 'coconut cream', 'polynesian', '< 4 hours'], 'cat_ingred_tag': ['Meat', 'cabbage leaf', 'cabbage', 'beef', 'tomato', 'coconut cream', 'polynesian', '< 4 hours']}, '250579': {'Name': 'Ambrosia Sweet Potatoes', 'RecipeCategory': 'Yam/Sweet Potato', 'Calories': 318.7, 'images': ['https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/26/07/38/picmsqxxo.jpg', 'https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/26/07/38/pico0luoo.jpg'], 'cook_time': '30 Minute(s) ', 'prep_time': '10 Minute(s) ', 'total_time': '40 Minute(s) ', 'recipe_servings': 8, 'tags': ['potato', 'vegetable', 'low protein', '< 60 mins'], 'instructions': ['Place sweet potatoes in a baking dish. slice orange and lemon into thin slices.', 'Alternate layering slices on top of sweet potatoes.', 'Combine drained pineapple.', 'Brown sugar and melted butter. pour mixture over sweet potatoes. sprinkle with shredded coconut.', 'Decorate with cherries. bake in a 350°f oven for 30 minutes.'], 'ingredient_quantities': ['6', '1/2', '1/2', '1', '3/4', '1/2', '1/2', 'na'], 'ingredients': ['sweet potatoes', 'orange', 'lemon', 'crushed pineapple', 'brown sugar', 'butter', 'maraschino cherry'], 'ingredients_cleaned': ['sweet potato', 'orange', 'lemon', 'pineapple', 'maraschino cherry'], 'ingred_and_tags': ['sweet potato', 'orange', 'lemon', 'pineapple', 'maraschino cherry', 'potato', 'vegetable', 'low protein', '< 60 mins'], 'name_cat_ingred_tag': ['Ambrosia', 'Sweet', 'Potatoes', 'Yam/Sweet', 'Potato', 'sweet potato', 'orange', 'lemon', 'pineapple', 'maraschino cherry', 'potato', 'vegetable', 'low protein', '< 60 mins'], 'cat_ingred_tag': ['Yam/Sweet', 'Potato', 'sweet potato', 'orange', 'lemon', 'pineapple', 'maraschino cherry', 'potato', 'vegetable', 'low protein', '< 60 mins']}}}

################### NLP MODEL FUNCTIONS ####################

# call and get response for recipes
# response_recipes = requests.get(url + "/suggest_recipes", params=parameters).json()

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

get_recipes_expand(response_recipes)

st.markdown("----")
columns = st.columns(3)
about_us = columns[0].button(" About Us ")
if about_us:
    switch_page("about")
st.markdown("----")
