class Inimigo:
    id = 0
    nome = ''
    vida = 10
    ataque = 0
    defesa = 0
    arma = 0
    escudo = 0
    armadura = 0
    
    def __str__(self):
        return f'{self.nome};{self.vida};{self.ataque};{self.defesa};{self.arma};{self.escudo};{self.armadura}'