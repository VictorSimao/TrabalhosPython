# Aula 21

# Crie uma classe cliente:

# 1) Atributos: Codigo, CPF, Nome, Idade, Sexo

# 2) Metodos: Receber Salario, Comprar, Pagar Divida

# 3) Estado: Dinheiro na Carteira, Divida, Bens

class Cliente:
    def __init__ (self, codigo, cpf, nome, idade, sexo):
        self.codigo = codigo
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

        self.divida = 0
        self.carteira = 0
        self.bens = 0
    
    def receber_salario(self, dinheiro):
        self.carteira += dinheiro
    
    def comprar(self, dinheiro):
        self.bens += dinheiro
        self.carteira = self. carteira - dinheiro
        if self.carteira < 0:
            self.divida = (self.divida - self.carteira)*1
            self.carteira = 0
    
    def pagar_divida(self):
        if self.divida > 0:
            if self.carteira >= self.divida:
                self.carteira -= self.divida
                self.divida = 0
            elif self.carteira < self.divida:
                print('Não tem dinheiro suficiente na carteira para pagar a divida')
        else:
            print('Não tem divida!')

p = Cliente(1,'12345678900','Victor',31,'m')

p.receber_salario(1000)
print('Recebeu 1000 reais')
p.comprar(1200)
print('Comprou 1200 reais de bens')

print('\n')
print(f'Nome {p.nome}')
print(f'Bens {p.bens}')
print(f'Carteira {p.carteira}')
print(f'Divida {p.divida}')
print('\n')

p.receber_salario(1200)
print('Recebeu 1200 reais de salario')
p.pagar_divida()
print('Pagar a divida se houver divida e dinheiro')

print('\n')
print(f'Nome {p.nome}')
print(f'Bens {p.bens}')
print(f'Carteira {p.carteira}')
print(f'Divida {p.divida}')
print('\n')
