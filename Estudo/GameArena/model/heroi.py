class Heroi:
    nome = ''
    vida = 10
    level = 0
    ataque = 0
    defesa = 0
    arma = 0
    escudo = 0
    armadura = 0

    def __str__(self):
        return f'{self.nome};{self.vida};{self.level};{self.ataque};{self.defesa};{self.arma};{self.escudo};{self.armadura}'