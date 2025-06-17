def multiplicacao(a: int, b: int) -> int:
    resultado = 0
    negativo = (a < 0) != (b < 0)
    a_abs = abs(a)
    b_abs = abs(b)

    for _ in range(b_abs):
        resultado += a_abs

    return -resultado if negativo else resultado


assert multiplicacao(-10, 2) == -20
assert multiplicacao(10, -2) == -20
assert multiplicacao(10, 2) == 20
assert multiplicacao(10, 0) == 0
