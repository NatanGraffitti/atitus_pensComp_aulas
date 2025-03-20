def area(largura, altura):
    return (largura * altura)


def perimetro(largura, altura):
    return (largura + altura) * 2


def hipotenusa(largura, altura):
    return ((largura ** 2) + (altura**2)) ** (1/2)


def test():
    assert area(5, 5) == 25
    assert area(0, 5) == 0
    assert area(10, 5) == 50

    assert perimetro(2, 3) == 10
    assert perimetro(5, 5) == 20
    assert perimetro(10, 5) == 30

    assert hipotenusa(4, 3) == 5
    assert hipotenusa(6, 8) == 10
    assert hipotenusa(5, 12) == 13

print (area(10, 5))
print (perimetro(10, 5))
print (hipotenusa(6, 8))