def calcular_juros_compostos(principal, taxa, tempo):
    pass


def calcular_juros_compostos_recursivo(principal, taxa, tempo):
    if tempo == 0:
        return principal
    return calcular_juros_compostos_recursivo(principal, taxa, tempo - 1) * (1 + taxa)

principal = 1000     #principal inicial
taxa = 0.05          #5/100 taxa em decimal
tempo = 5            #5 anos

montante_total = calcular_juros_compostos(principal, taxa, tempo)
print(f"Montante total após {tempo} anos: R$ {montante total}")

montante_total = calcular_juros_compostos_recursivo(principal, taxa, tempo)
print(f"Montante total após {tempo} anos: R$ {montante total}")

def test():
    assert calcular_juros_compostos(1000, 0.05, 5) == 1276.2815625000003
    assert calcular_juros_compostos(1000, 0.05, 10) == 1628.894626777442
    assert calcular_juros_compostos(1000, 0.05, 0) == 1000
    
    assert calcular_juros_compostos_recursivo(1000, 0.05, 5) == 1276.2815625000003
    assert calcular_juros_compostos_recursivo(1000, 0.05, 10) == 1628.894626777442
    assert calcular_juros_compostos_recursivo(1000, 0.05, 0) == 1000
