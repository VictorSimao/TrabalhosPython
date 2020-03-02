
def solution(A):
    set(A)
    print(A)
    if 0 in A:
        A.remove(0)
    if len(A) == max(A):
        return 1
    return 0

A = [0,1,5,6,8,4,3,2,7]
assert solution(A) == 1

A = [1,2]
assert solution(A) == 1

A = [1,3]
assert solution(A) == 0

A = [1,1]
assert solution(A) == 0