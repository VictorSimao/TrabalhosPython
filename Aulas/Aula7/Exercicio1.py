# Exercicio 1 - Dicionario
# Escreva programa que leia os dados de cerveja
# Cerveja: Marca, Tipo, IBU(amargor), Volume, ABV(teor alcoolico), EBC(cor)
# Crie um dicionario para armazenar os dados
# Imprima os dados do dicionario (não dicionario completo)


marca= input('Digite a marca da cerveja: ')
tipo= input('Digite o tipo da cerveja: ')
ibu= input('Digite a IBU da cerveja: ')
volume= input('Digite o volume da cerveja: ')
abv= input('Digite o ABV da cerveja: ')
ebc= input('Digite o EBC da cerveja: ')

cerva = {'Marca':marca,'Tipo':tipo,'IBU':ibu,'Volume':volume,'ABV':abv,'EBC':ebc}

print(f"Marca:{cerva['Marca']} - Tipo:{cerva['Tipo']} - IBU:{cerva['IBU']} - Volume{cerva['Volume']} - ABV:{cerva['ABV']} - EBC:{cerva['EBC']}")
print(cerva)