from flask_restful import Resource

from Aulas.Aula41.Dao.pessoa_dao import PessoaDao

class PessoaController(Resource):
    def __init__(self):
        self.dao = PessoaDao()

    def get(self):
        msg = self.dao.list_all()
        return msg

    def put(self):
        msg = self.dao.update('')
        return msg

    def delete(self):
        msg = self.dao.delete(10)
        return msg

    def post(self):
        msg = self.dao.insert('')
        return msg

