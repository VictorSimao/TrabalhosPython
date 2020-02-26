
def binarygap(numero):
    numero = bin(numero)
    valida_gap = False
    maior_gap = 0
    gap = 0
    for i in numero:
        if i == "1":
            if maior_gap < gap:
                maior_gap = gap
            gap = 0
            valida_gap = True
        elif i == "0" and valida_gap == True:
            gap += 1
    return maior_gap

assert binarygap(20) == 1
assert binarygap(15) == 0
assert binarygap(32) == 0
assert binarygap(529) == 4
assert binarygap(850) == 2
assert binarygap(1041) == 5
assert binarygap(1256) == 2
assert binarygap(10119) == 4




