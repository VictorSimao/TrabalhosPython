from Air import airlines
from time import sleep
from termcolor import colored
air = airlines()

terminal = air.abrir()
carro = []
aviao = [] 
cont = 1

while not not terminal:
    print(colored(f'\n########## VIAGEM {cont} #########', 'green'))
    print('\n########## TERMINAL #########')
    air.listar_terminal(terminal)
    air.listar_carro(carro)
    if not carro:
        air.transfer(carro,terminal)
    print('\n########## INDO PARA O AVIAO ##########')
    if terminal[0] == 'policial':
        terminal.append(carro[0])    
        carro.clear()
        air.transfer(carro,terminal)
        air.transfer(carro,terminal)
    else:
        air.transfer(carro,terminal)
    print(f'Dirigindo: {carro[0]} Passageiro: {carro[1]}')
    print('\n########## AVIAO ##########')
    if carro[0] == 'policial':
        carro.append('piloto')
        aviao.pop(2)
        air.transfer(aviao,carro)
        air.transfer(aviao,carro)
    elif carro[1] == 'chefe':
        air.transfer(aviao,carro)
    else:
        aviao.append(carro[-1])
        carro.pop(-1)
    air.listar_aviao(aviao)
    if not not terminal:
        print('\n########## INDO PARA O TERMINAL ##########')
        print(f'Dirigindo: {carro[0]}')
        sleep(2)
    else:
        print(colored(f'\nPor último, {carro[0]} embarca no avião.', 'green'))
        aviao.append(carro[-1])
        carro.clear()
        sleep(2)
        print('\n########## AVIAO ##########')
        air.listar_aviao(aviao)
        print(colored('\nEMBARQUE FINALIZADO!', 'red'))
        air.gravar(aviao)
    cont += 1