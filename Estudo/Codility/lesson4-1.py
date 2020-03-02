
# def solution(X, A):
#     if not A:
#         return -1
#
#     lista = []
#     for numero in range(1, X+1):
#         if numero not in A:
#             return -1
#         if A.index(numero) >= X:
#             lista.append(A.index(numero))
#     return max(lista)

def solution(X, A):
    set1 = set()
    for i, j in enumerate(A):
        set1.add(j)
        if len(set1) == X:
            return i
    return -1

A = [3,1,2,3,4,3]
X = 4
print(solution(X, A))
assert solution(X, A) == 4