
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
assert solution(A) == 2

A = [2,3,1,5]
assert solution(A) == 4

A = [2,3,1,4,5]
assert solution(A) == 6

A = []
assert solution(A) == 1

A = [1]
assert solution(A) == 2


A = [2,3,1,4]
assert solution(A) == 5