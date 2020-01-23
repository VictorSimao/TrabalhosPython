from dao.frontend_dao import FrontEndDao
from model.frontend import FrontEnd

class FrontEndController:
    dao = FrontEndDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, frontend:FrontEnd):
        return self.dao.salvar(frontend)

    def alterar(self, frontend:FrontEnd):
        self.dao.alterar(frontend)

    def deletar(self, id):
        self.dao.deletar(id)