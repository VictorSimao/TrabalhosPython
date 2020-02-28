
def solution(A):
    if A:
        for numero in range(1,max(A)):
            if A.count(numero) == 0:
                return numero
        return max(A)+1

A= [2,3,1,5]
assert solution(A) == 4

A= []
assert solution(A) == None

A= [1]
assert solution(A) == 2

A= [2]
assert solution(A) == 1

A= [2,3,1,4]
assert solution(A) == 5