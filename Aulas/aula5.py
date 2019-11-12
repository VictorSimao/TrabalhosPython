n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

lista = [n1, n2, n3, n4]
print(f'Maior nota: ', max(lista))

print(f'Menor nota: ', min(lista))

maior = float(0)
if n1 >= n2 and n1 >= n3 and n1 >= n4:
    maior = n1
elif n2 >= n1 and n2 >= n3 and n2 >= n4:
    maior = n2
elif n3 >= n1 and n3 >= n2 and n3 >= n4:
    maior = n3
elif n4 >= n1 and n4 >= n2 and n4 >= n3:
    maior = n4

print(f'Maior nota: {maior}')

menor = float(0)
if n1 <= n2 and n1 <= n3 and n1 <= n4:
    menor = n1
elif n2 <= n1 and n2 <= n3 and n2 <= n4:
    menor = n2
elif n3 <= n1 and n3 <= n2 and n3 <= n4:
    menor = n3
elif n4 <= n1 and n4 <= n2 and n4 <= n3:
    menor = n4 
    
print(f'Menor nota: {menor}')

media = float((n1+n2+n3+n4)/4)
print(f'Media final: {media}')

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')