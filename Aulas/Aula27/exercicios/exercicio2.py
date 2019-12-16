# Aula 21 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como defult ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10)

print(lista)

a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.




lista = embaralhar(2,10,2)

print(lista)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).

if (lista[0] is lista[1]):
    print('Apontam local de memoria') 
else:
    print('Não apontam para o mesmo local de memoria')

# 2) Qual é o maior valor destas duas listas 

if max(lista[0]) > max(lista[1]):
    print(f'Maior valor: {max(lista[0])}')
else:
    print(f'Maior valor: {max(lista[1])}')


# 3) Qual é o maior valor de cada lista

print(f'Maior lista 0 = {max(lista[0])}')
print(f'Maior lista 1 = {max(lista[1])}')

# 4) Há o número 10 dentro da lista[0]?

if 10 in lista[0]: 
    print(f'Tem 10 na lista 0 !')
else:
    print('Não tem 10 na lista 0 !')

# 5) Há o número 20 dentro da lista[1]?

if 20 in lista[1]: 
    print(f'Tem 20 na lista 1 !')
else:
    print('Não tem 20 na lista 1 !')

# 6) Quantos números da lista[0] tem dentro da lista[1]?
count = 0
for i in lista[0]:
    for x in lista[1]:
        if i == x:
            count += 1

print(f'Tem {count} da lista 0 na lista 1')


# 7) Mostre os números da lista[0] que estão dentro da lista[1]

for i in lista[0]:
    for x in lista[1]:
        if i == x:
            print(f'{i}')


# 8) Mutliplique a soma da lista[0] com cada item da lista[1]
resultado = 0
for i in lista[1]:
    resultado += (i * sum(lista[0]))

print(f'Total: {resultado}')

# 9) Faça uma divisão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!

if max(lista[0]) > max(lista[1]):
    maior_valor = max(lista[0])
else:
    maior_valor = max(lista[1])

if min(lista[0]) < min(lista[1]):
    menor_valor = min(lista[0])
else:
    menor_valor = min(lista[1])

resultado = maior_valor // menor_valor

for i in lista[0]:
    if resultado == i:
        print(f'Contém {resultado} na lista 0, posição {i}')
for i in lista[1]:
    if resultado == i:
        print(f'Contém {resultado} na lista 0, posição {i}')

print(resultado)



# 10) Verifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]

for i in lista[1]:
    if max(lista[0]) == i:
        print(f'Maior numero da lista[0] esta dentro da lista[1]')

for i in lista[0]:
    if min(lista[0]) == i:
        print(f'Menor numero da lista[1] esta dentro da lista[0]')

