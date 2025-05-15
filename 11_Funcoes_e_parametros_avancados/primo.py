def eh_primo(numero: int) -> bool:
    if numero <= 1:
        return False

    for i in range(2, numero): #[2 ... 6] -> lista de dois ate numero sem incluir numero
        if numero % i ==0:
            return False

    return True

def test():
    assert not eh_primo(-1)
    assert not eh_primo(0)
    assert not eh_primo(1)
    assert eh_primo(2)
    assert eh_primo(3)
    assert not eh_primo(4)
    assert eh_primo(5)
