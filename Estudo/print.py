# Aula Print - 18/11/2019

print(''' Texto
com quebra de
    linhas sem \n''')

nome= 'Victor' ' ' 'Simão'

print(nome)
print(nome.lower()) # todas letras em minusculo
print(nome.upper()) # todas letras em maiscula
print(nome.split(' ')) # separa onde vc indicar, no caso nos espaço em vazios
print(nome.split('i')) # separa onde vc indicar, no caso nos espaço com 'i'
print(nome.strip()) # remove  espaço vazios antes e depois

pessoa= [' ','Carinhoso','Atencioso','Querido']
print(pessoa)
print((' Nem ').join(pessoa)) # Adiciona o que for indicado a cada elemento da sequencia
print(pessoa[1:]) 
print(pessoa[:2])
print(pessoa[1:3])
print(pessoa.count('Carinhoso'.strip().capitalize()))

frase='Teste'
print(frase[2:])
print(frase[:3])
print(frase[1:3])

print(('a '.join(frase)))

