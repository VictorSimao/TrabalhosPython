
class BackEnd:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.versao = ''

    def __str__(self):
        return f'{self.id};{self.nome};{self.versao}'