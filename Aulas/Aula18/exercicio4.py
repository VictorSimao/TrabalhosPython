# Aula 18 - 03-11-2019

# interação de lista com o for

# Usando o comando for vamos fazer uma interação de varialvel tipo coleção. A interação é (simplificadamente) 
# percorer toda a variavel e isolar seu valores.

def tupla_lista():
    for a in range(4):
        dic_cerveja = {'Marca':cerveja[a+1][0],'Tipo':cerveja[a+1][1],'IBU':cerveja[a+1][2],'Preço':cerveja[a+1][3]}
        lista_dic.append(dic_cerveja)
    return lista_dic

# 1.1 Com a seguinte lista, use o for para interar esta tupla  e apresentar (usando o f-string) O nome da cerveja, 
# tipo da cerveja, o IBU da cerveja e o preço dela.

cerveja = (('marca', 'tipo', 'ibu','preço'),
           ('Skol','IPA','ultra-leve',3.50),
           ('Brahma','lager','leve/media',3.45),
           ('Kaiser','Americam Larger','leve',2.35),
           ('Sol','larger mão','agua',1.19)
          )

i = 0
for a in range(4):
    j = 0
    for b in range(4):
        print(f'{cerveja[0][j]}:{cerveja[i+1][j]}')
        j += 1
    i += 1

# 1.2 Crie uma função que receba esta tupla e devolva uma lista com um dicionários referenciando cada uma destas 
# cervejas.

lista_dic = []
dic_cerveja = {}
lista_dic = tupla_lista()

for linha in lista_dic:
    print(linha)