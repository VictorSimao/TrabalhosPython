# Aula 2 18/11/2019
# Input e Estrutura de desição

lista_numeros = [1,2,3]

if 'Teti'.count('t')>0:
    print('Existe "t" em "Teti" ')

if 'e' in 'Teti':
    print('Existe "e" em "Teti" ')

if 'M' not in 'Teti':
    print('Não existe "M" em "Teti" ')

num = ()
if num in lista_numeros:
    print('Existe')
else:
    print('Não Existe')

lista_vazia = []

if len(lista_numeros) == 0:
    print('Vazia')
else:
    print('Não Vazia')

if lista_vazia:
    print('Tem elementos')
else:
    print('Lista Vazia')

nome = ''

if nome:
    print('Preenchida')
else:
    print('Nome Vazio')