#--- Exercício 2 - For
#--- Escreva programa que leia um número inteiro
#--- Calcule a taboada do número informado
#--- Imprima a taboada com a conta completa (n * i = r)

num = int(input('Digite um numero inteiro: '))
for i in range(0, 11):
    print(f'{i} x {num} = {i*num}')