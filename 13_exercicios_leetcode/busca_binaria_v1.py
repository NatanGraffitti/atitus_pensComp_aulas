def busca_binaria(lista: list, valor: int) -> bool:
    esquerda, direita = 0, len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return True
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return False

assert busca_binaria([1, 3, 5, 7, 9, 11, 13, 15], 7)
assert not busca_binaria([1, 3, 5, 7, 9, 11, 13, 15], 8)
