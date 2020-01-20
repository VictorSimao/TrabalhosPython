class Item:
    id = 0
    nome = ''
    arma = 0
    escudo = 0
    armadura = 0

    def __str__(self):
        return f'{self.id};{self.nome};{self.arma};{self.escudo};{self.armadura}'