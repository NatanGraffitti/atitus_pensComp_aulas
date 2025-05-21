def calcula_classe_social(salarios, salario_minimo): 
    if not salarios:
        return None  

    total_salarios = 0
    quantidade_salarios = 0
    for salario in salarios:
        total_salarios += salario
        quantidade_salarios += 1

    media = total_salarios / quantidade_salarios
    renda_em_salarios_minimos = media / salario_minimo

    if renda_em_salarios_minimos <= 1:
        return "E"
    elif renda_em_salarios_minimos <= 2:
        return "D"
    elif renda_em_salarios_minimos <= 4:
        return "C"
    elif renda_em_salarios_minimos <= 10:
        return "B"
    else:
        return "A"

salarios_input = input("Digite os salários separados por vírgula: ")
salarios = [float(s) for s in salarios_input.split(",")]  # Converte os salários para uma lista de floats

salario_minimo = float(input("Digite o valor do salário mínimo: "))

classe = calcula_classe_social(salarios, salario_minimo)

if classe:
    print(f"A classe social é: {classe}")
else:
    print("A lista de salários está vazia.")


def test(): 
    assert calcula_classe_social([], 1000) is None
    assert calcula_classe_social([1000], 1000) == "E"
    assert calcula_classe_social([500], 1000) == "E"
    assert calcula_classe_social([500], 1000) == "E"
    assert calcula_classe_social([1000, 0], 900) == "E"
    assert calcula_classe_social([1000], 900) == "D"
    assert calcula_classe_social([10000, 15000], 1000) == "B"
    assert calcula_classe_social([20000, 25000], 1000) == "A"
    assert calcula_classe_social([20000, 0, 0, 0, 0], 1000) == "C"
