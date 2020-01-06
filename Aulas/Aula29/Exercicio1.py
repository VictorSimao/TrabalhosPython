''' A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
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

Equipe tecnica:
- 1 Piloto e 2 oficias

Tripulação de cabine:
- Chefe de serviço e 2 comissarias

Tripulação extra:
- 1 policial e 1 presidiario

Veiculo Smart Fortwo:
- Apenas duas pessoas.
- Policial e presidiario sempre juntos.
- Dirigir: Piloto, Chefe de Serviço e Policial.
- Proibido: piloto com comissarias, chefe com oficiais, 

Passo a passo:
1 - Terminal: 2 oficiais, policial e presidiario, 2 comissario / Fortwo indo: piloto e chefe / Avião: vazio
2 - Terminal: 2 oficiais, policial e presidiario, 2 comissario / Fortwo voltando: Chefe / Avião: Piloto
3 - Terminal: 2 oficiais, chefe, 2 comissario / Fortwo indo: policial e presidiario / Avião: Piloto
4 - Terminal: 2 oficiais, chefe, 2 comissario / Fortwo voltando: piloto / Avião: policial e presidiario
5 - Terminal: 2 oficiais, chefe, 2 comissario / Fortwo indo: piloto e 1 oficial / Avião: policial e presidiario
6 - Terminal: 1 oficiais, chefe, 2 comissario / Fortwo voltando: piloto / Avião: policial e presidiario, 1 oficial
7 - Terminal: chefe, 2 comissario / Fortwo indo: piloto e 1 oficial / Avião: policial e presidiario, 1 oficial
8 - Terminal: chefe, 2 comissario / Fortwo voltando: piloto / Avião: policial e presidiario, 2 oficial
9 - Terminal: 2 comissario / Fortwo indo: piloto e chefe / Avião: policial e presidiario, 2 oficial
10 - Terminal: 2 comissario / Fortwo voltando: chefe / Avião: policial e presidiario, piloto, 2 oficial
11 - Terminal: 1 comissario / Fortwo indo: chefe e 1 comissario / Avião: policial e presidiario, piloto, 2 oficial
12 - Terminal: 1 comissario / Fortwo voltando: chefe / Avião: policial e presidiario, piloto, 2 oficial, 1 comissario
13 - Terminal: vazio / Fortwo indo: chefe e 1 comissario / Avião: policial e presidiario, piloto, 2 oficial, 1 comissario
14 - Terminal: vazio / Fortwo: vazio / Avião:policial e presidiario, piloto, 2 oficial, chefe, 2 comissario

Requisitos:
1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
5 - Deve ser feito em Python'''


terminal = ['piloto', 'chefe_servico', 'policial', 'oficial_1', 'oficial_2', 'comissaria_1', 'comissaria_2', 'presidiario']
fortwo = []
aviao = []


for i in terminal:
    if i == 'policial':
        terminal.remove('piloto')
        terminal.remove('chefe_servico')
        fortwo.append('piloto')
        fortwo.append('chefe_servico')
print(f'Terminal: {terminal}')
print(f'Fortwo: {fortwo}')
print(f'Avião: {aviao}')
