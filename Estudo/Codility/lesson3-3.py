
def solution(A):
    left = A[0]
    right = sum(A[1:])
    dif = abs(left - right)

    for i in range(1, len(A)):
        dif_2 = abs(left - right)
        if dif_2 < dif:
            dif = dif_2
        left += A[i]
        right -= A[i]
    return dif

A = [3,1,2,4,3]

print(solution(A))


