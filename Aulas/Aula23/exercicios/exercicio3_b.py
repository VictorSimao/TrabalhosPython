class Cadastro:
    def __init__(self):
        self.lista=[]
        self.ler()

    def ler(self):
        try:

            arquivo = open('Aulas/Aula23/exercicios/cadastro_atualizado.txt','r')
            for pessoa in arquivo:
                pessoa = pessoa.strip().split(';')

                dic = {'codigo':pessoa[0],'nome':pessoa[1],'idade':pessoa[2],'sexo':pessoa[3],'email':pessoa[4],'telefone':pessoa[5]}
                self.lista.append(dic)

        finally:
            arquivo.close()
    
    def salvar(self):
        try:
            arquivo = open('Aulas/Aula23/exercicios/cadastro_atualizado.txt','w')
            for pessoa in self.lista:
                texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['idade']};{pessoa['sexo']};{pessoa['email']};{pessoa['telefone']}"
                arquivo.write(texto)
        finally:
            arquivo.close()

    def cadastrar(self):
        nome = input('Nome: ')
        idade = input('Idade: ')
        sexo = input('Sexo: ')
        email = input('Email: ')
        telefone = input('Telefone: ')

        dict_cadastro = {
            'codigo':str(len(self.lista_cadastro)+1),
            'nome':nome,
            'idade':idade,
            'sexo':sexo,
            'email':email,
            'telefone':telefone
            }
        self.lista.append(dict_cadastro) 
    
    def consulta(self,codigo):
        for pessoa in self.lista:
            if int(pessoa['codigo']) == codigo:
                print(pessoa)
                break

    def atualizar(self):
        pass

p = Cadastro()

p.consulta(501)