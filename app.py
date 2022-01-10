import streamlit as st
from PIL import Image
import datetime

import requests




'''
# Projet Createur de recette

Createur de recette [createur de recette API](https://tblablabla.fr)

'''

#img = Image.open("le_wagon.png")
#st.image(img, caption=None,width=150)
st.image('./le_wagon.png',width=150)


input_text = st.text_input('input text', value="carottes, boeuf, oignons")
#button = st.button('Run')

# enter here the address of your flask api
url = 'https://taxifare.lewagon.ai/predict'

params = dict(input_text=input_text,
              )

#response = requests.get(url, params=params)

#prediction = response.json()

#pred = prediction['prediction']
#output_text = st.write('Output Text')

pred= "This is the predicted recipe using : " + input_text

if st.button("Run"):
    st.write(pred)
else:
    st.write("hello")
