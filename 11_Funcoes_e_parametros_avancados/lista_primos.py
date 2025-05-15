numero = 7

def eh_primo(numero: int) -> bool:
    if numero <= 1:
        return False
        
    for i in range(2, numero): #[2 ... 6] -> lista de dois ate numero sem incluir numero 7
        if numero % i ==0:
            return False
    return True

def lista_primos(x: int) -> bool:
    if result = []
    for x in range(val + 1):
        if eh_primo(x):
            result.append(x)
    return result
    
resultado = lista_primos(100)
print(resultado)

def test():
    assert lista_primos(10) == [2, 3, 5, 7]
    assert lista_primos(13) == [2, 3, 5, 7, 11, 13]
    assert lista_primos(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
