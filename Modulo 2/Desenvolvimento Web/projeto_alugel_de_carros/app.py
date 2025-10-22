# import streamlit as st

# st.title("Olá mundo, meu nome é gustavo")
# # escreve um titulo

# date = st.date_input("Selecione uma Data")
# #Criando um calendário

# file = st.file_uploader("Pick a file")
# #Permitindo o upload


#  python -m streamlit run app.py
#  python -m streamlit run app.py

import streamlit as st
import pandas as pd


# ------------------------------------------------- Sidebar

st.sidebar.image("Logo.png")
#Informa uma imagem
st.sidebar.title("Gustavo aluga - Alugando uma viagem mais segura")
#icoloca um título para a sidebar
carros = ['Corsa', 'Gol','Toro', 'Porsche', 'Fiat Uno']
#Informa as opções de carros
opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)
#Cria o seletor de carro

# ------------------------------------------------- Principal

st.title('Alugel de Carros') # ou abatedouros
#Título da pagina

st.image(f'{opcao}.png')
#Carro selecionado

st.markdown(f'## Você alugou o modelo: {opcao} foi alugado')
st.markdown('---')
#Informando o carro alugado
dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
#Informando os dias do alugel
km = st.text_input(f'Quantos km você rodou com o {opcao}?')
#Informando os kms percorridos


if opcao == 'Corsa':
    diaria = 200
#Preço do Corsa
elif opcao == 'Gol':
    diaria = 250
#Preço do Gol
elif opcao == 'Toro':
    diaria = 1000
#Preço do Toro
elif opcao == 'Porsche':
    diaria = 500
#Preço do Porsche
elif opcao == 'Fiat Uno':
    diaria = 300
#Preço do Fiat Uno

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')
