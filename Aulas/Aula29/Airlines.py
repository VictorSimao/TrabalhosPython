
class Fortwo:
    def __init__(self):
        self.tripT = ['piloto','oficial_1','oficial_2']
        self.tripC = ['chefe','comissario_1','comissario_2']
        self.tripP = ['policial','prisioneiro']
        self.carro = []
        self.aviao = []
        self.terminal = self.tripC + self.tripC + self.tripP
        
    def imprimir(self):
        print(f'Terminal: {self.terminal}')
        print(f'Carro: {self.carro}')
        print(f'Avião: {self.aviao}')

    def ida(self):
        if not self.carro:
            self.carro.append()

# trip_tecnica = ['piloto','oficial_1','oficial_2']
# trip_cabine = ['chefe','comissario_1','comissario_2']
# trip_passageiro = ['policial','prisioneiro']

p = Fortwo()
p.ida()



    