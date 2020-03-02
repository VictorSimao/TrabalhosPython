
def solution(X, A):
    if not A:
        return -1

    lista = []
    for numero in range(1, X+1):
        if numero not in A:
            return -1
        lista.append(A.index(numero))
    return max(lista)

# def solution(X, A):
#     resultado = -1
#     if not A:
#         return -1
#
#     for numero in range(1, X+1):
#         if resultado < A.index(numero):
#             resultado = A.index(numero)
#
#     return resultado

A = [3,1,2,3,4,3]
X = 4
# print(solution(X, A))
assert solution(X, A) == 4