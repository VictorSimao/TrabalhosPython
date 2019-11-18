#--- Exercicio 1  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia dois números inteiros
#--- Realize as 4 operações matemáticas básicas com os números lidos
#--- Imprima os resultados das operações 
#--- Informe qual número é maior ou se os dois são iguais

n1=int(input('Numero 1: '))
n2=int(input('Numero 2: '))

print(f'Adição: {n1+n2}, Subtração: {n1-n2}, Multiplicação: {n1*n2}, Divisão: {n1/n2}')

if n1>n2:
    print(f'{n1} é maior')
elif n2>n1:
    print(f'{n2} é maior')
else:
    print(f'{n1} e {n2} são iguais')