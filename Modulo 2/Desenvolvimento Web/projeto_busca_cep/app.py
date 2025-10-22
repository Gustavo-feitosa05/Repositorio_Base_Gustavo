import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd

#python -m streamlit run app.py

##### TÍTULO DA APLICAÇÃO #####

st.title("Busca cep")

##### Lista de Opções #####

opcoes = ["Buscar CEP", "Descobrir CEP"]


##### BARRA LATERAL #####

st.sidebar.title("Busca cep")
st.sidebar.image("logo.png")

st.sidebar.markdown("Aplicação para buscar endereço a partir de CEP e mostrar localização no mapa")
st.sidebar.markdown("")
opcao = st.sidebar.selectbox("Escolha uma opção", opcoes)

##### BOTÃO BUSCAR CEP #####



##### BOTÃO DESCOBRIR CEP #####

if opcao == "Buscar CEP":
    st.header("Buscar Endereço pelo Cep")
    st.image("principal.png")
    cep = st.text_input("Digite o CEP (somente números:)")

    if st.button("Buscar"):
        if len(cep) != 8 or not cep.isdigit():
            st.error("Por favor, insira um CEP válido com 8 dígitos numéricos.")
        else:
            try:
                endereco = BuscarCep.buscar_cep(cep)
                if endereco:
                    st.success("Endereço encontrado:")
                    st.write(f"CEP: {endereco[0]}")
                    st.write(f"Endereço: {endereco[1]}")
                    st.write(f"Bairro: {endereco[2]}")
                    st.write(f"Cidade: {endereco[3]}")
                    st.write(f"Estado: {endereco[4]}")

                    ## Mapas
                    st.title("Localização no Mapa")
                    df = pd.DataFrame({"latitude": [endereco[5]], "longitude": [endereco[6]]})
                    st.map(df, zoom=15)
                else:
                    st.error("CEP não encontrado.")
            except Exception as e:
                st.error(f"Ocorreu um erro ao buscar o CEP: {e}")


elif opcao == "Descobrir CEP":
    st.header("Descobrir CEP pelo Endereço")
    st.image("Descobrir.png")
    endereco_usuario = st.text_input("Digite o endereço (ex: Rua Olga, Barueri, sp):")

    if st.button("Descobrir"):
        if not endereco_usuario.strip():
            st.error("Por favor, insira um endereço válido.")
        else:
            try:
                resultado = BuscarCep.descobrir_cep(endereco_usuario)
                st.success("Link de busca no Google:")
                st.write(resultado)
            except Exception as e:
                st.error(f"Ocorreu um erro ao descobrir o CEP: {e}")