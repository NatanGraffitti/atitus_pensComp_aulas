def eh_primo(numero: int) -> bool: 
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def lista_primos(num: int) -> list:
    resultado = []
    for x in range(num + 1):
        if eh_primo(x):
            resultado.append(x)
    return resultado

def test(): 
    assert lista_primos(10) == [2, 3, 5, 7]
    assert lista_primos(13) == [2, 3, 5, 7, 11, 13]
    assert lista_primos(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

print([2, 3, 5, 7])
print([2, 3, 5, 7, 11, 13])
print([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
print("Pronto")
