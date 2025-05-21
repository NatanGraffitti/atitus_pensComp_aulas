def calcula_classe_social(salarios, salario_minimo):
    if not salarios:
        return None
    
    total_rendimento = sum(salarios)
    
    if total_rendimento <= salario_minimo:
        return "E"
    elif total_rendimento <= 3 * salario_minimo:
        return "D"
    elif total_rendimento <= 10 * salario_minimo:
        return "C"
    elif total_rendimento <= 20 * salario_minimo:
        return "B"
    else:
        return "A"
        
def test():
    assert calcula_classe_social([], 1000) is None
    assert calcula_classe_social([1000], 1000) == "E"
    assert calcula_classe_social([500], 1000) == "E"
    assert calcula_classe_social([1000, 0], 900) == "E"
    assert calcula_classe_social([1000], 900) == "D"
    assert calcula_classe_social([10000, 15000], 1000) == "B"
    assert calcula_classe_social([20000, 25000], 1000) == "A"
    assert calcula_classe_social([20000, 0, 0, 0, 0], 1000) == "C"

print(calcula_classe_social([1000], 15000))
