def transfer(recebe,exclue):
    recebe.append(exclue[0])
    exclue.pop(0)

terminal = ['piloto','oficial_1','oficial_2','chefe','comissario_1','comissario_2','policial','prisioneiro']
carro = []
aviao = [] 

while not not terminal:
    print('########## TERMINAL #########')
    print(f'Terminal: {terminal}')
    print(f'Carro: {carro}')
    if not carro:
        transfer(carro,terminal)
    print('########## INDO PARA O AVIAO ##########')
    if terminal[0] == 'policial':
        terminal.append(carro[0])    
        carro.clear()
        transfer(carro,terminal)
        transfer(carro,terminal)
    else:
        transfer(carro,terminal)
    print(f'Dirigindo: {carro[0]} Passageiro: {carro[1]}')
    print('########## AVIAO ##########')
    if carro[0] == 'policial':
        carro.append('piloto')
        aviao.pop(2)
        transfer(aviao,carro)
        transfer(aviao,carro)
    elif carro[1] == 'chefe':
        transfer(aviao,carro)
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