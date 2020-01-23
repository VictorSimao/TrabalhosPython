
class Squad:

    def __init__(self):
        self.idsquad = 0
        self.nome = ''
        self.descricao= ''
        self.numeropessoas = 0
        self.linguagembackend = BackEnd()
        self.frameworkfrontend = FrontEnd()
        self.sgbd = Sgbd()

    def __str__(self):
        return f'{self.idsquad};{self.nome};{self.descricao};{self.numeropessoas};{self.linguagembackend};{self.frameworkfrontend};{self.sgbd}'