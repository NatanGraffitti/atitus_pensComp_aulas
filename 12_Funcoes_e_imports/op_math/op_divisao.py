def divisao(a: int, b: int) -> int | None:
    if b == 0:
        return None  # divisão por zero não 
    negativo = (a < 0) != (b < 0) 

    a = abs(a)
    b = abs(b)
    
    quociente = 0
    while a >= b:
        a -= b
        quociente += 1  
    return -quociente if negativo else quociente

assert divisao(-10, 2) == -5
assert divisao(10, -2) == -5
assert divisao(10, 2) == 5
assert divisao(10, 0) is None
