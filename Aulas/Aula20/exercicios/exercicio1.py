# Aula 20 - 05-12-2019
# Lista com for e metodos

# Com esta lista:

lista = [
         ['codigo','produto','valor','quantidade'],
         [1,'Cevada',15.00,10],
         [2,'Lupulo',150.50,200],
         [3,'Malte',57.80,5000],
         [4,'Levedura 1',10.65,500],
         [5,'Extrato de Levedura',15.00,60],
         [6,'Levedura 2',15.50,87]
        ]

# 2.1 - Faça uma função que pegue esta lista e retorne uma lista com biblioteca.

# 2.2 - Faça outra função para consultar o preço através do código passado
# por parametro. Esta função deve printar o nome do produto, a quantidade
# e o preço.
# Execute esta função dentro do while e quando digitar qualquer código que 
# não tenha produto cadastrado o programa se encerra.
#

def dicionario(produtos, cabe):
        # cabe = ['codigo','produto','valor','quantidade']
       
       
        # produtos =
        # [1,'Cevada',15.00,10],
        # [2,'Lupulo',150.50,200],
        # [3,'Malte',57.80,5000],
        # [4,'Levedura 1',10.65,500],
        # [5,'Extrato de Levedura',15.00,60],
        # [6,'Levedura 2',15.50,87]


        lista_dicionario = []
        

        for linha in produtos:
                
                # linha
                # [1,'Cevada',15.00,10]
              
               
                dicionario2 = {}

                for b in range(4):
                        # cabe = ['codigo','produto','valor','quantidade']
                        # linha = [1,'Cevada',15.00,10],

                        # 0
                        dicionario2[cabe[b]] = linha[b]
                
                lista_dicionario.append(dicionario2)
        return lista_dicionario



cabe = lista[0]
produtos = lista[1:]

resultado = dicionario(produtos, cabe)

def consulta(resultado):
        cod = int(input('Digite o codigo: '))
        for linha in resultado:
                if linha['codigo'] == cod:
                        cont = 1
                        for i in linha:
                                if cont < len(cabe):
                                        print(f'{cabe[cont]}: {linha[cabe[cont]]}')
                                        cont += 1


        return cod

cod = 1
while cod > 0 and cod < 7:
        cod = consulta(resultado)
