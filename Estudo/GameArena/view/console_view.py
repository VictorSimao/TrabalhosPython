import sys
sys.path.append('C:/Users/Familia Nande Simão/Documents/GitHub/TrabalhosPython/Estudo/GameArena')

from time import sleep

from dao.heroi_db import HeroiDb
from dao.inimigo_db import InimigoDb
from controller.luta_controller import LutaController

import os
clear = lambda: os.system('cls')

luta = LutaController()

while True:
    clear()
    luta.layout()
    print('\t1 - Lutar\t\t3 - Fugir')
    cod = int(input('\tEscolha a opção: '))
    if cod == 1:
        clear()
        luta.turno_heroi()
    elif cod == 3:
        print('\tOpção não implementada!')
        print('\tNovidades em Breve')
        sleep(3)
    if luta.heroi.vida <= 0:
        clear()
        print('############################################################')
        print('\n\n\n\t\t\tGAME OVER\n\n\n')
        print('############################################################')
        break
    elif luta.heroi.level == 5:
        clear()
        print('############################################################')
        print('\n\n\n\t\t\tWIN THE GAME\n\n\n')
        print('############################################################')
        break