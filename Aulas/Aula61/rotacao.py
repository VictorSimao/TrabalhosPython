

def rotacao(A:list, K:int):
    for i in range(K):
        if A:
            lista_copia = A.copy()
            for i in range(len(A)-1):
                lista_copia[i + 1] = A[i]
            lista_copia[0] = A[-1]
            A = lista_copia
    return A


A = [3, 8, 9, 7, 6]
K = 6
assert rotacao(A, K) == [6, 3, 8, 9, 7]

A = [3, 8, 9, 7, 6]
K = 3
assert rotacao(A, K) == [9, 7, 6, 3, 8]

A = [1, 2, 3, 4]
K = 4
assert rotacao(A, K) == [1, 2, 3, 4]

A = []
K = 1
assert rotacao(A, K) == []

