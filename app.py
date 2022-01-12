import streamlit as st
from PIL import Image
import requests

url = "https://createur-de-recettes-vikteoeica-ew.a.run.app/predict"

'''
# Projet Createur de recette

Createur de recette [createur de recette API](https://tblablabla.fr)

'''

#img = Image.open("le_wagon.png")
#st.image(img, caption=None,width=150)
st.image('./le_wagon.png',width=150)


input_text = st.text_input('input text', value="carottes, boeuf, oignons")
#button = st.button('Run')

#response = requests.get(url, params=params)

#prediction = response.json()

#pred = prediction['prediction']
#output_text = st.write('Output Text')

# model = Trainer()
# pred = model.trucchouette
# pred = "This is the predicted recipe using : " + input_text
# pred_test = Trainer().generate_recipe("🥕\n\n100 g de viande hachée\n200 g de tomates\n2 oignons\n500 g de spaghettis\n1 kg de piment\n\n📝\n")
# pred_test = Trainer().generate_recipe("""🥕

# 100 g de viande hachée
# 200 g de tomates
# 2 oignons
# 500 g de spaghettis
#  1 kg de piment

# 📝

# """)
# pred= "Voici la recette prédite par le model : " + input_text


if st.button("Exécuter"):
    ingredients = "🥕\n\n" + '\n'.join(
        [ingredient.strip()
         for ingredient in input_text.split(',')]) + "\n\n📝\n\n"

    # params = dict(input_text=ingredients)
    params = {
        'ingredients': ingredients  # string
    }
    # pred = ingredients
    response = requests.get(url, params=params).content.json()
    # print(response)
    pred = response['response']

    # st.write(pred)
    st.text_area(pred)
else:
    st.write("hello")

# app avant le massacre :
# import streamlit as st
# from PIL import Image

# from createur_de_recette.trainer import Trainer
# '''
# # Projet Createur de recette

# Createur de recette [createur de recette API](https://tblablabla.fr)

# '''

# #img = Image.open("le_wagon.png")
# #st.image(img, caption=None,width=150)
# st.image('./le_wagon.png', width=150)

# input_text = st.text_input('input text', value="carottes, boeuf, oignons")
# #button = st.button('Run')

# params = dict(input_text=input_text, )

# #response = requests.get(url, params=params)

# #prediction = response.json()

# #pred = prediction['prediction']
# #output_text = st.write('Output Text')

# # model = Trainer()
# # pred = model.trucchouette
# # pred = "This is the predicted recipe using : " + input_text
# # pred_test = Trainer().generate_recipe("🥕\n\n100 g de viande hachée\n200 g de tomates\n2 oignons\n500 g de spaghettis\n1 kg de piment\n\n📝\n")
# # pred_test = Trainer().generate_recipe("""🥕

# # 100 g de viande hachée
# # 200 g de tomates
# # 2 oignons
# # 500 g de spaghettis
# #  1 kg de piment

# # 📝

# # """)
# pred = "This is the predicted recipe using : " + input_text

# if st.button("Run"):
#     st.write(pred)
# else:
#     st.write("hello")
