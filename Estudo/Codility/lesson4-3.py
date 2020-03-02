
def solution(A):
    print(max(A))
    if max(A) < 1:
        return 1

    for numero in range(1, max(A) + 2):
        if numero not in A:
            return numero


