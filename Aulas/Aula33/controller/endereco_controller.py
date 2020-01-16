from model.endereco import Endereco
from dao.endereco_db import EnderecoDb

class EnderecoController:
    e = Endereco()
    e_db = EnderecoDb()

    def listar_todos(self):
        return self.e_db.listar_todos()

    def exportar(self):
        lec = self.e_db.listar_todos()
        self.e.exportar_txt(lec)
