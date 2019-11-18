# Aula 8 - 18/11/2019
# Tuplas

# Criação Tupla
numeros = [0,1,2,3] # lista
usuario = {'chave':'valor', 'passwd':123456} # dicionario

pessoa=('victor','simão',0,45.5,numeros) # tupla

print(f'{numeros}\n{usuario}\n{pessoa}\n')

lista_pessoa=[]

lista_pessoa.append(pessoa) # Adicionando tupla dentro da lista

print(f'Elemento da lista na tupla: {pessoa[4][1]}') # Exibindo elemento especifico da lista dentro da tupla

