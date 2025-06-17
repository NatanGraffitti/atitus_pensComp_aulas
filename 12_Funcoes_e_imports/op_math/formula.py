def formula(a, b):
    soma = adicao(a, b)          # a + b sem usar '+'
    diferenca = subtracao(a, b)  # a - b sem usar '-'
    produto = multiplicacao(soma, diferenca)  # (a + b) * (a - b) sem '*'
    resultado = divisao(produto, 2)            # divide por 2 sem '/'
    return resultado
