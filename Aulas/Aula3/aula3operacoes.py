nome = input('Digite seu nome:')
sobrenome = input('Digite seu sobrenome:')
idade = int(input('Digite sua idade:'))fa

print(f'Nome Completo: {nome} {sobrenome}\nIdade: {idade} anos')

if idade < 18:
    print('Menor')
if idade >= 18:
    print('Maior')
if idade == 18:
    print('o/')

if idade < 18:
    print('Menor')
else:
    print('Maior')
