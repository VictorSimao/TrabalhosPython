
def solution(A):
    if A:
        for numero in range(1,max(A)):
            if A.count(numero) == 0:
                return numero
        return max(A)+1
    return 1

# def solution(A):
#     if A:
#         A.sort()
#         print(A)
#         for numero in range(0,len(A),2):
#             if A[numero] != A[-1]:
#                 pos = numero + 1
#                 if A[numero] != A[pos]-1:
#                     return A[numero]+1
#             elif len(A) == 1 and A[0] == 1:
#                 return 2
#             elif len(A) == A[0] == 2:
#                 return 1
#         return max(A)+1

A= [2,3,1,5]
assert solution(A) == 4

A= [2,3,1,4,5]
assert solution(A) == 6

A= [1]
assert solution(A) == 2

A= [2]
assert solution(A) == 1

A= [2,3,1,4]
assert solution(A) == 5