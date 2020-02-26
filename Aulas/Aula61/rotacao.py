

def rotacao(a:list, k:int):
    for i in range(k):
        lista_copia = a.copy()
        for i in range(len(a)-1):
            lista_copia[i+1] = a[i]
        lista_copia[0] = a[-1]
        a = lista_copia
    return a


A = [3, 8, 9, 7, 6]
K = 6
assert rotacao(A, K) == [6, 3, 8, 9, 7]

A = [3, 8, 9, 7, 6]
K = 3
assert rotacao(A, K) == [9, 7, 6, 3, 8]

A = [1, 2, 3, 4]
K = 4
assert rotacao(A, K) == [1, 2, 3, 4]

