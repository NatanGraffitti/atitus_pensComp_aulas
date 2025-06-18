def soma_str(param: str) -> int:
    """
    Soma todos os dígitos numéricos encontrados em uma string,
    ignorando outros caracteres e sinais.

    Args:
        param (str): A string de entrada que pode conter dígitos e outros caracteres.

    Returns:
        int: A soma de todos os dígitos encontrados na string.
    """
    total_sum = 0
    for char in param:
        if char.isdigit():
            total_sum += int(char)
    return total_sum

def test():
    assert soma_str("") == 0
    assert soma_str("a") == 0
    assert soma_str("4") == 4
    assert soma_str("5ab6") == 11  # 5+6
    assert soma_str("3 -4 z5") == 12  # 3+4+5, ignora o sinal e o espaço
    assert soma_str("11a2z3") == 7  # 1+1+2+3

print("Todos os testes passaram com sucesso!")
