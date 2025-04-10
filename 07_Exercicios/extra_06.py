def valor_pgto(valor, forma_pgto):
    if forma_pgto == 1:
        return valor - (valor * (15 / 100))
    if forma_pgto == 2:
        return valor - (valor * (10 / 100))
    if forma_pgto == 3:
        return valor
    if forma_pgto == 4:
        return valor + (valor * (10 / 100))
    if forma_pagto not in [1, 2, 3, 4]:
        return "Opção inválida. Por favor, escolha uma das opções listadas.")

def test():
    assert valor_pgto(100, 1) == 85
    assert valor_pgto(100, 2) == 90
    assert valor_pgto(100, 3) == 100
    assert valor_pgto(100, 4) == 110
    assert isinstance(valor_pgto(100, 5), str)
