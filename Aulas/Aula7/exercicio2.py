# Exercicio 2
# Escreva um programa que leia os dados de 11 jogadores
# Jogador: Nome, Posição, Numero, PernaBoa
# Crie um dicionario para armazenar dos dados
# Imprima todos os jogadores e seus dados


lista_jogadores = []
for i in range(0,2):
    jogadores = {'Nome':'','Posicao':'','Numero':'','PernaBoa':''}
    jogadores['Nome']= input('Digite o nome: ')
    jogadores['Posicao']= input('Digite a posicao: ')
    jogadores['Numero']= input('Digite o numero: ')
    jogadores['PernaBoa']= input('Perna boa: ')
    lista_jogadores.append(jogadores)

for jogador in lista_jogadores:
    print(f'{jogadores["Nome"]} - {jogador["Posicao"]} - {jogador["Numero"]} - {jogador["PernaBoa"]}')