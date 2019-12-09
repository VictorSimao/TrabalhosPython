# Aula 22 - 09/12/2019
# Class

# # 1 - Caracteristica de uma pessoa ?
# ###### Atributos ( variaveis )
# nome
# idade
# telefone
# sexo

# # 2 - O que a pessoa faz ?
# ###### Metodos (função/procedimento)
# respira
# dorme
# corre 
# bebe 
# come 
# multiplica 

# # 3 - Com a pessoa esta agora ?
# ###### Atributos de estado ( Variaveis )
# divida 
# cansada 
# viva 
# fome 
# sede 

class Pessoa:
    def __init__ (self, nome1, idade1, telefone1, sexo1):
        self.nome = nome1
        self.idade = idade1
        self.telefone = telefone1
        self.sexo = sexo1

        self.divida = None
        self.cansada = 'não'
        self.viva = True
        self.fome = 'não'
        self.sede = 'não'

    def respira(self):
        if self.viva == True:
            if respirar == True:
                self.viva = True
            else:
                self.vive = False

    def corre(self, distancia):
        if self.viva:
            if distancia < 100:
                self.cansada = 'pouco'
                self.sede = 'pouco'
                self.fome = 'pouco'
            elif distancia >= 100 and distancia < 200:
                self.cansada = 'medio'
                self.sede = 'medio'
                self.fome = 'medio'
            elif distancia >= 200:
                self.cansada = 'muito'
                self.sede = 'muito'
                self.fome = 'muito'

    def dorme(self):
        if self.viva:
            self.cansada = 'não'
            self.come()
            self.bebe()

    def bebe(self):
        if self.viva:
            self.sede = 'não'

    def come(self):
        if self.viva:
            self.fome = 'não'

    def multiplica(self):
        pass

p = Pessoa('Fulano', 18, '4799998888', 'm')

p.corre(300)
p.dorme()

print(f'Nome: {p.nome}')
print(f'Esta vivo? {p.viva}')
print(f'Esta com fome? {p.fome}')
print(f'Esta com sede? {p.sede}')
print(f'Esta cansado? {p.cansada}')