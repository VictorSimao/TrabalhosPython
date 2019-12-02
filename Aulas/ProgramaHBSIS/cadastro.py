dados_cliente = ['Codigo_Cliente','CPF','Nome_Completo','Data_Nascimento','Estado','Cidade','Endereco']
lista_cliente = ()

def cadastro_cliente():
    cadastro = {}
    for i in dados_cliente:
        cadastro[i] = input(f'{i}: ')
    lista_cliente.append(cadastro)

def salvar_cliente():
    arquivo = open('clientes.txt','a')
    for i in lista_cliente:
        arquivo.write(f"{i};")
    arquivo.close()

def exibir_cliente():
    arquivo = open('clientes.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        linha_lista = linha.split(';')
        cliente = dados_cliente(linha_lista[0],linha_lista[1],linha_lista[2])
        lista_cliente.append(cliente)
    arquivo.close()



menu = '''
######################################################################################################################################
#                                                I Festival de Cerveja de Ituroró                                                    #
######################################################################################################################################

1 - Cadastro de Cliente
2 - Ver Clientes Cadastrados
3 - Cadastro de Produtos
4 - Ver Produtos Cadastrados
5 - Vendas
6 - Relarotio de Vendas
7 - Sair

Digite a opção desejada: '''

while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de Cliente')
        cadastro_cliente()
        salvar_cliente()
    elif opcao == '2':
        print('Ver Clientes Cadastrados')
        exibir_cliente()
    elif opcao == '3':
        print('Cadastro de Produtos')
    elif opcao == '4':
        print('Ver Produtos Cadastrados')
    elif opcao == '5':
        print('Vendas')
    elif opcao == '6':
        print('Relatorio de Vendas')
    elif opcao == '7':
        print('Sair')
        break
    else:
        print('Valor Invalido')