
from model.heroi import Heroi
from dao.itens_db import ItensDb

class HeroiDb:

    def exibir(self):
        x = Heroi()
        with open('Estudo/GameArena/dao/heroi.txt','r') as arquivo:
            for linha in arquivo:
                lista = linha.split(';')
            x.nome = lista[0]
            x.vida = int(lista[1])
            x.level = int(lista[2])
            x.ataque = int(lista[3])
            x.defesa = int(lista[4])
            x.arma = int(lista[5])
            x.escudo = int(lista[6])
            x.armadura = int(lista[7])
        return x

    def equipar(self, id):
        pass

    def salvar(self):
        pass

    def deletar(self):
        pass