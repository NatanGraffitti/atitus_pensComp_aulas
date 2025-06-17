def negativo(x: int) -> int:
    return ~x + 1

def subtracao(valor1: int, valor2: int) -> int:
    return valor1 + negativo(valor2)

assert subtracao(-10, 2) == -12
assert subtracao(10, -2) == 12
assert subtracao(-10, -2) == -14
assert subtracao(10, 2) == 8
assert subtracao(10, 0) == 10
