
from model.item import Item

class ItensDb:

    def craftar(self, id):
        x = Item()
        with open('C:/Users/Familia Nande Simão/Documents/GitHub/TrabalhosPython/Estudo/GameArena/dao/itens.txt','r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                lista = linha.split(';')
                x.id = int(lista[0])
                x.nome = lista[1]
                x.arma = int(lista[2])
                x.escudo = int(lista[3])
                x.armadura = int(lista[4])
                if x.id == id:
                    return x
