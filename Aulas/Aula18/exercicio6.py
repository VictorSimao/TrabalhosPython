# Aula 18 - 03-11-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: codigo, nome, sexo, idade

# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) do que para os homens (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.

# 3 - Faça uma terceira função que ao digitar o código do participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de idade apareça o texto "Entrada Proibida!"

def dicionario():
    lista_dic = []
    arquivo = open('Aulas/Aula18/cadastro.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        dic_convidados = {'codigo':lista_linha[0],'nome':lista_linha[1],'sexo':lista_linha[2],'idade':lista_linha[3]}
        lista_dic.append(dic_convidados)
    arquivo.close()
    return lista_dic

def separar_sexo():
    for linha in convidados:
        if linha['sexo'] == 'f':
            arquivo = open('Aulas/Aula18/lista_mulher.txt','a')
            arquivo.write(f"{linha['codigo']};{linha['nome']};{linha['sexo']};{linha['idade']}\n")
            arquivo.close()
        elif linha['sexo'] == 'm':
            arquivo = open('Aulas/Aula18/lista_homem.txt','a')
            arquivo.write(f"{linha['codigo']};{linha['nome']};{linha['sexo']};{linha['idade']}\n")
            arquivo.close()

def entrada():       
    cod = input('Digite o codigo: ')
    arquivo = open('Aulas/Aula18/lista_mulher.txt','r')
    for linha in arquivo:
        lista_linha = linha.split(';')
        if lista_linha[0] == cod:
            if lista_linha[3] < '18':
                print("Entrada Proibida!")
            else:
                print(f'{lista_linha[1]} - R$ 15,00')  
    arquivo.close()

    arquivo = open('Aulas/Aula18/lista_homem.txt','r')
    for linha in arquivo:
        lista_linha = linha.split(';')
        if lista_linha[0] == cod:
            if lista_linha[3] < '18':
                print("Entrada Proibida!")
            else:
                print(f'{lista_linha[1]} - R$ 35,00')
    arquivo.close()
    return cod

convidados = dicionario()

# separar_sexo()

while True:
    entrada()
    
