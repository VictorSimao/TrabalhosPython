#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)

nome = []
media = []
resultado = []
for i in range(0,2):
    nome.append(input('Digite o nome: '))
    nota = 0
    for i in range(0,4):
        nota += int(input(f'Digite {i+1} nota: '))
    media.append(nota/4)

for i in range(0,2):
    if media[i] >= 7:
        resultado.append('Aprovado')
    else:
        resultado.append('Reprovado')

for i in range(0,2):
    print(f'Aluno: {nome[i]} - Media: {media[i]} - Resultado: {resultado[i]}')
