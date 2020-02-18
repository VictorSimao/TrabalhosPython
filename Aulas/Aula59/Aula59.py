#--- teste em sucuri

#--- verificacao se determina condicao é verdadeira
assert True
assert 10 == 10
assert 10 > 5
assert 'Volti' != 'Vini'

def soma(n1, n2):
    resultado = n1 + n2
    return resultado

def multiplicacao(n1, n2, n3=1):
    return n1 * n2 * n3

def checa_maioridade(idade):
    if idade >= 18:
        return True
    else:
        return False

assert checa_maioridade(18) == True
assert checa_maioridade(19) == True
assert checa_maioridade(17) == False

assert soma(5, 10) == 15
assert multiplicacao(2, 4, 6) == 48
assert multiplicacao(2,4) == 8

class Calc:
    def __init__(self, numero1, numero2):
        self.__n1 = numero1
        self.__n2 = numero2
        self.__resultado = 0

    def set_n1(self, valor):
        self.__n1 = valor
    def get_n1(self):
        return self.__n1

    def set_n2(self, valor):
        self.__n2 = valor
    def get_n2(self):
        return self.__n2

    def get_resultado(self):
        return self.__resultado

    def soma(self):
        self.__resultado = self.__n1 + self.__n2

    def sub(self):
        self.__resultado = self.__n1 - self.__n2

    def mult(self):
        self.__resultado = self.__n1 * self.__n2


c = Calc(10,20)
assert isinstance(c, Calc)
assert c.get_n1() == 10
assert c.get_n2() == 20

assert c.soma() == None
assert c.get_resultado() == 30

assert c.mult() == None
assert c.get_resultado() == 200

assert c.sub() == None
assert c.get_resultado() == -10

assert c.set_n1(5) == None
assert c.get_n1() == 5

assert c.set_n2(10) == None
assert c.get_n2() == 10


