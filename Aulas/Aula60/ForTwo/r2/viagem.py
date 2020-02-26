from Aulas.Aula60.ForTwo.r2.embarque import embarque
from Aulas.Aula60.ForTwo.r2.desembarque import desembarque

from Aulas.Aula60.ForTwo.r2.terminal import Terminal
from Aulas.Aula60.ForTwo.r2.aviao import Aviao
from Aulas.Aula60.ForTwo.r2.local import Local
from Aulas.Aula60.ForTwo.r2.fortwo import Fortwo

# terminal = {'descricao':'terminal', 'pessoas': ['piloto','oficial1','oficial2','chefe de serviço','comissário1','comissário2','policial','presidiario']}
# aviao = { 'descricao':'aviao', 'pessoas': [] }

# def viagem(motorista:str, passageiro:str, saida:dict, chegada:dict):
#     fortwo = embarque(motorista, passageiro, saida)
#     print(f"Saindo do {saida['descricao']}")
#     print('Iniciando a viagem...')
#     print(f"Chegando no {chegada['descricao']}")
#     print('Finalizando a viagem ...')
#     # alto acoplamento
#     desembarque(fortwo, chegada)
#     print(saida)
#     print(chegada)

def viagem2(pessoa1, pessoa2, origem:Local, destino:Local):
    fortwo = Fortwo()
    if origem.saida(pessoa2):
        if origem.saida(pessoa1):
            if fortwo.set_motorista(pessoa1):
                if fortwo.set_passageiro(pessoa2):
                    fortwo.viagem(origem, destino)
                    if destino.entrada(pessoa2):
                        if not destino.entrada(pessoa1):
                            print('Não permitido6')
                    else:
                        print('Não permitido5')
                else:
                    print('Não permitido4')
            else:
                print('Não permitido3')
        else:
            print('Não permitido2')
    else:
        print('Não permitido1')
    print(f'origem: {origem.get_pessoas()}')
    print(f'destino: {destino.get_pessoas()}')

terminal = Terminal()
aviao = Aviao()

viagem2('policial','presidiário', terminal, aviao)
viagem2('policial','', aviao, terminal)
viagem2('piloto','policial', terminal, aviao)
viagem2('piloto','', aviao, terminal)
viagem2('piloto','oficial1', terminal, aviao)
viagem2('piloto','', aviao, terminal)
viagem2('piloto','oficial2', terminal, aviao)
viagem2('piloto','', aviao, terminal)
viagem2('chefe de serviço','piloto', terminal, aviao)
viagem2('chefe de serviço','', aviao, terminal)
viagem2('chefe de serviço','comissário1', terminal, aviao)
viagem2('chefe de serviço','', aviao, terminal)
viagem2('chefe de serviço','comissário2', terminal, aviao)