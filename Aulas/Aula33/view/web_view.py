from flask import Flask, render_template
import sys
sys.path.append('C:/Users/900165/Documents/TrabalhosPython/Aulas/Aula33')
from controller.pessoa_controller import PessoaController
from controller.endereco_controller import EnderecoController

app = Flask(__name__)
pc = PessoaController()
ec = EnderecoController()

@app.route('/')
def inicio():
    enderecos = ec.listar_todos()
    pessoas = pc.listar_todos()
    return render_template('index.html', lista_pessoas = pessoas, lista_enderecos = enderecos)

app.run()