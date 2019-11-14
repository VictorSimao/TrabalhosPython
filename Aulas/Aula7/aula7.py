# Aula 7 14-11-2019
# Dicionarios

# Declarar dicionario
dicionario = { 'Nome':'Victor', 'Sobrenome':'Simão'}
bandas = {}
nome = []

# Imprimir dicionario
print(dicionario)
print(f"{dicionario['Sobrenome']}")

# Entrada de dados no dicionario
nome.append('Dejavu')
nome.append('Calipso')
bandas['Nome'] = nome[0]
bandas['Nome'] = nome[1]

nome= 'Teste'
lista_notas = [10,10,10,10]
media = sum(lista_notas)/len(lista_notas) # sum() = retorna a soma / len() = retorna a quantidade de item da lista
situacao = 'Reprovado'
if media >= 7:
    situacao = 'Aprovado'
dicionario_alunos = {'Nome': nome,'Lista_Notas':lista_notas,'Media':media, 'Situacao':situacao}

# Imprimir um item especificio do dicionario
print(f'{dicionario_alunos["Nome"]} - {dicionario_alunos["Media"]}')
print(f'{"Nome":nome[0]} - {bandas[nome[1]]}')
print(bandas)
