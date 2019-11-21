

def iss(valor_servico):
    return valor_servico*0.02

def rentabilidade(investimento, taxa, prazo):
    taxa = taxa / 100
    total = investimento*(1+taxa)**prazo
    return total

def porc(investimento, total):
    porc = float((total*100)/investimento)-100
    return porc

def selic25(valor_inicial):
    valor_final = valor_inicial
    for i in range(0,64):
        valor_final += (valor_inicial * (0.0502/12))
    return valor_final
