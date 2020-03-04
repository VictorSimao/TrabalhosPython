
def solution(A):
    if max(A) < 1:
        return 1

    for numero in range(1, max(A) + 2):
        if numero not in A:
            return numero


A = [1, 3, 6, 4, 1, 2]

print(solution(A))

A = [1,2,3]

print(solution(A))