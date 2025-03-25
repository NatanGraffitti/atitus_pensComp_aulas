def eh_positivo(numero):
    if numero >= 0:
        return True
    else:
        return False
#   poderia ser usado também: def eh_positivo(valor):
#                                  return valor > 0

def eh_negativo(numero):
    if numero < 0:
        return True
    else:
        return False    

def test():
    assert eh_positivo(1)
    assert eh_positivo(2)
    assert eh_positivo(10)
    assert not eh_positivo(0)
    assert not eh_positivo(-1)
    assert not eh_positivo(-10)

    assert eh_negativo(-1)
    assert eh_negativo(-2)
    assert eh_negativo(-10)
    assert not eh_negativo(0)
    assert not eh_negativo(1)
    assert not eh_negativo(10)

print (eh_positivo(10))
print (eh_negativo(10))