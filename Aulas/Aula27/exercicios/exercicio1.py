# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int

from random import randint

lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int(randint(5,75))
lista3 = lista_simples_int(randint(5,70))


# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?

print(f'{len(lista1)}')


# 1.2) Qual é o maior valor da lista2?

print(f'{max(lista2)}')

# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?

print(f'{max(lista2)+min(lista2)}')

# 1.4) Qual é a média aritmética da lista1?

print(f'{sum(lista1)/len(lista1)}')

# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)

print(sum(lista1))
print(sum(lista2))
print(sum(lista3))
print(sum(lista1+lista2+lista3))


# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.

for i in lista1:
    print(f'{i}')

# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError

try:
    i = 1
    print(f'{lista1[5]}, {lista1[9]}, {lista1[10]}, {lista1[25]}')
    i = 2
    print(f'{lista2[5]}, {lista2[9]}, {lista2[10]}, {lista2[25]}')
    i = 3
    print(f'{lista3[5]}, {lista3[9]}, {lista3[10]}, {lista3[25]}')

except IndexError:
    print(f'Tamanho da lista {i} invalido')

# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).

if len(lista1) >= len(lista2):
    if len(lista1) >= len(lista3):
        print('Mais itens: lista 1')
if len(lista1) <= len(lista2):
    if len(lista2) >= len(lista3):
        print('Mais itens: lista 2')
if len(lista3) >= len(lista2):
    if len(lista3) >= len(lista1):
        print('Mais itens: lista 3')

print(f'Tamanho L1: {len(lista1)} L2: {len(lista2)} L3: {len(lista3)}')


# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.

if min(lista1) <= min(lista2):
    if min(lista1) <= min(lista3):
        menor_valor = min(lista1)
if min(lista2) <= min(lista1):
    if min(lista2) <= min(lista3):
        menor_valor = min(lista2)
if min(lista3) <= min(lista1):
    if min(lista3) <= min(lista2):
        menor_valor = min(lista3)

soma_maior = max(lista1)+max(lista2)+max(lista3)

print(f'{soma_maior} - {menor_valor} = {soma_maior - menor_valor}')

# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas

if min(lista1) <= min(lista2):
    if min(lista1) <= min(lista3):
        menor_valor = min(lista1)
if min(lista2) <= min(lista1):
    if min(lista2) <= min(lista3):
        menor_valor = min(lista2)
if min(lista3) <= min(lista1):
    if min(lista3) <= min(lista2):
        menor_valor = min(lista3)

if max(lista1) >= max(lista2):
    if max(lista1) >= max(lista3):
        maior_valor = min(lista1)
if max(lista2) >= max(lista1):
    if max(lista2) >= max(lista3):
        maior_valor = max(lista2)
if max(lista3) >= max(lista1):
    if max(lista3) >= max(lista2):
        maior_valor = max(lista3)

resultado = maior_valor + menor_valor

print(f'{resultado}')





