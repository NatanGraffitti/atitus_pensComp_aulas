def calcula_classe_social(salarios, salario_minimo):
    if len(salarios) == 0:  # Verifica se a lista de salários está vazia
        return None

    total_dinheiro = sum(salarios)
    total_pessoas = len(salarios)
    renda_por_pessoa = total_dinheiro / total_pessoas
    salarios_minimos_por_pessoa = renda_por_pessoa / salario_minimo

    if salarios_minimos_por_pessoa > 15:
        classe = "Classe A"
    elif salarios_minimos_por_pessoa >= 5:
        classe = "Classe B"
    elif salarios_minimos_por_pessoa >= 3:
        classe = "Classe C"
    elif salarios_minimos_por_pessoa >= 1:
        classe = "Classe D"
    else:
        classe = "Classe E"
    
    return classe

salarios_da_familia = [2000, 1500, 800, 500]
valor_salario_minimo = 1412.00  

classe_da_familia = calcula_classe_social(salarios_da_familia, valor_salario_minimo)
print("A família é da", classe_da_familia)

def test():
    assert calcula_classe_social([], 1000) is None  
    assert calcula_classe_social([1000], 1000) == "D"  
    assert calcula_classe_social([500], 1000) == "E"  
    assert calcula_classe_social([1000, 0], 900) == "E"  
    assert calcula_classe_social([1000], 900) == "D"  
    assert calcula_classe_social([10000, 15000], 1000) == "B"
    assert calcula_classe_social([20000, 25000], 1000) == "A"
    assert calcula_classe_social([20000, 0, 0, 0, 0], 1000) == "C"
