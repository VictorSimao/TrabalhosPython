# A[0] = 3
# A[1] = 1
# A[2] = 2
# A[3] = 4
# A[4] = 3

# def solution(A):
#     left = A[0]
#     right = sum(A[1::])
#     diff = abs(left - right)
#
#     for p in range(1, len(A)):
#         ldiff = abs(left - right)
#         if ldiff < diff:
#             diff = ldiff
#         left += A[p]
#         right -= A[p]
#
#     return diff

A = [3,1,2,4,3]

print(solution(A))


def solution(A):
    resto = []
    left = 0
    right = sum(A)

    for i in A:
        left += i
        right -= i
        if left >= right:
            resto.append(left - right)
        elif right > left:
            resto.append(right - left)
    return min(resto)