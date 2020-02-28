
# def solution(A):
#     for numero in range(1,1000000,2):
#         if A.count(numero) % 2 == 1:
#             return numero

# def solution(A):
#     for numero in A:
#         if A.count(numero) == 1:
#             return numero

def solution(A):
    A.sort()
    if len(A) == 1:
        numero = A[0]
        return numero
    for i in range(0,len(A),2):
        if i == len(A) - 1:
            return A[i]
        if A[i] != A[i + 1]:
            return A[i]

A = [3, 8, 3, 8, 5]
assert solution(A) == 5
A = [9, 3, 9, 3, 9, 7, 9]
assert solution(A) == 7
A = [9, 9, 9, 9, 9, 9, 11]
assert solution(A) == 11
A = [9]
assert solution(A) == 9
A = []
assert solution(A) == None
A = [201]
assert solution(A) == 201
A = [601]
assert solution(A) == 601
A = [2001]
assert solution(A) == 2001
A = [100003]
assert solution(A) == 100003
A = [999999]
assert solution(A) == 999999
