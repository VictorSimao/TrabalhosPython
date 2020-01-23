from dao.sgbd_dao import SgbdDao
from model.sgbd import Sgbd

class SgbdController:
    dao = SgbdDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, sgbd:Sgbd):
        return self.dao.salvar(sgbd)

    def alterar(self, sgbd:Sgbd):
        self.dao.alterar(sgbd)

    def deletar(self, id):
        self.dao.deletar(id)