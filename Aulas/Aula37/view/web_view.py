from flask import Flask, render_template, request, redirect

import sys
sys.path.append('C:/Users/900165/Documents/TrabalhosPython/Aulas/Aula37')
from controller.squad_controller import SquadController
from model.squad import Squad

app = Flask(__name__)
squad_controller = SquadController()
nome = 'Cadastros Squad'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squads = squad_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = squads)

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()
    if 'idsquad' in request.args:
        id = request.args['idsquad']
        squad = squad_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, squad = squad )

@app.route('/salvar')
def salvar():
    squad = Squad()
    squad.idsquad = int(request.args['idsquad'])
    squad.nome = request.args['nome']
    squad.descricao = request.args['descricao']
    squad.numeropessoas = request.args['numeropessoas']
    squad.linguagembackend = request.args['linguagembackend']
    squad.frameworkfrontend = request.args['frameworkfrontend']

    print(squad.idsquad)
    if squad.idsquad == 0:
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)
    return redirect('/listar')

@app.route('/excluir')
def excluir():
    id = int(request.args['idsquad'])
    squad_controller.deletar(id)
    return redirect('/listar')

app.run()