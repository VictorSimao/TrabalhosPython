from flask import Flask
from flask_restful import Api

from Aulas.Aula55.controller.autor_controller import AutorController

app = Flask(__name__)
api = Api(app)

api.add_resource(AutorController, '/api/autor', endpoint='autores')
api.add_resource(AutorController, '/api/autor/<int:id>', endpoint='autor')

app.run(debug=True)