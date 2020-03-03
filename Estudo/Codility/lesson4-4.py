
def solution(A):
    if len(A) == max(A):
        set_1 = set(i for i in A)
        if len(set_1) == max(set_1):
            return 1
    return 0

A = [1,5,6,8,4,3,2,7]
assert solution(A) == 1, 'erro 1'

A = [1,2]
assert solution(A) == 1, 'erro 2'

A = [1,3]
assert solution(A) == 0, 'erro 3'

A = [1,1]
assert solution(A) == 0, 'erro 4'