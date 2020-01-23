from dao.squad_dao import SquadDao
from model.squad import Squad
from model.backend import BackEnd
from model.frontend import FrontEnd
from model.sgbd import Sgbd
from controller.backend_controller import BackEndController
from controller.frontend_controller import FrontEndController
from controller.sgbd_controller import SgbdController

class SquadController:

    dao = SquadDao()
    backend_controller = BackEndController()
    frontend_controller = FrontEndController()
    sgbd_controller = SgbdController()

    def listar_todos(self):
        lista_squads = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            s1 = Squad()
            s1.id = s[0]
            s1.nome = s[1]
            s1.descricao= s[2]
            s1.numeropessoas = s[3]
            s1.backend = BackEnd()
            s1.backend.id = s[4]
            s1.backend.nome = s[5]
            s1.backend.versao = s[6]
            # s1.frontend = FrontEnd()
            # s1.frontend.id = s[7]
            # s1.frontend.nome = s[8]
            # s1.frontend.versao = s[9]
            # s1.sgbd = Sgbd()
            # s1.sgbd.id = s[10]
            # s1.sgbd.nome = s[11]
            lista_squads.append(s1)
        return lista_squads

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        s1 = Squad()
        s1.id = s[0]
        s1.nome = s[1]
        s1.descricao= s[2]
        s1.numeropessoas = s[3]
        s1.backend.id = s[4]
        s1.backend.nome = s[5]
        s1.frontend.id = s[7]
        s1.frontend.nome = s[8]
        s1.sgbd.id = s[10]
        s1.sgbd.nome = s[11]
        return s1


    def salvar(self, squad:Squad):
        squad.backend.id = self.backend_controller.salvar(squad)
        squad.frontend.id = self.frontend_controller.salvar(squad)
        squad.sgbd.id = self.sgbd_controller.salvar(salvar)
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        self.backend_controller.alterar(squad)
        self.frontend_controller.alterar(squad)
        self.sgbd_controller.alterar(squad)
        self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)