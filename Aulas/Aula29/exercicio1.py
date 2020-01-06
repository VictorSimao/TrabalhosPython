'''A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

Requisitos:
1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
5 - Deve ser feito em Python'''

# 'piloto','oficial_1','oficial_2','chefe','comissario_1','comissario_2','policial','presidiario'

def ida(lista):
    carro = []
    carro.append(lista[0])
    carro.append(lista[-1])
    lista.pop()
    return carro

trip_tecnica = ['piloto','oficial_1','oficial_2']
trip_cabine = ['chefe','comissario_1','comissario_2']
trip_passageiro = ['policial','presidiario']
terminal = []
aviao = []
carro = []
i = 0

while i != 2:
    terminal.clear()
    terminal.extend(trip_tecnica)
    terminal.extend(trip_cabine)
    terminal.extend(trip_passageiro)
    print(f'Terminal: {terminal}')
    print(f'Carro: {carro}')
    print(f'Avião: {aviao}')
    carro.append(ida(trip_tecnica))
    print(f'Carro: {carro}')
    i += 1







