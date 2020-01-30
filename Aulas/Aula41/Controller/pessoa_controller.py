from flask_restful import Resource

class PessoaController(Resource):
    def get(self):
        return 'Acessando controladora pelo metodo HTTP GET'

    def put(self):
        return 'Acessando controladora pelo metodo HTTP PUT'

    def delete(self):
        return 'Acessando controladora pelo metodo HTTP DELETE'

    def post(self):
        return 'Acessando controladora pelo metodo HTTP POST'

