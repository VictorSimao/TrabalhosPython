from flask import Flask, render_template, request, redirect

import sys
sys.path.append('C:/Users/Familia Nande Simão/Documents/GitHub/TrabalhosPython/Aula36')
from Controller.pessoa_controller import PessoaController
from Controller.endereco_controller import EnderecoController

app = Flask(__name__)
pessoa_controller = PessoaController()
end_controller = EnderecoController()
nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    pessoas = pessoa_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = pessoas)

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
    id_end = request.args['id_end']
    pessoa_controller.deletar(id)
    if id_end != 'None':
        end_controller.deletar(id_end)
    return redirect('/listar')
app.run(debug=True)