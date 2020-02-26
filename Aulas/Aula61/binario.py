

def binarygap(numero):
    numero = bin(numero)
    maior_gap = 0
    x = 0
    for i in numero:
        if i == "1":
            x = numero.index(i) + 1
            gap = 0
            while numero[x] < "1":
                gap += 1
                if len(numero) > x-1:
                    x += 1
            if gap > maior_gap:
                maior_gap = gap
    print(maior_gap)

binarygap(32)





