
# def solution(A):
#     if A:
#         for numero in range(1,max(A)):
#             if A.count(numero) == 0:
#                 return numero
#         return max(A)+1
#     return 1

# def solution(A):
#     A.sort()
#
#     if not A:
#         return 1
#
#     if 1 not in A:
#         return 1
#
#     if A[-1] == len(A):
#         return A[-1] + 1
#
#     inicio = 0
#     tamanho = len(A)
#     meio = 0
#     resultado = confereposicao(A, inicio, tamanho, meio)
#
#     return resultado + 1
#
# def confereposicao(A, inicio, tamanho, meio):
#     if tamanho <= 1:
#         return meio
#     else:
#         meio = (tamanho // 2) + inicio
#         if A[meio] == meio + 1:
#             return confereposicao(A, meio, tamanho - meio, meio)
#         elif A[meio] != meio + 1:
#             return confereposicao(A, inicio, meio - inicio, meio)


# def solution(A):
#     A.sort()
#
#     if not A:
#         return 1
#
#     if 1 not in A:
#         return 1
#
#     if A[-1] == len(A):
#         return A[-1] + 1
#
#     if len(A) % 2 == 0:
#         resultado = conf_par(A)
#     else:
#         resultado = conf_impar(A)
#     return resultado + 1
#
# def conf_par(lista:list):
#     meio = len(lista) // 2
#     if meio > 1:
#         if lista[meio] == lista[meio+1] - 1:
#             conf_par(lista[meio:])
#         if lista[meio] != lista[meio+1] - 1:
#             conf_par(lista[:meio])
#     else:
#         return lista[meio]
#
# def conf_impar(lista:list):
#     meio = len(lista) // 2 - 1
#     if meio > 1:
#         if lista[meio] == lista[meio+1] - 1:
#             conf_par(lista[meio:])
#         if lista[meio] != lista[meio+1] - 1:
#             conf_par(lista[:meio])
#     else:
#         return lista[meio]


def solution(A):
    A.sort()
    if 1 not in A:
        return 1

    for numero in range(0, len(A)-1):
        pos = numero + 1
        if A[numero] != A[pos]-1:
            return A[numero]+1
    return max(A)+1


A = [1,3]
print(solution(A))
assert solution(A) == 2

A = [2,3,1,5]
print(solution(A))
assert solution(A) == 4

A = [2,3,1,4,5]
print(solution(A))
assert solution(A) == 6

A = []
assert solution(A) == 1

A = [1]
assert solution(A) == 2


A = [2,3,1,4]
assert solution(A) == 5