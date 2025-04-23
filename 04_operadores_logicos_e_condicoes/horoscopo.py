def horoscopo(mes):  # função (def) com assinatura do método (horoscopo) e parâmetro (mes)
    if mes <= 0 or mes > 12:
        return ("Valor inválido")
    if 1 <= mes <= 3:
        return ("Você é do signo de Python")
    if 4 <= mes <= 6:
        return ("Você é do signo de Java")
    if 7 <= mes <= 9:
        return ("Você é do signo de PHP")
    if 10 <= mes <= 12:
        return ("Você é do signo de TypeScript")


def test():
    assert horoscopo(1) == "Você é do signo de Python"
    assert horoscopo(3) == "Você é do signo de Python"
    assert horoscopo(4) == "Você é do signo de Java"
    assert horoscopo(6) == "Você é do signo de Java"
    assert horoscopo(7) == "Você é do signo de PHP"
    assert horoscopo(9) == "Você é do signo de PHP"
    assert horoscopo(10) == "Você é do signo de TypeScript"
    assert horoscopo(12) == "Você é do signo de TypeScript"
    assert horoscopo(-1) == "Valor inválido"
    assert horoscopo(0) == "Valor inválido"
    assert horoscopo(13) == "Valor inválido"


print(horoscopo(1))
