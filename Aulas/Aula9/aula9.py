

from operacoes import soma, sub, mult, div, div_frac, resto, raiz

n1 = int(input('Digite numero 1: '))
n2 = int(input('Digite numero 2: '))

print(f'Soma: {soma(n1,n2)}\nSubtração: {sub(n1,n2)}\nMultiplicação: {mult(n1,n2)}\nDivisão Inteiro: {div(n1,n2)}\nDivisão fracionada: {div_frac(n1,n2)}\nResto: {resto(n1,n2)}\nRaiz: {raiz(n1,n2)}')