from flask import Flask, render_template, request, redirect

import sys
sys.path.append('Aulas/Aula38')

from controller.squad_controller import SquadController
from controller.backend_controller import BackEndController
from controller.frontend_controller import FrontEndController
from controller.sgbd_controller import SgbdController

from model.squad import Squad
from model.backend import BackEnd
from model.frontend import FrontEnd
from model.sgbd import Sgbd

app = Flask(__name__)
squad_controller = SquadController()
backend_controller = BackEndController()
frontend_controller = FrontEndController()
sgbd_controller = SgbdController()
nome = 'Cadastros Squad'

@app.route('/')
def inicio():
    return render_template('homepage.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squads = squad_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = squads)


@app.route('/cadastrar')
def cadastrar():
    squad = Squad()
    if 'id' in request.args:
        id = request.args['id']
        squad = squad_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, squad = squad )

@app.route('/salvar')
def salvar():
    squad = Squad()
    squad.id = int(request.args['id'])
    squad.nome = request.args['nome']
    squad.descricao = request.args['descricao']
    squad.numpessoas = request.args['numpessoas']
    # squad.backend = request.args['backend']
    # squad.frontend = request.args['frontend']
    

    if squad.id == 0:
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)
    return redirect('/listar')

@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    squad_controller.deletar(id)
    return redirect('/listar')

@app.route('/listarback')
def listarback():
    backs = backend_controller.listar_todos()
    return render_template('listarback.html', titulo_app = nome, lista = backs)

@app.route('/cadastrarback')
def cadastrarback():
    backend = BackEnd()
    if 'id' in request.args:
        id = request.args['id']
        backend = backend_controller.buscar_por_id(id)
    return render_template('cadastrarback.html', titulo_app = nome, back = backend )

@app.route('/salvarback')
def salvarback():
    backend = BackEnd()
    backend.id = int(request.args['id'])
    backend.nome = request.args['nome']
    backend.versao = request.args['versao']
    
    if backend.id == 0:
        backend_controller.salvar(backend)
    else:
        backend_controller.alterar(backend)
    return redirect('/listarback')

@app.route('/excluirback')
def excluirback():
    id = int(request.args['id'])
    backend_controller.deletar(id)
    return redirect('/listarback')

@app.route('/listarfront')
def listarfront():
    fronts = frontend_controller.listar_todos()
    return render_template('listarfront.html', titulo_app = nome, lista = fronts)

@app.route('/cadastrarfront')
def cadastrarfront():
    frontend = FrontEnd()
    if 'id' in request.args:
        id = request.args['id']
        frontend = frontend_controller.buscar_por_id(id)
    return render_template('cadastrarfront.html', titulo_app = nome, front = frontend )

@app.route('/salvarfront')
def salvarfront():
    frontend = FrontEnd()
    frontend.id = int(request.args['id'])
    frontend.nome = request.args['nome']
    frontend.versao = request.args['versao']
    
    if frontend.id == 0:
        frontend_controller.salvar(frontend)
    else:
        frontend_controller.alterar(frontend)
    return redirect('/listarfront')

@app.route('/excluirfront')
def excluirfront():
    id = int(request.args['id'])
    frontend_controller.deletar(id)
    return redirect('/listarfront')

@app.route('/listarsgbds')
def listarsgbd():
    sgbds = sgbd_controller.listar_todos()
    return render_template('listarsgbd.html', titulo_app = nome, lista = sgbds)

@app.route('/cadastrarsgbd')
def cadastrarsgbd():
    sgbd = Sgbd()
    if 'id' in request.args:
        id = request.args['id']
        sgbd = sgbd_controller.buscar_por_id(id)
    return render_template('cadastrarsgbd.html', titulo_app = nome, sgbd = sgbd )

@app.route('/salvarsgbd')
def salvarsgbd():
    sgbd = Sgbd()
    sgbd.id = int(request.args['id'])
    sgbd.nome = request.args['nome']
    sgbd.versao = request.args['versao']
    
    if sgbd.id == 0:
        sgbd_controller.salvar(sgbd)
    else:
        sgbd_controller.alterar(sgbd)
    return redirect('/listarsgbds')

@app.route('/excluirsgbd')
def excluirsgbd():
    id = int(request.args['id'])
    sgbd_controller.deletar(id)
    return redirect('/listarsgbds')

app.run(debug=True)