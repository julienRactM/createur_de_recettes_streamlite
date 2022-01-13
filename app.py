import streamlit as st
from PIL import Image
import requests
import time
import re

url = "https://createur-de-recette-vikteoeica-ew.a.run.app/predict"





#above in ''' ''' Createur de recette [createur de recette API](https://tblablabla.fr)
# COLOR = "#2F4F4F"
# BACKGROUND_COLOR = "#D3D3D3"
# fonts Lucida Calligraphy cursive Brush Script MT
FONTFAMILY = "Lucida Calligraphy"
#img = Image.open("le_wagon.png")
#st.image(img, caption=None,width=150)


col1, col2, col3 = st.columns([1,6,1])
# button_col1, button_col2, button_col3 = st.columns([1, 6, 1])

with col1:
    st.write(" ")

with col2:
    st.image('./logo_marmIAton_gris.png')

    input_text = st.text_input(
        'Choisissez vos ingrédients : ',
        value=
        "200g de chocolat noir, 150g de beurre, 150g de sucre en poudre, 50g de farine, 3 œufs"
    )
    # possible values carottes, boeuf, oignons, 2 cuillères de sel, 4 patates

    # pred= "Voici la recette prédite par le model : " + input_text

    # st.balloons()
    if st.button("Générer une recette"):
        # with st.spinner('En cours de préparation...'):
        #     time.sleep(100)

        ingredients = "🥕\n\n" + '\n'.join(
            [ingredient.strip()
            for ingredient in input_text.split(',')]) + "\n\n📝\n\n"

        # params = dict(input_text=ingredients)
        params = {
            'ingredients': ingredients  # string
        }
        # pred = ingredients
        while True:
            with st.spinner('En cours de préparation...'):
                response = requests.get(url, params=params)  #.content.json())
                print(response.status_code)
                if response.status_code == 200:
                    # st.success('C\'est prêt !')
                    response_result = re.sub("(\n{1}[0-9])",
                                            r"\n\1",
                                            string=response.json()['response'])
                    response_result = re.sub("\n\n\n",
                                            "\n\n",
                                            string=response_result)
                    st.write(response_result)

                    print(response_result)
                    # st.write(response.json()['response'])
                    # st.write(response.content)
                    break
    else:
        st.write("En attente d'ingrédients")

with col3:
    st.write(" ")




st.markdown(
    f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 96%;
    }}
    .reportview-container .main {{

    }}
    h1{{font-size:30px}}
    p{{
        margin: 0px 0px 0.2rem;
    }}
    .css-183lzff {{

        word-break: break-all;
        word-wrap: break-word;
         font-size:18px;
         font-weight:500;
         font-family:{FONTFAMILY};
    }}
    .block-container{{
        padding: 60px 0;
    }}
    .css-1j15ncu{{
        visibility: hidden;
    }}
    img{{
        align-content: center;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 66%;
    }}

</style>
""",
    unsafe_allow_html=True,
)

# in 183       width: 90%;
# above in main background-color: {BACKGROUND_COLOR};
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
