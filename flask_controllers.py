from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_url_path='/static')


class Programa:
    def __init__(self, nome, descricao, produtora):
        self.nome = nome
        self.descricao = descricao
        self.produtora = produtora


class Administrador:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

#  CRIANDO PROGRAMAS
vingadores_guerra_infinita = Programa('Vingadores',
                                      'Homem de Ferro, Thor, Hulk e os Vingadores se unem para combater seu inimigo mais poderoso, o maligno Thanos. Em uma missão para coletar todas as seis pedras infinitas, Thanos planeja usá-las para infligir sua vontade maléfica sobre a realidade.',
                                      'Marvel Studius')
logan = Programa('Logan',
                 'Em 2024, os mutantes estão em franco declínio, e as pessoas não sabem o real motivo. Uma organização está transformando as crianças mutantes em verdadeiras assassinas. Wolverine, cansado de tudo e a pedido de um cada vez mais enfraquecido Professor Xavier, precisa proteger a jovem e poderosa Laura.',
                 'Fox')

programas = [vingadores_guerra_infinita, logan]



@app.route('/')
def index():
    return render_template('index.html', titulo='LocaGeek - Home', programas=programas)


@app.route('/login')
def login():
    return render_template('login.html', titulo='LocaGeek - Login')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo='LocaGeek - Cadastro', programas=programas)


@app.route('/criar-produto', methods=["POST", ])
def criar_programa():

    nomeCad = request.form['nomeCad']
    descricaoCad = request.form['descricaoCad']
    produtoraCad = request.form['produtoraCad']

    programa = Programa(nomeCad, descricaoCad, produtoraCad)

    programas.append(programa)
    return render_template('cadastro.html', titulo='LocaGeek - Cadastro', programas=programas)


@app.route('/verificar-login', methods=['POST'])
def verificar_login():
    #  CRIANDO ADMINISTRADOR
    adm = Administrador('lucassimoessilva@hotmail.com', '123')
    usuarios = [adm]

    email = request.form['email_usuario']
    senha = request.form['password']

    for admin in usuarios:
        if admin.email == email and admin.senha == senha:
            return redirect('/cadastro')
        else:
            return render_template('login.html', titulo='LocaGeek - login')



app.run(debug=True)
