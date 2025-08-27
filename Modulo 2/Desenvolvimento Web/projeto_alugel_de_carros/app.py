import streamlit as st

st.title("Olá mundo, meu nome é gustavo")
# escreve um titulo

date = st.date_input("Selecione uma Data")
#Criando um calendário

file = st.file_uploader("Pick a file")
#Permitindo o upload



#python -m streamlit rum app.py