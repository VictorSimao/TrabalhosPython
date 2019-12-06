# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.


while True:
    try:
        n1 = int(input('Numero 1: '))
        n2 = int(input('Numero 2: '))
    
        print(f'A soma {n1} + {n2} = {n1 + n2}')
        print(f'A divisão de {n1} / {n2} = {n1 / n2}')
        print(f'A multiplicação de {n1} * {n2} = {n1 * n2}')
        print(f'A subtração de {n1} - {n2} = {n1 - n2}')

        sair = input('Digite s para sair ou enter para continuar: ')
        if sair == 's':
            break
    except ValueError:
        print('Digitou um valor invalido!')
    
    except ZeroDivisionError:
        print('Voce esta querendo dividir um inteiro por zero!')
