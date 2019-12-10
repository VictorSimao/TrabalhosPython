# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)



class Cliente():
    def __init__(self,dadobruto):
        self.dado_bruto = dadobruto
        # self.codigo = None
        # self.nome = None
        # self.idade = None
        # self.genero = None
        # self.email = None
        # self.telefone = None

    def entrada_valor(self):
        lista_dado = self.dado_bruto.split(';')
        self.codigo = int(lista_dado[0])
        self.nome = lista_dado[1]
        self.idade = int(lista_dado[2])
        self.genero = lista_dado[3]
        self.email = lista_dado[4]
        self.telefone = lista_dado[5]

p = Cliente(dadobruto)
p.entrada_valor()

# print(f'Dado bruto: {p}')
print(f'Codigo: {p.codigo}')
print(f'Nome {p.nome}')
print(f'Idade {p.idade}')
print(f'Genero {p.genero}')
print(f'Email {p.email}')
print(f'Telefone {p.telefone}')