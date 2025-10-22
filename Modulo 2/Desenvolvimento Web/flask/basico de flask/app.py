

### IMPORTANDO "PARTES" DO FLASK

from flask import Flask, render_template,request

### Criando o app e dizendo que ele está nesse arquivo com nome dele
app = Flask(__name__)



### Criando Rotas

## / significa principal onde o site já vai de cara 

@app.route('/')
def ola_mundo():
    return "Olá mundo, Gustavo programando!"


### Aqui vamos criar uma nova rota, dessa vez vai ser a /contato

@app.route('/contato')
def contato():
    return render_template('Contato.html')


### Sua vez crie uma nova rota dessa vez /hobbies, lá coloque algo que você goste de fazer, exemplo : Jogar bola

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')


### lembre-se de criar um template chamado hobbies.html

### Executando o arquivo
if __name__ == '__main__':
    app.run(debug=True)