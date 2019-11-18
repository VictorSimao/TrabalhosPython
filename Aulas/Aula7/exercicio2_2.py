# Exercicio 2
# Escreva um programa que leia os dados de 11 jogadores
# Jogador: Nome, Posição, Numero, PernaBoa
# Crie um dicionario para armazenar dos dados
# Imprima todos os jogadores e seus dados

time = []
for i in range(0,2):
    jogadores={}
    jogadores['Nome']= input('Digite o nome: ')
    jogadores['Posicao']= input('Digite a posição: ')
    jogadores['Numero']= input('Digite o numero: ')
    jogadores['PernaBoa']= input('Perna Boa: ')
    time.append(jogadores)

for jogador in time:
    print(f"{jogador['Nome']} {jogador['Posicao']} {jogador['Numero']} {jogador['PernaBoa']}")