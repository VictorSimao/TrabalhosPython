# Aula 22 - 10-12-2019
# Classe

# Na I Feira de Cerveja de Ituroró que irá acontecer em 2020, a AMBEV irá colocar 2 conteiners 
# de atendimento automatizado, um para bebidas alcoolicas e outro de bebidas não alcoolicas.
# O sistema irá operar da seguinte forma: 
# - O cliente se cadastrará no caixa retirando um cartão com um qrcod.
# - O cliente poderá recarregar o cartão com um determinado valor em dinheiro.
# - Quando o cliente chega no conteiner, passará o cartão em um leitor de qrcode que irá liberar 
# uma torneira da bebida de sua preferência. 
# -  Cada bebida tem um valor por ml que conforme enche o copo, irá descontando em tempo real, do 
# cartão do cliente.
# - Se o acabar os créditos, a torneira fecha autométicamente
# - Para a bebida alcoolica, só poderá ser liberada caso o cliente tenha mais de 18 anos.


# 1) Crie uma classe cliente que possui como atributos: Nome, idade, telefone.
# A variável nome e telefone deve ser um string. A variável idade deve ser valor inteiro.
# O cliente deve ter R$ 100.00 de dinheiro como saldo no cartão.
# 2) Crie metodos para: adicionar saldo no cartão, descontar saldo do cartão e verificar saldo do cartão.
# 3) para descontar o saldo do cartão, deve-se entra com a quantidade de ml e o valor por ml da bebida.
# O metodo deve imprimir na tela a quantidade de bebida e o valor descontado. Caso o saldo do cliente não
# seja o suficiente, deve-se imprimir o valor descontado e o volume liberado de bebida.


# Bebidas: 
# Refrigerante R$ 0,01 /ml 
# Cerveja ipa  R$ 0,05 /ml 
# Cerveja ale  R$ 0,063 /ml 


class Cliente():
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

        self.saldo = 100.0
    
    def ver_saldo(self):
        print('########################')
        print(f'Seu saldo é R$ {self.saldo}')
        if self.saldo == 0:
            print('########################')
            print('Adicionar saldo!!!')

    def adicionar_saldo(self, valor):
        self.saldo += valor
        self.ver_saldo()
    
    def descontar_valor(self, ml, tipo):
        if tipo == 1:
            tipo = 0.01
        elif tipo == 2:
            tipo = 0.05
        elif tipo == 3:
            tipo = 0.063

        valor = ml * tipo
        if self.saldo >= valor:
            self.saldo -= valor
        elif self.saldo < valor:
            ml = self.saldo/tipo
            valor = ml * tipo
            self.saldo -= valor
        self.ver_saldo()
        print(f'Liberou {ml} ml!')

p = Cliente('Victor',31,'4799998888')

while True:
    print('########################')
    print(f'Cliente {p.nome}')
    print('########################')
    print('1 - Ver saldo!')
    print('2 - Aumentar saldo!')
    print('3 - Comprar bebida!')
    menu = int(input('Qual opção: '))
    if menu == 1:
        p.ver_saldo()
    elif menu == 2:
        print('########################')
        valor = float(input('Adicionar: '))
        p.adicionar_saldo(valor)
    elif menu == 3:
        print('########################')
        print('Qual você quer comprar')
        print('1 - Refrigerante, Valor 0.01/ml')
        print('2 - Cerveja IPA, Valor 0.05/ml')
        print('3 - Cerveja ALE, Valor 0.063/ml')
        tipo = int(input('Qual opção: '))
        ml = int(input('Quantos mls:  '))
        p.descontar_valor(ml, tipo)
