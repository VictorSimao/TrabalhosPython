from metodos import *

investimento = float(input('Digite o valor investido: '))
taxa = float(input('Digite a  taxa de juro: '))
prazo = int(input('Digite o prazo do investimento em meses: '))
total = float(rentabilidade(investimento, taxa, prazo))
porc_final = float(porc(investimento, total))
print(f'Investimento inicial: {investimento}\nValor final: {total:.2f}\n% final: {porc_final:.2f}')