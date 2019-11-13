# Aula 6 - 13/11/2019
# Estrutura de repetição - FOR

# For simples usando range com incremento padrão de 1
for i in range(0,20): # range(inicio, fim, incremento)
    print(f'{i}-Messagem')

# Imprimir numeros pares ate 100
for i in range(0,101,2):
    print(f'{i}- Pares')

# Imprimir lista com for
lista = ['Mateus','Marcela','Nicole','Pablo']
for i in range(0,4):
    print(lista[i])

for i in lista:
    print(i)

numero = 10
for i in range(0,11):
    print(f'{i} x {numero} = {i*numero}')