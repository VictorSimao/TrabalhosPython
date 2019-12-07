# Aula 19 - 04-12-2019
# Lista com for e metodos

# Como comer um gigante.... é com um pedaço de cada vez.
# Na hora de fazer este exercicio, atentar para 

# Com o arquivo de cadastro.txt onde possui os seguintes dados: codigo cliente, nome, idade, sexo, e-mail e telefone
# 1 - Crie um metodo que gere e retorne uma lista com bibliotecas com os dados dos clientes
# 2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
# Esta função tambem retornar uma lista com a biblioteca dos maiores de idades.
# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.
# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1
#  4.1 - A pesquisa deve aparecer uma frase para as seguintes condições:
#           Mulheres até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!""
#           Mulheres acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor alegria! O seu 
#                                            cruch vai adorar!"
#           Mulheres acima de 18:  "Olá {nome}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico
#                                                com o dobro de sabor!!!"
#           Homens até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!""
#           Homens acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor Corriga de carros!  
#                                          A sua amada vai adorar!"
#           Homens acima de 18:  "Olá {nome}! Já experimentou nossa cerveja? alto teor alcoolico
#                                                com o dobro do amargor!!!"
#      Lembre-se: É importante que apareça a frase. Pois a mesma será encaminhada por e-mail pela equipe de marketing


def ler_cadastro():
    arquivo = open('Aulas/Aula19/exercicios/cadastro.txt','r')
    lista_dados = []
    cabeçalho = ['codigo','nome','idade','sexo','e-mail','telefone']
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        dados = {}
        i = 0
        for linha in lista_linha:
            dados[cabeçalho[i]] = linha
            i += 1
        lista_dados.append(dados)
    return lista_dados

def separar_menores():
    arquivo_menores = open('Aulas/Aula19/exercicios/menores_idade.txt','w')
    arquivo_maiores = open('Aulas/Aula19/exercicios/maiores_idade.txt','w')
    for linha in resultado:
        if linha['idade'] < '18':
            arquivo_menores.write(f'{linha}\n')
        else:
            arquivo_maiores.write(f'{linha}\n')
    arquivo_maiores.close()
    arquivo_menores.close()

def separar_genero():
    arquivo_mulheres = open('Aulas/Aula19/exercicios/mulheres.txt','w')
    arquivo_homens = open('Aulas/Aula19/exercicios/homens.txt','a')
    count_m = 0
    count_f = 0
    for linha in resultado:
        if linha['sexo'] == 'f':
            arquivo_mulheres.write(f'{linha}\n')
            count_f += 1
        else:
            arquivo_homens.write(f'{linha}\n')
            count_m += 1
    arquivo_mulheres.close()
    arquivo_homens.close()

def clientes():
    cod = input('Digite o codigo do cliente: ')
    for linha in resultado:
        if linha['codigo'] == cod:
            if linha['sexo'] == 'f' and linha['idade'] < '16':
                print(f'{linha}')
                print(f'Ola {linha["nome"]}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!')
                return
            elif linha['sexo'] == 'f' and linha['idade'] > '16' and linha['idade'] <= '18':
                print(f'{linha}')
                print(f'Olá {linha["nome"]}! Quer experimentar nosso refigerante sabor alegria! O seu cruch vai adorar!')
                return
            elif linha['sexo'] == 'f' and linha['idade'] > '18':
                print(f'{linha}')
                print(f'Olá {linha["nome"]}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico com o dobro de sabor!!!')
                return
            elif linha['sexo'] == 'm' and linha['idade'] < '16':
                print(f'{linha}')
                print(f'Ola {linha["nome"]}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!')
                return
            elif linha['sexo'] == 'm' and linha['idade'] > '16' and linha['idade'] <= '18':
                print(f'{linha}')
                print(f'Olá {linha["nome"]}! Quer experimentar nosso refigerante sabor Corriga de carros! A sua amada vai adorar!')
                return
            elif linha['sexo'] == 'm' and linha['idade'] > '18':
                print(f'{linha}')
                print(f'Olá {linha["nome"]}! Já experimentou nossa cerveja? alto teor alcoolico com o dobro do amargor!!!')
                return
    print(f'Codigo {cod}. Não Cadastrado!')
            

resultado = ler_cadastro()

separar_genero()
separar_menores()
while True:
    clientes()
