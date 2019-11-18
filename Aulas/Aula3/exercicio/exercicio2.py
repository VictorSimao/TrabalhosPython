#--- Exercicio 2  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um cliente
#--- Cliente: Nome, Sobrenome, ano de nascimento
#--- Exiba uma mensagem de boas vindas para o cliente
#--- Exiba um menu: Produtos alcoolicos e Produtos não alcoolicos, Sair
#--- Caso o cliente seja menor de idade o item 'produtos alcoolicos' não deve ser exibido
#--- Leia a opção digitada e crie uma tela para cada opção

nome=input('Nome: ')
sobrenome=input('Sobrenome: ')
idade=2019-int(input('Ano de nascimento: '))

print("\n"*100)
print('')
print(f'{nome} {sobrenome}, {idade} anos')
print('Bem Vindo - Sistema de Compra de Bebidas')
print('Proibido venda de bebida alcoolicas para menor')
print('')
if idade>17:
    print('='*10, 'MENU', '='*10)
    menu=input('1 - Não Alcoolicos\n2 - Alcoolicos\nx - Sair\n')
    print('='*26)
else:
    print('='*10, 'MENU', '='*10)
    menu=input('1 - Não Alcoolicos\nx - Sair')
    print('='*26)

if menu == '1':
    print('='*10,'Não Alcoolicos','='*10)
    print('1 - Refrigerantes')
    print('2 - Energeticos')
    print('3 - Sucos')
elif menu == '2' and idade>17:
    print('='*10, 'Alcoolicos', '='*10)
    print('1 - Cerveja')
    print('2 - Destilados')
    print('3 - Vinho')
elif menu == 'x':
    pass
else:
    print('Opção invalida')