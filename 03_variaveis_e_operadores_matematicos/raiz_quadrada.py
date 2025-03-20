def raiz_quadrada(valor):
    return valor ** (1/2)

def test():
    assert raiz_quadrada(9) == 3
    assert raiz_quadrada(16) == 4
    assert raiz_quadrada(25) == 5

print (raiz_quadrada(9))