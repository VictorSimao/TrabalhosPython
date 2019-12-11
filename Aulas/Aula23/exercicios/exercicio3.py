# Aula 22 - 10-12-2019
# # Como Tratar e Trabalhar Erros!!!

# Dica: O mais importante é conseguir fazer! Não importa como chegou ao resultado e sim o resultado!

# Dica2: na função .open() você pode escolher entre 'r' para ler, 'w' para sobrescrever e criar um 
# arquivo novo ou o 'a' que é abreveativo de append, onde ele inclui linha no final do arquivo.
# Você sabia que o 'r', 'w' e o 'a' são string que podem ser passadas via variável exemplo:

# atributo = 'r'
# nome_arquivo = 'cadastro'
# arquivo.open(f'exercicio/{nome_arquivo}.txt',atributo)



# 1) Crie uma classe cadastro.
# Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastro numa lista com dicionários.

# 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
# 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode 
# se repetir.
# 3) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
# 4) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
#
#  Observação: Use o try/filnaly para abrir e fechar os arquivos. Veja na aula 21- Ecessões como é!

# 1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117


class Cadastro():
    def __init__(self, link):
        arquivo = open(link,'r')
        self.lista_cadastro = []
        for linha in arquivo:
            linha = linha.strip()
            lista_linha = linha.split(';')
            dict_cadastro = {'codigo':lista_linha[0],'nome':lista_linha[1],'idade':lista_linha[2],'sexo':lista_linha[3],'email':lista_linha[4],'telefone':lista_linha[5]}
            self.lista_cadastro.append(dict_cadastro)
        arquivo.close()
    
    def ver_lista_dict(self):
        for linha in self.lista_cadastro:
            print(linha)

    def salvar(self):
        # 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
        arquivo = open('Aulas/Aula23/exercicios/cadastro_atualizado.txt','w')
        for linha in self.lista_cadastro:
            arquivo.write(f"{linha['codigo']};{linha['nome']};{linha['idade']};{linha['sexo']};{linha['email']};{linha['telefone']}\n")
        arquivo.close

    def cadastrar_cliente(self,nome,idade,sexo,email,telefone):
        # 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode se repetir.
        dict_cadastro = {
            'codigo':str(len(self.lista_cadastro)+1),
            'nome':nome,
            'idade':idade,
            'sexo':sexo,
            'email':email,
            'telefone':telefone
            }
        self.lista_cadastro.append(dict_cadastro)
        self.salvar()
    
    def consulta_cliente(self, cod):
        # 3) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
        for linha in self.lista_cadastro:
            if cod == linha['codigo']:
                print(linha)
    
    def atualizar_cadastro(self, cod):
        # 4) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente. Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
        for linha in self.lista_cadastro:
            if cod == linha['codigo']:
                print(linha)
                linha['codigo']=cod
                linha['nome']=input('Nome: ')
                linha['idade']=input('Idade: ')
                linha['sexo']=input('Sexo: ')
                linha['email']=input('Email: ')
                linha['telefone']=input('Telefone: ')
        self.salvar()
    



link = ('Aulas/Aula23/exercicios/cadastro2.txt')
p = Cadastro(link)


nome = input('Nome: ')
idade = input('Idade: ')
sexo = input('Sexo: ')
email = input('Email: ')
telefone = input('Telefone: ')

p.cadastrar_cliente(nome,idade,sexo,email,telefone)
p.ver_lista_dict()

cod = input('Codigo cliente: ')
p.atualizar_cadastro(cod)
p.consulta_cliente(cod)