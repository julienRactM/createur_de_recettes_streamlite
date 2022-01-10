import streamlit as st
from PIL import Image
#import datetime

import requests

'''
# Createur de recette Model front

This front queries the Createur de recette [createur de recette API](https://tblablabla.fr)

'''

img=Image.open("le_wagon.png")
st.set_page_config(page_title="Demo Day",page_icon=img)
#pickup_date = st.date_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
# pickup_time = st.time_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
# pickup_datetime = f'{pickup_date} {pickup_time}'
# pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
# pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
input_text = st.text_input('input text', value="carottes, boeuf, oignons")
#button = st.button('Run')
output_text = st.write('output text')

# enter here the address of your flask api
url = 'https://taxifare.lewagon.ai/predict'

params = dict(input_text=input_text,
              )

#response = requests.get(url, params=params)

#prediction = response.json()

#pred = prediction['prediction']
pred= "This is the predicted recipe using : " + input_text

if st.button("Run"):
    st.write(pred)
else:
    st.write("hello")
