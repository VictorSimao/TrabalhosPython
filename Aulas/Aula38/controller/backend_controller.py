from dao.backend_dao import BackEndDao
from model.backend import BackEnd

class BackEndController:
    dao = BackEndDao()

    def listar_todos(self):
        lista_backs = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            p1 = BackEnd()
            p1.id = p[0]
            p1.nome = p[1]
            p1.versao = p[2]
            lista_backs.append(p1)
        return lista_backs

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        p1 = BackEnd()
        p1.id = p[0]
        p1.nome = p[1]
        p1.versao = p[2]
        return p1

    def salvar(self, backend:BackEnd):
        return self.dao.salvar(backend)

    def alterar(self, backend:BackEnd):
        self.dao.alterar(backend)

    def deletar(self, id):
        self.dao.deletar(id)