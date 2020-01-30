from flask import Flask
from flask_restful import Api

from Aulas.Aula41.Controller.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoa')

@app.route('/')
def inicio():
    return 'Bem vindo a API - Teste'

app.run(debug=True, port=80)