from dao.frontend_dao import FrontEndDao
from model.frontend import FrontEnd

class FrontEndController:
    dao = FrontEndDao()

    def listar_todos(self):
        lista_fronts = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            p1 = FrontEnd()
            p1.id = p[0]
            p1.nome = p[1]
            p1.versao = p[2]
            lista_fronts.append(p1)
        return lista_fronts

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        p1 = FrontEnd()
        p1.id = p[0]
        p1.nome = p[1]
        p1.versao = p[2]
        return p1

    def salvar(self, frontend:FrontEnd):
        return self.dao.salvar(frontend)

    def alterar(self, frontend:FrontEnd):
        self.dao.alterar(frontend)

    def deletar(self, id):
        self.dao.deletar(id)