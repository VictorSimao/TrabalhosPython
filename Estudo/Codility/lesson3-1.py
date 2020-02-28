
def solution(X:int, Y:int, D:int):
    resultado = Y - X
    if resultado > 0:
        resultado = resultado / D
        if resultado % 1 != 0:
            resultado += 1
    return int(resultado)


X = 10
Y = 85
D = 30
assert solution(X, Y, D) == 3

X = 10
Y = 110
D = 30
assert solution(X, Y, D) == 4