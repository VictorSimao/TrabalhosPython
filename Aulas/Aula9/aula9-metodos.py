# Aula 9 - 19-11-2019
# Metodo

from calculo_imposto import calculo_inss, calculo_irff

salario = float(input('Salario: '))

inss = calculo_inss(salario)
irrf = calculo_irff(salario, inss)


salario_liquido = salario - inss - irrf

print(f'Salario: {salario} INSS: {inss} IRRF: {irrf:.2f} Salario Liquido: {salario_liquido:.2f}')