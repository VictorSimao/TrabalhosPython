
terminal = ['piloto','oficial_1','oficial_2','chefe','comissario_1','comissario_2','policial','prisioneiro']
carro = []
aviao = [] 

while not not terminal:
    print('########## TERMINAL #########')
    print(f'Terminal: {terminal}')
    print(f'Carro: {carro}')
    if not carro:
        carro.append(terminal[0])
        terminal.pop(0)
    print('########## INDO PARA O AVIAO ##########')
    if terminal[0] == 'policial':
        terminal.append(carro[0])    
        carro.clear()
        carro.append(terminal[0])
        terminal.pop(0)
        carro.append(terminal[0])
        terminal.pop(0)
    else:
        carro.append(terminal[0])
        terminal.pop(0)
    print(f'Dirigindo: {carro[0]} Passageiro: {carro[1]}')
    print('########## AVIAO ##########')
    if carro[0] == 'policial':
        carro.append('piloto')
        aviao.pop(2)
        aviao.append(carro[0])
        carro.pop(0)
        aviao.append(carro[0])
        carro.pop(0)
    elif carro[1] == 'chefe':
        aviao.append(carro[0])
        carro.pop(0)
    else:
        aviao.append(carro[-1])
        carro.pop(-1)
    print(f'Aviao: {aviao}')
    if not not terminal:
        print('########## INDO PARA O TERMINAL ##########')
        print(f'Dirigindo: {carro}')
    else:
        aviao.append(carro[-1])
        carro.clear()
        print(f'Aviao: {aviao}')
        print('EMBARQUE FINALIZADO')