import streamlit as st
from PIL import Image
import requests


url = "https://createur-de-recette-vikteoeica-ew.a.run.app/predict"
'''
# Projet Createur de recette



'''
#above in ''' ''' Createur de recette [createur de recette API](https://tblablabla.fr)
COLOR = "#2F4F4F"
BACKGROUND_COLOR = "#D3D3D3"
# fonts Lucida Calligraphy cursive Brush Script MT
FONTFAMILY = "Lucida Calligraphy"
#img = Image.open("le_wagon.png")
#st.image(img, caption=None,width=150)
st.image('./le_wagon.png',width=150)


input_text = st.text_input(
    'input text',
    value="carottes, boeuf, oignons, 2 cuillères de sel, 4 patates")

# pred= "Voici la recette prédite par le model : " + input_text


if st.button("Exécuter"):
    while True:
        ingredients = "🥕\n\n" + '\n'.join(
            [ingredient.strip()
            for ingredient in input_text.split(',')]) + "\n\n📝\n\n"


        # params = dict(input_text=ingredients)
        params = {
            'ingredients': ingredients  # string
        }
        # pred = ingredients
        response = requests.get(url, params=params) #.content.json())
        if response.status_code == 200:
            st.text(response.json()['response'])
            # st.write(response.json()['response'])
            # st.write(response.content)
            break
        else :
            st.write("Nous avons rencontrer une erreur")
            st.write(response.status_code)

else:
    st.write("En attente d'ingrédients")


st.markdown(
    f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
    }}
    .reportview-container .main {{
        background-color: {BACKGROUND_COLOR};
    }}
    .css-183lzff {{
        width: 90%;
        word-break: break-all;
        word-wrap: break-word;
         font-size:18px;
         font-weight:500;
         font-family:{FONTFAMILY};
    }}
</style>
""",
    unsafe_allow_html=True,
)



# above in st.markdown :color: {COLOR}; overflow-x: hidden; text-overflow: ellipsis; word-wrap: break-word;




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
# Add a placeholder


# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     # Update the progress bar with each iteration.
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)



if __name__ == "__main__":
    pass
