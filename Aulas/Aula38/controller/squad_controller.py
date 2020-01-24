from dao.squad_dao import SquadDao
from dao.backend_dao import BackEndDao
from dao.frontend_dao import FrontEndDao
from dao.sgbd_dao import SgbdDao

from model.squad import Squad
from model.backend import BackEnd
from model.frontend import FrontEnd
from model.sgbd import Sgbd

from controller.backend_controller import BackEndController
from controller.frontend_controller import FrontEndController
from controller.sgbd_controller import SgbdController

class SquadController:

    def __init__(self):
        self.squad_dao = SquadDao()
        self.backend_dao = BackEndDao()
        self.backend_controller = BackEndController()
        self.frontend_controller = FrontEndController()
        self.sgbd_controller = SgbdController()

    def listar_todos(self):
        lista_squads = []
        lista_tuplas_squads = self.squad_dao.listar_todos()
        for s in lista_tuplas_squads:
            s1 = Squad()
            s1.id = s[0]
            s1.nome = s[1]
            s1.descricao= s[2]
            s1.numeropessoas = s[3]
            lista_tuplas_backend = self.backend_dao.listar_todos(s1.id)
            i=0
            for b in range(len(lista_tuplas_backend)):
                s1.backend.append(b[i])
                i+=1
            lista_tuplas_frontend = self.frontend_dao.listar_todos(s1.id)
            i=0
            for f in range(len(lista_tuplas_frontend)):
                s1.frontend.append(b[i])
                i+=1
            lista_tuplas_sgbd = self.sgbd_dao.listar_todos(s1.id)
            i=0
            for sg in range(len(lista_tuplas_sgbd)):
                s1.sgbd.append(sg[1])
                i+=1
            lista_squads.append(s1)
        return lista_squads

    def buscar_por_id(self, id):
        s = self.squad_dao.buscar_por_id(id)
        s1 = Squad()
        s1.id = s[0]
        s1.nome = s[1]
        s1.descricao= s[2]
        s1.numeropessoas = s[3]
        lista_tuplas_backend = self.backend_dao.listar_todos(s1.id)
        i=0
        for b in range(len(lista_tuplas_backend)):
            s1.backend.append(b[i])
            i+=1
        lista_tuplas_frontend = self.frontend_dao.listar_todos(s1.id)
        i=0
        for f in range(len(lista_tuplas_frontend)):
            s1.frontend.append(b[i])
            i+=1
        lista_tuplas_sgbd = self.sgbd_dao.listar_todos(s1.id)
        i=0
        for sg in range(len(lista_tuplas_sgbd)):
            s1.sgbd.append(sg[1])
            i+=1
        return s1


    def salvar(self, squad:Squad):
        # squad.backend.id = self.backend_controller.salvar(squad)
        # squad.frontend.id = self.frontend_controller.salvar(squad)
        # squad.sgbd.id = self.sgbd_controller.salvar(salvar)
        return self.squad_dao.salvar(squad)

    def alterar(self, squad:Squad):
        # self.backend_controller.alterar(squad)
        # self.frontend_controller.alterar(squad)
        # self.sgbd_controller.alterar(squad)
        self.squad_dao.alterar(squad)

    def deletar(self, id):
        self.squad_dao.deletar(id)