from dao.squad_dao import SquadDao
from model.squad import Squad

class SquadController:

    dao = SquadDao()

    def listar_todos(self):
        lista_squads = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            p1 = Squad()
            p1.idsquad = p[0]
            p1.nome = p[1]
            p1.descricao= p[2]
            p1.numeropessoas = p[3]
            p1.linguagembackend = p[4]
            p1.frameworkfrontend = p[5]
            lista_squads.append(p1)
        return lista_squads

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        p1 = Squad()
        p1.idsquad = p[0]
        p1.nome = p[1]
        p1.descricao= p[2]
        p1.numeropessoas = p[3]
        p1.linguagembackend = p[4]
        p1.frameworkfrontend = p[5]
        return p1


    def salvar(self, squad:Squad):
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)