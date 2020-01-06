from Air import listar_terminal, listar_aviao, listar_carro

terminal = ['Piloto', 'Oficial 1', 'Oficial 2', 'Chefe de Serviço', 'Comissária 1', 'Comissária 2', 'Policial', 'Prisioneiro']
aviao = []
smart = []

print('#'*55, '\nVIAGEM 1\n', '#'*55, sep='')
print('\nEmbarcam no Fortwo: ')
smart.append('Piloto')
smart.append('Oficial 1')
terminal.pop(0)
terminal.pop(0)
listar_carro(smart)

print('\nTerminal: ')
listar_terminal(terminal)

print('\nFortwo chega ao avião.')

print(f'\nEmbarcam no avião: Oficial 1 ')
aviao.append('Oficial 1')
smart.pop(1)

print('\nPessoas no avião: ')
listar_aviao(aviao)

print('\nFortwo volta para o terminal com: ')
listar_carro(smart)

print('\nFortwo chega no terminal.')

print('#'*55, '\nVIAGEM 2\n', '#'*55, sep='')
print('\nEmbarcam no Fortwo: ')
smart.append('Oficial 2')
terminal.pop(0)
listar_carro(smart)

print('\nTerminal: ')
listar_terminal(terminal)

print('\nFortwo chega ao avião.')

print(f'\nEmbarcam no avião: Oficial 2 ')
aviao.append('Oficial 2')
smart.pop(1)

print('\nPessoas no avião: ')
listar_aviao(aviao)

print('\nFortwo volta para o terminal com: ')
listar_carro(smart)

print('#'*55, '\nVIAGEM 3\n', '#'*55, sep='')
print('\nEmbarcam no Fortwo: ')
smart.append('Chefe de Serviço')
terminal.pop(0)
listar_carro(smart)

print('\nTerminal: ')
listar_terminal(terminal)

print('\nFortwo chega ao avião.')

print(f'\nEmbarcam no avião: Piloto')
aviao.append('Piloto')
smart.pop(0)

print('\nPessoas no avião: ')
listar_aviao(aviao)

print('\nFortwo volta para o terminal com: ')
listar_carro(smart)

print('#'*55, '\nVIAGEM 4\n', '#'*55, sep='')
print('\nEmbarcam no Fortwo: ')
smart.append('Comissária 1')
terminal.pop(0)
listar_carro(smart)

print('\nTerminal: ')
listar_terminal(terminal)

print('\nFortwo chega ao avião.')

print(f'\nEmbarcam no avião: Comissária 1')
aviao.append('Comissária 1')
smart.pop(1)

print('\nPessoas no avião: ')
listar_aviao(aviao)

print('\nFortwo volta para o terminal com: ')
listar_carro(smart)

print('#'*55, '\nVIAGEM 5\n', '#'*55, sep='')
print('\nEmbarcam no Fortwo: ')
smart.append('Comissária 2')
terminal.pop(0)
listar_carro(smart)

print('\nTerminal: ')
listar_terminal(terminal)

print('\nFortwo chega ao avião.')

print(f'\nEmbarcam no avião: Comissária 2')
aviao.append('Comissária 2')
smart.pop(1)

print('\nPessoas no avião: ')
listar_aviao(aviao)

print('\nFortwo volta para o terminal com: ')
listar_carro(smart)

print('#'*55, '\nVIAGEM 6\n', '#'*55, sep='')
print('\nEmbarcam no Fortwo: ')
smart.pop(0)
smart.append('Policial')
smart.append('Prisioneiro')
terminal.pop()
terminal.pop()
terminal.append('Chefe de Servico')
listar_carro(smart)

print('\nTerminal: ')
listar_terminal(terminal)

print('\nFortwo chega ao avião.')

print(f'\nEmbarcam no avião: Policial e Prisioneiro')
aviao.append('Policial')
aviao.append('Prisioneiro')
smart.pop(0)
smart.pop(0)
smart.append('Piloto')

print('\nPessoas no avião: ')
listar_aviao(aviao)

print('\nFortwo volta para o terminal com: ')

listar_carro(smart)