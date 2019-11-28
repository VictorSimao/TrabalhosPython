#--- Ex.3 Crie um programa para calculo de investimento, solicitar valor a ser investido no Tesouro Selic
#--- (Considerar valor do Tesouro Selic hoje) Calcular o valor total ate o vencimento do titulo
#--- Utilizar Metodos

from metodos import *

# unitario 10410
# min 104.10
# 5 + 0.02%
# Vencimento - 01/03/2025

qt_cota = int(input('Digite a quantidade de cota a ser investido(0.01 = R$104,10): '))

if qt_cota > 0.01:
    valor_inicial = qt_cota * 10410
else:
    print("Valor Invalido")

print(f'Valor final: {selic25(valor_inicial)}')

