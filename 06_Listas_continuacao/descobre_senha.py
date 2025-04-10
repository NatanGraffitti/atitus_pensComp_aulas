def segredo(valor):
    if valor < 0 or valor > 10:
        return False
    tentativas = 1
    while (valor):
        numero = int(input('digite um numero entre 0 e 10:'))
        if numero < 0 or numero > 10:
            print('Valor invalido, tente novamente')
        if numero == valor:
            print('Segredo descoberto', tentativas, 'tentativas')
            return True
        tentativas += 1



print(segredo(0))
