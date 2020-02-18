from flask import Flask
from flask_restful import Api

from Aulas.Aula58.controller.base_controller import BaseController

app = Flask(__name__)
api = Api(app)

api.add_resource(BaseController, '/api/pessoa', endpoint='pessoas')
api.add_resource(BaseController, '/api/pessoa/<int:id>', endpoint='pessoa')

app.run(debug=True)