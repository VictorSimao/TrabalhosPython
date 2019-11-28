# Marca, Tipo, Teor

def salvar_cerveja(cerveja):
    arquivo = open('aula15.txt','a')
    arquivo.write(f"{cerveja['nome']};{cerveja['tipo']};{cerveja['teor']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('aula15.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        marca = {'nome':lista_linha[0],'tipo':lista_linha[1],'teor':lista_linha[2]}
        lista.append(marca)
    arquivo.close()
    return lista

nome = input('Marca: ')
tipo = input('Tipo: ')
teor = float(input('Teor: '))
cerveja = {'nome':nome,'tipo':tipo,'teor':teor}
salvar_cerveja(cerveja)

for cerva in ler():
    print(f"Marca: {cerva['nome']} - Tipo: {cerva['tipo']} - Teor: {cerva['teor']}")

