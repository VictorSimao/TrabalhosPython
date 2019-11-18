#--- Exercicio 4  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que realize a autenticação de usuário
#--- Crie duas variáveis para conter o usuário e senha padrão do sistema
#--- Leia o usuário e senha informados pelo usuário via função input()
#--- Valide se usuário e senha estão corretos
#--- Caso o usuário e senha estejam corretos informe com mensagem de boas vindas
#--- Caso o usuário e senha estejam incorretos informe com mensagem de falha de login

user='Victor'
senha='123'

aut_user=input('Usuario: ')
aut_senha=input('Senha: ')

print('\n'*100)
if aut_user == user and aut_senha == senha:
    print('Bem Vindo a Matrix')
else:
    print('Falha de Login')