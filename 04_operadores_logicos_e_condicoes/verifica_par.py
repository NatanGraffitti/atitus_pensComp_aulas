def eh_par(valor):
    if valor % 2 == 0:
        return True
    else:
        return False    


def eh_impar(valor):
    return not eh_par(valor) #reaproveita a função eh_par e nega ele, invertendo o valor

def test():
    assert eh_par(0)
    assert eh_par(2)
    assert eh_par(4)

    assert not eh_par(1)
    assert not eh_par(3)

    assert eh_impar(1)
    assert eh_impar(3)
    assert eh_impar(5)

    assert not eh_impar(0)
    assert not eh_impar(2)

print (eh_par(5))
print (eh_impar(-2))