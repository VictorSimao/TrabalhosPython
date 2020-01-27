from dao.sgbd_dao import SgbdDao
from model.sgbd import Sgbd

class SgbdController:
    dao = SgbdDao()

    def listar_todos(self):
        lista_sgbds = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            p1 = Sgbd()
            p1.id = p[0]
            p1.nome = p[1]
            p1.versao = p[2]
            lista_sgbds.append(p1)
        return lista_sgbds

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        p1 = Sgbd()
        p1.id = p[0]
        p1.nome = p[1]
        p1.versao = p[2]
        return p1

    def salvar(self, sgbd:Sgbd):
        return self.dao.salvar(sgbd)

    def alterar(self, sgbd:Sgbd):
        self.dao.alterar(sgbd)

    def deletar(self, id):
        self.dao.deletar(id)