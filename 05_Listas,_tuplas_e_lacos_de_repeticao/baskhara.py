def baskhara(a, b, c):
    delta = b**2 - 4 * a * c  # Calcula o delta

    if delta < 0:
        return "Sem raízes reais"
    elif delta == 0:
        x = -b / (2 * a)
        return (x, x)
    else:
        raiz_delta = raiz_quadrada(delta)  
        x1 = (-b + raiz_delta) / (2 * a)  # Calcula a primeira raiz
        x2 = (-b - raiz_delta) / (2 * a)  # Calcula a segunda raiz
        return (x1, x2)  # Retorna as duas raízes


def test():
    assert baskhara(1, -3, 2) == [2, 1]
    assert baskhara(2, 3, -2) == [-2, 0.5]
    assert baskhara(1, -5, 6) == [2, 3]
    assert baskhara(1, -7, 10) == [2, 5]
    
    assert baskhara(1, 2, 3) is None
    assert baskhara(1, 0, 0) == 0


baskhara (2, 3, -2)
