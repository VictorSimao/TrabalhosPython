# n = int(input('Numero: '))

# def digital_root(n):
#     num = n
#     soma = 0
#     while num >= 10:
#         soma += (num%10) # Resto
#         num = num // 10 # Div q retorna inteiro
#     resultado = soma + num
#     if resultado > 10:
#             digital_root(resultado)
#     return resultado


# print(digital_root(n))

num = int(input('Numero: '))
pronto = True
while pronto:
    soma = num // 10
    num = num % 10
    # soma += num
    if num < 10:
        soma += num
    if soma > 10:
        num = soma
    else:
        pronto = False

print(soma)