from model.backend import BackEnd
from model.frontend import FrontEnd
from model.sgbd import Sgbd

class Squad:

    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao= ''
        self.numeropessoas = 0
        self.backend = BackEnd()
        # self.frontend = FrontEnd()
        # self.sgbd = Sgbd()

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeropessoas};{self.backend}'

