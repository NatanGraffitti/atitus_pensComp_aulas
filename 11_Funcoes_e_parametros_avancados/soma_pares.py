def soma_pares(numeros: list, alvo: int) -> bool: 
        for lista in numeros:
        x = lista
        for i in numeros:
            if i + x == alvo:
                return True
            else:
                pass
    return False

def test():
        assert soma_pares([1, 2], 4)
        assert not soma_pares([8], 1)
        assert not soma_pares([8], 10)
        assert soma_pares([3, 4, 6], 9)
        assert soma_pares([3, 4, 6], 7)
