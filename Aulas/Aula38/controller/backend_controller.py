from dao.backend_dao import BackEndDao
from model.backend import BackEnd

class BackEndController:
    dao = BackEndDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, backend:BackEnd):
        return self.dao.salvar(backend)

    def alterar(self, backend:BackEnd):
        self.dao.alterar(backend)

    def deletar(self, id):
        self.dao.deletar(id)