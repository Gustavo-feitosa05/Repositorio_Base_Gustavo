import streamlit as st

# python -m streamlit run app.py

# -------------------------------------- sidebar

st.sidebar.image("playlist.png")

generos = ["Rock", "Pop", "MPB", "Sertanejo"]
     
musicas_por_genero = {
    "Rock": ['Elvis Presley', 'The Beatles', 'Queen', 'Nirvana'],
    "Pop": ['Michael Jackson', 'Madonna', 'Beyoncé', 'Justin Bieber'],
    "MPB": ['Caetano Veloso', 'Gilberto Gil', 'Gal Costa', 'Maria Bethânia'],
    "Sertanejo": ['Zezé Di Camargo & Luciano', 'Jorge & Mateus', 'Marília Mendonça', 'Gusttavo Lima']
} 

genero_selecionado = st.sidebar.selectbox("Selecione o gênero musical:", generos)

if genero_selecionado:
    cantor_selecionado = st.sidebar.selectbox(
        "Selecione o cantor:",
        musicas_por_genero[genero_selecionado]
    )

if genero_selecionado and cantor_selecionado:
    st.write(f"**Cantor selecionado:** {cantor_selecionado}")
    st.write(f"**Gênero:** {genero_selecionado}")
    st.image(f"{cantor_selecionado}.png", width=500)

# -------------------------------------- 

if genero_selecionado == 'Rock' and cantor_selecionado == 'Elvis Presley':
    st.markdown("""
    ### 🎸 Elvis Presley  
    Elvis Presley, conhecido como o *Rei do Rock*, foi um dos maiores fenômenos culturais do século XX. Sua mistura de rock, country e blues, unida a um estilo ousado e inovador, conquistou multidões a partir dos anos 1950. Além da voz marcante, Elvis se destacou por suas performances carismáticas, que uniam sensualidade e energia no palco. Sua influência atravessa gerações, e músicas como *Jailhouse Rock* e *Can’t Help Falling in Love* ainda ecoam como símbolos de uma era de transformação na música mundial.
    """)
    st.video('https://youtu.be/ixbcvKCl4Jc?si=XY9BVIaR4wcPVjYT')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Elvis%20Presley')

elif genero_selecionado == 'Rock' and cantor_selecionado == 'The Beatles':
    st.markdown("""
    ### 🎸 The Beatles  
    The Beatles foram mais do que uma banda: se tornaram um fenômeno cultural que mudou a forma de se fazer e consumir música. Formado por John Lennon, Paul McCartney, George Harrison e Ringo Starr, o quarteto britânico conquistou o mundo com melodias cativantes e letras que iam do simples romance às reflexões mais profundas. Durante os anos 1960, inovaram constantemente, misturando estilos e explorando novas sonoridades. Clássicos como *Hey Jude*, *Let It Be* e *Yesterday* continuam marcando gerações, fazendo dos Beatles uma lenda eterna do rock.
    """) 
    st.video('https://youtu.be/NCtzkaL2t_Y?si=cHeMTzLKeTIZ_YpF')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/The%20Beatles')

elif genero_selecionado == 'Rock' and cantor_selecionado == 'Queen':
    st.markdown("""
    ### 🎸 Queen  
    O Queen, liderado pelo icônico Freddie Mercury, é considerado uma das maiores bandas de rock da história. Reconhecido por sua mistura única de estilos musicais, a banda transitou entre o rock clássico, ópera e até elementos de música eletrônica. Canções como *Bohemian Rhapsody*, *We Will Rock You* e *We Are the Champions* se tornaram hinos globais. Freddie Mercury, com sua voz poderosa e presença de palco incomparável, transformou cada show em um espetáculo inesquecível. A banda deixou um legado que continua inspirando fãs e músicos até hoje.
    """)
    st.video('https://youtu.be/fJ9rUzIMcZQ?si=VUlWjYFVG4yStubH')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Queen')

elif genero_selecionado == 'Rock' and cantor_selecionado == 'Nirvana':
    st.markdown("""
    ### 🎸 Nirvana  
    Nirvana surgiu no final dos anos 80 e se tornou símbolo do movimento grunge nos anos 90, revolucionando o cenário musical com sua sonoridade crua e letras intensas. Liderada por Kurt Cobain, a banda expressava sentimentos de angústia e rebeldia que marcaram uma geração. O álbum *Nevermind*, com o hit *Smells Like Teen Spirit*, levou o grunge ao mainstream e transformou o Nirvana em um dos maiores nomes do rock alternativo. Apesar da curta trajetória, o impacto da banda permanece vivo como referência cultural e musical.
    """)
    st.video('https://youtu.be/hTWKbfoikeg?si=0qRGjbPPY2P3gHlU')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Nirvana')


#=====


elif genero_selecionado == 'Pop' and cantor_selecionado == 'Michael Jackson':
    st.markdown("""
    ### 🎤 Michael Jackson  
    Michael Jackson, conhecido como o *Rei do Pop*, é uma das figuras mais icônicas da música mundial. Desde a infância, como integrante do Jackson 5, até sua carreira solo, conquistou recordes e multidões com sua voz única, coreografias inovadoras e videoclipes revolucionários. Álbuns como *Thriller* e *Bad* marcaram a história da música, e seus passos de dança, como o *moonwalk*, se tornaram símbolos culturais. Além da música, Michael deixou um legado de impacto artístico e humanitário, sendo lembrado como um dos maiores artistas de todos os tempos.
    """)
    st.video('https://youtu.be/Zi_XLOBDo_Y?si=I4q2sTmraK_aHgXE')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Michael%20Jackson')

elif genero_selecionado == 'Pop' and cantor_selecionado == 'Madonna':
    st.markdown("""
    ### 🎤 Madonna  
    Madonna é amplamente reconhecida como a *Rainha do Pop* por sua habilidade de se reinventar constantemente e por influenciar não só a música, mas também a moda e o comportamento. Sua carreira é marcada por ousadia, inovação e polêmicas que desafiaram padrões sociais e culturais. Com sucessos como *Like a Virgin*, *Vogue* e *Hung Up*, ela conquistou fãs ao redor do mundo e se tornou sinônimo de liberdade criativa. Madonna é um exemplo de longevidade no cenário musical e continua sendo referência para novas gerações de artistas.
    """)
    st.video('https://youtu.be/zpzdgmqIHOQ?si=mR0ClK4ZS2mKSTlg')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Madonna')

elif genero_selecionado == 'Pop' and cantor_selecionado == 'Beyoncé':
    st.markdown("""
    ### 🎤 Beyoncé  
    Beyoncé é uma das artistas mais poderosas e admiradas da atualidade, destacando-se por sua voz marcante, presença de palco inigualável e músicas que transmitem mensagens de empoderamento. Iniciou a carreira no grupo Destiny’s Child, mas brilhou ainda mais em sua trajetória solo, com álbuns aclamados como *Lemonade* e *Renaissance*. Além do talento musical, Beyoncé é conhecida por suas produções visuais inovadoras e pelo ativismo em prol da igualdade racial e dos direitos das mulheres, consolidando-se como um ícone da cultura pop contemporânea.
    """)
    st.video('https://youtu.be/VBmMU_iwe6U?si=KnIq15mIQ7f57JQ8')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Beyonc%C3%A9')

elif genero_selecionado == 'Pop' and cantor_selecionado == 'Justin Bieber':
    st.markdown("""
    ### 🎤 Justin Bieber  
    Justin Bieber iniciou sua carreira de forma inusitada, ao ser descoberto no YouTube ainda adolescente. Seu talento rapidamente o levou ao estrelato, tornando-se um dos artistas pop mais influentes da sua geração. Ao longo da carreira, amadureceu musicalmente, explorando estilos que vão do pop ao R&B. Sucessos como *Baby*, *Sorry* e *Peaches* o colocaram no topo das paradas mundiais. Apesar das polêmicas da juventude, Bieber se consolidou como um cantor versátil e resiliente, com milhões de fãs fiéis ao redor do planeta.
    """)
    st.video('https://youtu.be/kffacxfA7G4?si=y4jSzL76dkS1S4Pf')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Justin%20Bieber')


#=====


elif genero_selecionado == 'MPB' and cantor_selecionado == 'Caetano Veloso':
    st.markdown("""
    ### 🎶 Caetano Veloso  
    Caetano Veloso é um dos maiores ícones da Música Popular Brasileira, tendo papel fundamental no movimento da Tropicália, que uniu tradição e modernidade na década de 1960. Suas composições transitam entre poesia, crítica social e melodias envolventes, explorando diversos estilos musicais. Canções como *Sampa* e *Sozinho* marcaram sua carreira, assim como sua postura de inovação constante. Caetano é admirado por sua capacidade de dialogar com diferentes gerações e de manter-se relevante ao longo de décadas, sendo considerado um verdadeiro poeta da música.
    """)
    st.video('https://youtu.be/j9UbE1slI-Q?si=OZySzS1tCrdr_ixf')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Caetano%20Veloso')

elif genero_selecionado == 'MPB' and cantor_selecionado == 'Gilberto Gil':
    st.markdown("""
    ### 🎶 Gilberto Gil  
    Gilberto Gil é uma das vozes mais importantes do Brasil, tanto na música quanto na política. Seu estilo mistura elementos do samba, baião, reggae e MPB, resultando em um som único e universal. Participou do movimento tropicalista ao lado de Caetano Veloso e conquistou reconhecimento internacional com sua musicalidade. Entre suas canções mais marcantes estão *Aquele Abraço* e *Andar com Fé*. Além da carreira artística, Gil também foi Ministro da Cultura, reforçando sua importância como figura influente na sociedade brasileira.
    """) 
    st.video('https://youtu.be/JC63-PQ-O1w?si=O3NGN_ZzPZN9RS45')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Gilberto%20Gil')

elif genero_selecionado == 'MPB' and cantor_selecionado == 'Gal Costa':
    st.markdown("""
    ### 🎶 Gal Costa  
    Gal Costa foi uma das maiores intérpretes da MPB, dona de uma voz versátil e envolvente. Sua carreira começou no movimento da Tropicália, ao lado de Caetano e Gil, e se consolidou com sucessos que marcaram época, como *Baby* e *Meu Nome é Gal*. Gal transitou entre o experimental e o popular, sempre surpreendendo o público com sua interpretação intensa. Ao longo da vida, construiu um legado artístico que a colocou entre as maiores vozes femininas do Brasil.
    """)
    st.video('https://youtu.be/rtHTSta0xh8?si=SmUwDTD9FisNAC9j')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Gal%20Costa')

elif genero_selecionado == 'MPB' and cantor_selecionado == 'Maria Bethânia':
    st.markdown("""
    ### 🎶 Maria Bethânia  
    Maria Bethânia é uma das artistas mais respeitadas da música brasileira, conhecida por sua interpretação profunda e pela maneira única de transformar letras em verdadeiras poesias cantadas. Com uma carreira marcada por sucessos como *Grito de Alerta* e *Negue*, ela construiu um repertório de enorme riqueza cultural. Irmã de Caetano Veloso, Bethânia também se destacou por suas apresentações emocionantes, onde une música, literatura e teatro. Sua voz e presença de palco fazem dela uma das maiores representantes da MPB.
    """)
    st.video('https://youtu.be/YPO1iaetL2I?si=7tV-zPmwtV3y99dc')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Maria%20Beth%C3%A2nia')


#=====


elif genero_selecionado == 'Sertanejo' and cantor_selecionado == 'Zezé Di Camargo & Luciano':
    st.markdown("""
    ### 🎵 Zezé Di Camargo & Luciano  
    A dupla Zezé Di Camargo & Luciano se tornou um dos maiores nomes do sertanejo romântico nos anos 1990. Ganhou notoriedade com a música *É o Amor*, que rapidamente conquistou o Brasil e se tornou um clássico do gênero. Ao longo da carreira, emplacaram dezenas de sucessos e construíram uma legião de fãs. A trajetória da dupla também foi retratada no filme *2 Filhos de Francisco*, que emocionou o público ao contar a história de superação até a fama.
    """)
    st.video('https://youtu.be/jqJpikFKO5w?si=Zv4hrZ0bxfeT8SxP')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Zez%C3%A9%20Di%20Camargo%20%26%20Luciano')

elif genero_selecionado == 'Sertanejo' and cantor_selecionado == 'Jorge & Mateus':
    st.markdown("""
    ### 🎵 Jorge & Mateus  
    Jorge & Mateus representam a força do sertanejo universitário, conquistando multidões com músicas que misturam romantismo e alegria. Conhecidos por sucessos como *Amo Noite e Dia* e *Sosseguei*, se consolidaram como uma das duplas mais populares da atualidade. Seus shows lotam estádios e festas pelo Brasil, com uma energia contagiante que conecta o público em cada apresentação.
    """)
    st.video('https://youtu.be/KJDIA5pLwuo?si=VNQ4oSE0qFVl4sVX')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Jorge%20%26%20Mateus')

elif genero_selecionado == 'Sertanejo' and cantor_selecionado == 'Marília Mendonça':
    st.markdown("""
    ### 🎵 Marília Mendonça  
    Marília Mendonça, conhecida como a *Rainha da Sofrência*, revolucionou o sertanejo feminino com suas músicas que falavam diretamente sobre sentimentos, relacionamentos e a vida real. Sua voz poderosa e suas composições conquistaram milhões de fãs em pouco tempo. Canções como *Infiel* e *Todo Mundo Vai Sofrer* se tornaram hinos do gênero. Mesmo após sua partida precoce, Marília continua sendo lembrada com carinho e respeito como uma das maiores cantoras da música brasileira.
    """)
    st.video('https://youtu.be/lxcpH6kvnmg?si=Lk-ooutTr8nreMNb')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Mar%C3%ADlia%20Mendon%C3%A7a')

elif genero_selecionado == 'Sertanejo' and cantor_selecionado == 'Gusttavo Lima':
    st.markdown("""
    ### 🎵 Gusttavo Lima  
    Gusttavo Lima, apelidado de *Embaixador*, é um dos artistas mais populares do sertanejo atual. Com um repertório que vai de músicas românticas a canções animadas, conquistou o público com sucessos como *Balada Boa* e *Apelido Carinhoso*. Sua carreira é marcada por grandes shows, incluindo eventos de longa duração transmitidos para milhões de pessoas. Gusttavo representa a modernidade do sertanejo e é um dos cantores mais influentes da sua geração.
    """)
    st.video('https://youtu.be/T67WZx7CxY8?si=RKfe9TeYxs9KxBvA')
    st.link_button(label='Spotify', url='https://open.spotify.com/search/Gusttavo%20Lima')