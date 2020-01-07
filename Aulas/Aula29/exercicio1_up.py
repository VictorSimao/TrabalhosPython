from Air import airlines
air = airlines()

terminal = ['piloto','oficial_1','oficial_2','chefe','comissario_1','comissario_2','policial','prisioneiro']
carro = []
aviao = [] 

while not not terminal:
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
    else:
        print(f'\nPor último, {carro[0]} embarca no avião.')
        aviao.append(carro[-1])
        carro.clear()
        print('\n########## AVIAO ##########')
        air.listar_aviao(aviao)
        print('\nEMBARQUE FINALIZADO!')