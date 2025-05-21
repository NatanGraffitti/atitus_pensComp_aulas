def multiplica_matrix_scalar(matrix, scalar):
    resultado = []
    for linha in matrix:
        resultado_linha = []
        for elemento in linha:
            resultado_linha.append(elemento * scalar)
        resultado.append(resultado_linha)
    return resultado

matrix = [[1, 2], [3, 4]]
scalar = 2
result = multiplica_matrix_scalar(matrix, scalar)
print(result)


def test():
    matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result_01 = [[3, 6, 9], [12, 15, 18], [21, 24, 27]]
    assert multiplica_matrix_scalar(matrix_1, 3) == result_01  # Corrigido o nome da função

    matrix_02 = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
    result_02 = [[8, 12, 16], [20, 24, 28], [32, 36, 40]]
    assert multiplica_matrix_scalar(matrix_02, 4) == result_02  # Corrigido o nome da função


