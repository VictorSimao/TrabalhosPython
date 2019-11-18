#--- Exercicio 5  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia o salário de uma pessoa
#--- Use o método 50-20-10-20 - https://www.jaseimevirar.com/blog/como-voce-organiza-seu-orcamento-mensal/
#--- Informe os percentuais e valores que a pessoa deve utilizar em cada categoria
#--- Deve ser utilizado a função format e os caracteres de tabulação e quebra de linha para cada categoria

salario=float(input('Salario: '))

print('\n'*100)

print('METODO 50 - 20 - 10 - 20')
print(f'Gastos:{salario*0.5} reais\nLongo prazo:{salario*0.2} reais\nCurto Prazo:{salario*0.1} reais\nLivre:{salario*0.2} reais')