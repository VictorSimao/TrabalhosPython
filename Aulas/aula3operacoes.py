nome = input('Digite seu nome:')
sobrenome = input('Digite seu sobrenome:')
idade = int(input('Digite sua idade:'))

print(f'Nome Completo: {nome} {sobrenome}\nIdade: {idade} anos')

if idade < 18:
    print('Menor')
