#Aula 4
#Fazer um programa e leia 2 numeros
#Realize as 4 operações matematicas
#Imprima o resultado das operações
#Diga qual numero é o maior dos dois numeros

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segunda numero: '))

print('Adição:', num1+num2)
print('Subtração:', num1-num2)
print('Multiplicação:', num1*num2)
print('Divisão:', num1/num2)

print(f'Adição: {num1+num2}\nSubtração: {num1-num2}\nMultiplicação: {num1*num2}\nDivisão: {num1/num2}\n')

if num1 >= num2:
    print('Numero maior:', num1)
else:
    print('Numero maior:', num2)
