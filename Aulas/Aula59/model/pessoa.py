
class Pessoa():
    def __init__(self, nome, sobrenome, id=None):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            }