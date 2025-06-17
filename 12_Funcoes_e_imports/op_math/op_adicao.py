def adicao(valor1: int, valor2: int) -> int:
    if valor2 == 0:
        return valor1
    elif valor2 > 0:
        for _ in range(valor2):
            valor1 += 1
        return valor1
    else:  # valor2 negativo
        for _ in range(-valor2):
            valor1 -= 1
        return valor1

assert adicao(1, 2) == 3
assert adicao(1, 0) == 1
assert adicao(-1, -2) == -3
