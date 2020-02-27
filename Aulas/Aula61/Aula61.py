numero = 100
numero = bin(numero)
numero = numero[2:]
numero = str(numero)
numero = numero.strip('0').split('1')
print (numero)
print (len(max(numero)))