
from model.heroi import Heroi
from dao.heroi_db import HeroiDb
from dao.inimigo_db import InimigoDb
from dao.itens_db import ItensDb

import random
from time import sleep

import os
clear = lambda: os.system('cls')

class LutaController:
    h = HeroiDb()
    heroi = h.exibir()
    i = InimigoDb()
    inimigo = i.invocar(int(heroi.level))
    e = ItensDb()

    def turno_heroi(self):
        self.layout()
        sleep(0.5)
        dado = self.rolar_dado()
        clear()
        if (self.heroi.ataque + self.heroi.arma + dado) > (self.inimigo.defesa + self.inimigo.escudo + self.inimigo.armadura):
            self.layout()
            dano = (self.heroi.ataque + self.heroi.arma + dado)-(self.inimigo.defesa + self.inimigo.escudo + self.inimigo.armadura)
            self.inimigo.vida -= dano
            print(f'========================= TURNO DO HEROI =============================')
            sleep(.5)
            print(f'\t{dano} de dano sera causado ao {self.inimigo.nome}.')
            sleep(1)
            if self.inimigo.vida <= 0:
                self.inimigo.vida = 0
                clear()
                self.layout()
                sleep(0.5)
                print(f'\t{self.heroi.nome} matou o {self.inimigo.nome}.')
                sleep(1)
                print(f'\t{self.heroi.nome} subiu de level.')
                self.heroi.level += 1
                sleep(1)
                clear()
                self.turno_espolio()
                if self.heroi.level < 5:
                    print(f'\tInvocando o próximo adversario:')
                    self.inimigo = self.i.invocar(int(self.heroi.level))
                    sleep(1)
                    print(f'\t{self.inimigo.nome} se apresentando para a batalha!')
                    input('\n\t\tpressione enter para continuar')
                    clear()
            elif self.inimigo.vida > 0:
                sleep(.5)
                print(f'\t{self.inimigo.nome} ira atacar {self.heroi.nome}')
                input('\n\t\tpressione enter para continuar')
                clear()
                self.turno_inimigo()
        else:
            self.layout()
            print(f'========================= TURNO DO HEROI =============================')
            print(f'\tNão tirou dano do {self.inimigo.nome} !!!')
            input('\n\t\tpressione enter para continuar')
            clear()
            self.turno_inimigo()
        


    def turno_inimigo(self):
        self.layout()
        clear()
        if (self.inimigo.ataque + self.inimigo.arma) > (self.heroi.defesa + self.heroi.escudo + self.heroi.armadura):
            self.layout()
            dano = (self.inimigo.ataque + self.inimigo.arma) - (self.heroi.defesa + self.heroi.escudo + self.heroi.armadura)
            self.heroi.vida -= dano
            print(f'\t{dano} de dano sera causado ao {self.heroi.nome}.')
            sleep(3)
            if self.heroi.vida <= 0:
                clear()
                sleep(0.5)
                print(f'\t\t\tM')
                sleep(0.5)
                print(f'\t\t\tO')
                sleep(0.5)
                print(f'\t\t\tR')
                sleep(0.5)
                print(f'\t\t\tR')
                sleep(0.5)
                print(f'\t\t\tE')
                sleep(0.5)
                print(f'\t\t\tU')
                sleep(2)
            else:
                print(f'\tSeu turno de atacar.')
                input('\n\t\tpressione enter para continuar')
                clear()
                self.turno_heroi()
        else:
            self.layout()
            print(f'======================== TURNO DO ADVERSARIO ==========================')
            print(f'\tNão tirou dano do {self.heroi.nome} !!!')
            input('\n\t\tpressione enter para continuar')
            clear()
            self.turno_heroi()
    
    def turno_espolio(self):
        self.layout()
        sleep(0.5)
        x = random.randint(1,9)
        item = self.e.craftar(x)
        print(f'\t{item.nome} dropou de {self.inimigo.nome}')
        sleep(.5)
        print(f'\t1-Equipar\t\t3-Ignorar')
        cod = int(input('\tEscolha a opção: '))
        clear()
        if cod == 1:
            if item.id > 0 and item.id < 6:
                self.heroi.arma = item.arma
            elif item.id > 5 and item.id < 8:
                self.heroi.armadura = item.armadura
            elif item.id > 7:
                self.heroi.escudo = item.escudo
            self.layout()
            sleep(0.5)
            print(f'\tVocê equipou {item.nome}')
        else:
            self.layout()
            sleep(0.5)
            print(f'\tIgnorou o espolio da luta !!')
        input('\n\t\tpressione enter para continuar')
        clear()
        self.layout()
    
    def layout(self):
        return print(f'''
############################ COMBATE ##################################
\t{self.heroi.nome} {self.heroi.level} \t\tx\t {self.inimigo.nome}
\tVida: {self.heroi.vida} \t\tx\t Vida: {self.inimigo.vida}
\tAtaque: {self.heroi.ataque} \t\tx\t Ataque: {self.inimigo.ataque}
\tDefesa: {self.heroi.defesa} \t\tx\t Defesa: {self.inimigo.defesa}
\tArma: {self.heroi.arma} \t\tx\t Arma: {self.inimigo.arma}
\tEscudo: {self.heroi.escudo} \t\tx\t Escudo: {self.inimigo.escudo}
\tArmadura: {self.heroi.armadura} \t\tx\t Armadura: {self.inimigo.armadura}
#######################################################################''')

    def rolar_dado(self):
        for i in range(1,10):
            clear()
            self.layout()
            print(f'\tRolando o dado...')
            x = random.randint(1, 6)
            if x == 1:
                dado = '''
                \t#########
                \t#       #
                \t#       #
                \t#   #   #
                \t#       #
                \t#       #
                \t#########
                '''
            elif x == 2:
                dado = '''
                \t#########
                \t#       #
                \t#       #
                \t# #   # #
                \t#       #
                \t#       #
                \t#########
                '''
            elif x == 3:
                dado = '''
                \t#########
                \t#       #
                \t#   #   #
                \t#   #   #
                \t#   #   #
                \t#       #
                \t#########
                '''
            elif x == 4:
                dado = '''
                \t#########
                \t#       #
                \t# #   # #
                \t#       #
                \t# #   # #
                \t#       #
                \t#########
                '''
            elif x == 5:
                dado = '''
                \t#########
                \t#       #
                \t# #   # #
                \t#   #   #
                \t# #   # #
                \t#       #
                \t#########
                '''
            elif x == 6:
                dado = '''
                \t#########
                \t#       #
                \t# #   # #
                \t# #   # #
                \t# #   # #
                \t#       #
                \t#########
                '''
            print(dado)
            sleep(0.2)
            clear()
        self.layout()
        print(f'\tRolando o dado...')
        print(f'{dado}\t\t\t..tirou {x}')
        input('\n\t\tpressione enter para continuar')
        return x

         
        
