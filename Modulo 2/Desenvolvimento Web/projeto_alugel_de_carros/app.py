# import streamlit as st

# st.title("Olá mundo, meu nome é gustavo")
# # escreve um titulo

# date = st.date_input("Selecione uma Data")
# #Criando um calendário

# file = st.file_uploader("Pick a file")
# #Permitindo o upload


#  python -m streamlit run app.py
#  python -m streamlit run app.py

#==============================================

import streamlit as st
import pandas as pd

cidades = ['Nagoya', 'Xinxi', 'Tokyo']

#Barra lateral
opcao = st.sidebar.selectbox('Escolha uma cidade do Japão', cidades)

data = {'latitude': [35.6895, 34.6937, 39.701],
        'longitude': [139.6917, 135.5023, 141.673]}

df = pd.DataFrame(data)

### TITULO SO SITE
st.title("Mapa do Japão")

### CRIANDO UM MAPA/CRIA UM MAPA 
st.map(df)