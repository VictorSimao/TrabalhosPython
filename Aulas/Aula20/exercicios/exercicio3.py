# Aula 20 - 05-12-2019


# Surgiu a necessidade de envio massivo de e-mails dos clientes cadastrados
# no arquivo cadastro1.txt 

# >>>> Fazer tudo com metodos <<<<<

# 1 - Para isso o programa necessita que separe os clientes menores de 20 anos 
# em um arquivo separado chamado menores_de_idade.txt

# 2 - Separar os clientes femininos e salvar em um arquivo chamado feminino.txt

# 3 - Fazer um terminal de consulta onde se digita o código cliente e 
# imprima na tela o (f-string) o codigo, nome, idade, sexo, email, telefone.
# Se digitar um número que não exista, deverá aparecer uma mensagem dizendo
# "código não encontrado!" Se digitar 'S' (sair) o programa deve finalizar.

def consulta():
    cod = input('Digite o codigo do cliente: ')
    arquivo = open('Aulas/Aula20/exercicios/cadastro1.txt','r',encoding="utf8")
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        if lista_linha[0] == cod:
            print(f'{lista_linha}')
            arquivo.close()
            return cod
        elif cod == 's':
            arquivo.close()
            return cod
    print('Código não encontrado!')
    arquivo.close()
    return cod

def separar_menores():
    arquivo = open('Aulas/Aula20/exercicios/cadastro1.txt','r',encoding="utf8")
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        if lista_linha[2] < '20':
            arquivo = open('Aulas/Aula20/exercicios/menores_de_idade.txt','a')
            arquivo.write(f"{lista_linha}\n")
            arquivo.close()
    arquivo.close()


def separar_feminino():
    arquivo = open('Aulas/Aula20/exercicios/cadastro1.txt','r',encoding="utf8")
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        if lista_linha[3] == 'f':
            arquivo = open('Aulas/Aula20/exercicios/feminino.txt','a')
            arquivo.write(f"{lista_linha}\n")
            arquivo.close()
    arquivo.close()

# separar_menores()
# separar_feminino()
while True:
    sair = consulta()
    if sair == 's':
        break