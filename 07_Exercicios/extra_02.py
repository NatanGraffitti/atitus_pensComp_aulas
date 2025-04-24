# Função que encontra o maior número de uma lista
def maior_numero(lista):
    maior = lista[0]  
    for num in lista:
        if num > maior:  
            maior = num
    return maior

# Função que encontra o menor número de uma lista
def menor_numero(lista):
    menor = lista[0]  
    for num in lista:
        if num < menor:  
            menor = num
    return menor

# Função que encontra os números pares de uma lista
def numeros_pares(lista):
    pares = []  
    for num in lista:
        if num % 2 == 0:  
            pares.append(num)
    return pares

# Função que encontra os números ímpares de uma lista
def numeros_impares(lista):
    impares = []  
    for num in lista:
        if num % 2 != 0: 
            impares.append(num)
    return impares

# Função que encontra os números positivos de uma lista
def numeros_positivos(lista):
    positivos = []  
    for num in lista:
        if num >= 0: 
            positivos.append(num)
    return positivos

# Função que encontra os números negativos de uma lista
def numeros_negativos(lista):
    negativos = []  
    for num in lista:
        if num < 0: 
            negativos.append(num)
    return negativos

# Função que calcula a soma de todos os números da lista
def soma_numeros(lista):
    soma = 0  
    for num in lista:
        soma += num  
    return soma

def test():
    lista_1 = [10, 0, -3, 42, 5, -6, 8, 91]
    lista_2 = [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
    lista_3 = [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]
    
    # Teste para maior_numero
    print(maior_numero(lista_1))  # Esperado: 91
    print(maior_numero(lista_2))  # Esperado: 95
    print(maior_numero(lista_3))  # Esperado: 92

    # Teste para menor_numero
    print(menor_numero(lista_1))  # Esperado: -6
    print(menor_numero(lista_2))  # Esperado: 2
    print(menor_numero(lista_3))  # Esperado: 5

    # Teste para numeros_pares
    print(numeros_pares(lista_1))  # Esperado: [10, 0, 42, -6, 8]
    print(numeros_pares(lista_2))  # Esperado: [20, 2, 74, 22]
    print(numeros_pares(lista_3))  # Esperado: [92, 50, 28]

    # Teste para numeros_impares
    print(numeros_impares(lista_1))  # Esperado: [-3, 5, 91]
    print(numeros_impares(lista_2))  # Esperado: [27, 19, 85, 3, 95, 11]
    print(numeros_impares(lista_3))  # Esperado: [45, 23, 17, 89, 57, 15, 5]

    # Teste para numeros_positivos
    print(numeros_positivos(lista_1))  # Esperado: [10, 0, 42, 5, 8, 91]
    print(numeros_positivos(lista_2))  # Esperado: [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
    print(numeros_positivos(lista_3))  # Esperado: [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]

    # Teste para numeros_negativos
    print(numeros_negativos(lista_1))  # Esperado: [-3, -6]
    print(numeros_negativos(lista_2))  # Esperado: []
    print(numeros_negativos(lista_3))  # Esperado: []

    # Teste para soma_numeros
    print(soma_numeros(lista_1))  # Esperado: 147
    print(soma_numeros(lista_2))  # Esperado: 358
    print(soma_numeros(lista_3))  # Esperado: 421
