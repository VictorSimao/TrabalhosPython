from flask import Flask, render_template, request, redirect

import sys
sys.path.append('C:/Users/900165/Documents/TrabalhosPython/Aulas/Aula37')
from controller.squad_controller import SquadController

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
    return render_template('cadastrar.html', titulo_app = nome)

@app.route('/editar')
def editar():
    id = request.args['id']
    return f'O id selecionado foi {id}'

@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    squad_controller.deletar(id)
    return redirect('/listar')
app.run(debug=True)