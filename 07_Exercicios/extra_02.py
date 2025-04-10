def maior_numero(lista):
    maior = lista[0]

    for num in lista[1:]:
        if num > maior:
            maior = num
    return maior

def menor_numero(lista):
    menor = lista[0]

    for num in lista[1:]:
        if num < menor:
            menor = num
    return menor

def numeros_pares(lista):
     pares = []
    for numero in lista:
        if numero % 2 == 0: 
            pares.append(numero)
    return pares

def numeros_impares(lista):
    impares = []
    for numero in lista:
        if numero % 2 != 0: 
            impares.append(numero)
    return impares

def numeros_positivo(lista):
    positivos = []
    for numero in lista:
        if numero >= 0: 
            positivos.append(numero)
    return positivos

def numeros_negativos(lista):
    negativos = []
    for numero in lista:
        if numero < 0: 
            negativos.append(numero)
    return negativos

def soma_numeros(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

def test():
    lista_1 = [10, 0, -3, 42, 5, -6, 8, 91]
    lista_2 = [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
    lista_3 = [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]
    assert maior_numero(lista_1) == 91
    assert maior_numero(lista_2) == 95
    assert maior_numero(lista_3) == 92

    assert menor_numero(lista_1) == -6
    assert menor_numero(lista_2) == 2
    assert menor_numero(lista_3) == 5

    assert numeros_pares(lista_1) == [10, 0, 42, -6, 8]
    assert numeros_pares(lista_1) == [20, 2, 74, 22]
    assert numeros_pares(lista_1) == [92, 50, 28]

    assert numeros_impares(lista_1) == [-3, 5, 91]
    assert numeros_impares(lista_1) == [27, 19, 85, 3, 95, 11]
    assert numeros_impares(lista_1) == [45, 23, 17, 89, 57, 15, 5]

    assert numeros_positivo(lista_1) == [10, 0, 42, 5, 8, 91]
    assert numeros_positivo(lista_1) == [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
    assert numeros_positivo(lista_1) == [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]

    assert numeros_negativos(lista_1) == [-3, -6]
    assert numeros_negativos(lista_1) == []
    assert numeros_negativos(lista_1) == []

    assert soma_numeros(lista_1) == 147
    assert soma_numeros(lista_1) == 358
    assert soma_numeros(lista_1) == 421
