arquivo = open('Aulas/Aula18/cadastro.txt','r')

conteudo = arquivo.read()

lista_arquivo = conteudo.split('\n')

primeira_linha = lista_arquivo[0]

lista_primeira_linha = primeira_linha.split(';')

arquivo.close()

print(primeira_linha)

print(lista_primeira_linha[0])

print(type(arquivo))