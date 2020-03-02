
def solution(N, A):
    lista = [0] * N

    for numero in A:
        if numero <= N:
            lista[numero-1] += 1
        elif numero > N:
            maior = max(lista)
            lista = [maior] * N
    return lista

# def solution(N, A):
#     lista = [0] * N
#     for numero in A:
#         if numero <= N:
#             lista[numero-1] += 1
#         else:
#             maior = max(lista)
#             lista = [maior] * N
#     return lista

A = [3,4,4,6,1,4,4]
N = 5
print(solution(N, A))
assert solution(N, A) == [3,2,2,4,2]