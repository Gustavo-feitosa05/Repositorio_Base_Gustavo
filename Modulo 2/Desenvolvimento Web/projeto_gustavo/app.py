import streamlit as st
import pandas as pd
import datetime
# python -m streamlit run app.py

# -------------------------------------- sidebar

st.sidebar.image("Logo.png")
#Informa uma imagem

st.sidebar.title("cake Center")
#icoloca um título para a sidebar

sabores = ['Chocolate', 'Leite', 'Limão', 'Morango', 'Banana']
#Informa as opções de carros

opcao = st.sidebar.selectbox('Selecione um sabor', sabores)
#Cria o seletor de carro


# -------------------------------------- principal

st.title("Cake Center - Adoçando a sua rotina ")

st.title('🎂 Sobre nós')

st.markdown('Somos apaixonados por transformar momentos em doces lembranças. Nossa loja é especializada em bolos artesanais, feitos com ingredientes selecionados e muito carinho. Oferecemos desde os clássicos caseiros até bolos personalizados para aniversários, casamentos e outras comemorações especiais.')
st.markdown('✨ Nosso compromisso é levar sabor, qualidade e aquele gostinho de feito em casa para sua mesa.')


left, middle, right = st.columns(3, border=True)

left.markdown("🍓 Sabores: Nossos bolos são feitos em uma grande variedade de sabores, dos mais tradicionais aos mais criativos. Temos opções de frutas, chocolates, recheios especiais e combinações exclusivas que agradam todos os paladares ")
middle.markdown("✅ Qualidade: Trabalhamos apenas com ingredientes frescos e selecionados, garantindo maciez, sabor e aquele toque caseiro que faz toda a diferença. Cada bolo é preparado com carinho para oferecer a melhor experiência possível. ")
right.markdown("🚚 Entregas :Levamos o bolo até você com todo cuidado e pontualidade. Assim, seu pedido chega fresco, saboroso e pronto para adoçar o seu dia ou deixar sua comemoração ainda mais especial.")

st.markdown("👨‍🍳 Nossa história: Tudo começou de forma despretensiosa, quando o fundador ainda levava bolos feitos em casa para compartilhar com colegas na escola. O sabor conquistou rapidamente amigos, professores e familiares, que passaram a incentivar esse talento. Com o tempo, o que era apenas uma paixão se transformou em um sonho maior: abrir a própria loja de bolos. Hoje, esse sonho é realidade, e cada receita carrega a mesma dedicação e amor que marcaram os primeiros bolos preparados naquela época.")

# -----------------------------------------------

st.title('🎂 Encomende o seu bolo')
#Título da pagina

st.image(f'{opcao}.png')

# dias = st.text_input(f'Para que dia você quer o bolo??')

#dias 
dias = st.date_input("Informe para qual dia você quer o bolo", value=datetime.date.today(),format="DD/MM/YYYY")
data_formatada = dias.strftime("%d/%m/%Y")


#Informando os dias da incomenda
kilo_usuario = st.text_input(f'Quantos kilos vc vai querer?')
#Informando a quantidade de kls


if opcao == 'Leite':
    valor_kilo = 30

elif opcao == 'Chocolate':
    valor_kilo = 60

elif opcao == 'Limão':
    valor_kilo = 50

elif opcao == 'Morango':
    valor_kilo = 60

elif opcao == 'Banana':
    valor_kilo = 30


if st.button('Encomendar'):
    try:
        kilo_usuario = float(kilo_usuario)  # converte para número
        total_kl = kilo_usuario * valor_kilo
        st.success(f'Você encomendou o bolo de {opcao} para o dia {data_formatada} e o total ficou R${total_kl:.2f}')
    except ValueError:
        st.error("Digite um número válido para os quilos do bolo!")


sentiment_mapping = ["1", "2", "3", "4", "5"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"Vc selecionou {sentiment_mapping[selected]} estrelas.")