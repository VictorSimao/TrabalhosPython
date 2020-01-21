
from model.inimigo import Inimigo

class InimigoDb:

    def invocar(self, id):
        x = Inimigo()
        with open('Estudo/GameArena/dao/inimigos.txt','r') as arquivo:
            for linha in arquivo:
                lista = linha.split(';')
                x.id = int(lista[0])
                x.nome = lista[1]
                x.vida = int(lista[2])
                x.ataque = int(lista[3])
                x.defesa = int(lista[4])
                x.arma = int(lista[5])
                x.escudo = int(lista[6])
                x.armadura = int(lista[7])
                if x.id == id:
                    return x
    
    
    