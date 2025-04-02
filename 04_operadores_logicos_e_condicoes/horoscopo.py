def horoscopo(mes):  #função (def) com assinatura do método (horoscopo) e parâmetro (mes)
    if mes <= 0 or mes > 12:
        return ("Valor inválido")
    if mes > 0 and mes <= 3:
        return ("Você é do signo de Python")        
    if mes > 4 and mes <= 6:
        return ("Você é do signo de Java")
    if mes > 7 and mes <= 9:
        return ("Você é do signo de PHP")
    if mes > 10 and mes <= 12:
        return ("Você é do signo de TypeScript")   

def test():
    assert horoscopo(1) == "Python"
    assert horoscopo(3) == "Python"

    assert horoscopo(4) == "Java"
    assert horoscopo(6) == "Java"

    assert horoscopo(7) == "PHP"
    assert horoscopo(9) == "PHP"

    assert horoscopo(10) == "TypeScript"
    assert horoscopo(12) == "TypeScript"

    assert horoscopo(-1) is None
    assert horoscopo(0) is None
    assert horoscopo(13) is None
    
    
print (horoscopo(1))
