"""
Meses sao representados como: 1=Jan, 2=Feb, 3=Mar..

"""

MESES_31_DIAS = [1, 3, 5, 7, 8, 10, 12]
MESES_30_DIAS = [4, 6, 9, 11]


def eh_bissexto(ano: int) -> bool:
    if ano % 400 == 0:
        return True
    if ano % 100 == 0:
        return False
    if ano % 4 == 0:
        return True
    return False

def test():
    assert eh_bissexto(2000) == True
    assert eh_bissexto(1900) == False
    assert eh_bissexto(2024) == True
    assert eh_bissexto(2023) == False

def total_dias_no_mes(mes: int, ano: int) -> int:
    if mes in MESES_31_DIAS:
        return 31
    if mes in MESES_30_DIAS:
        return 30
    if eh_bissexto(ano):
        return 29
    return 28

def test():
    assert total_dias_no_mes(1, 2024) == 31
    assert total_dias_no_mes(2, 2024) == 29
    assert total_dias_no_mes(3, 2024) == 31
    assert total_dias_no_mes(11, 2024) == 30


def formata_data(data: list) -> str:
    return f"{data[0]}/{data[1]}/{data[2]}"

def test():
    assert formata_data([1, 2, 2024]) == "1/2/2024"
    assert formata_data([1, 12, 2024]) == "1/12/2024"

def dias_ate(data: list) -> list:
    dia, mes, ano = data
    total = 0

    for a in range(1, ano):
        total += 366 if eh_bissexto(a) else 365
    for m in range(1, mes):
        total += total_dias_no_mes(m, ano)
    total += dia
    return total


def calcula_diferenca(data1: list, data2: list) -> int:
    return abs(dias_ate(data2) - dias_ate(data1))

def test():
    # Diferenca em dias entre 2/7/2004 e 27/5/2024 é de 7268 dias
    assert calcula_diferenca([2, 7, 2004], [27, 5, 2024]) == 7269
    # Diferenca entre 27/5/2024 e 2/7/2089 é de 23779 dias
    assert calcula_diferenca([27, 5, 2024], [2, 7, 2004 + 85]) == 23777
    # Diferenca entre 2/7/2004 e 2/7/2089 é de 31047 dias
    assert calcula_diferenca([2, 7, 2004], [2, 7, 2004 + 85]) == 31046
    # A data 27/5/2024 representa 23.409669211195926% entre 2/7/2004 e 2/7/2089
    # Diferenca em dias entre 24/7/1991 e 24/10/2024 é de 12146 dias
    assert calcula_diferenca([24, 7, 1991], [24, 10, 2024]) == 12146
    # Diferenca entre 24/10/2024 e 24/7/2076 é de 18900 dias
    assert calcula_diferenca([24, 10, 2024], [24, 7, 1991 + 85]) == 18901
    # Diferenca entre 24/7/1991 e 24/7/2076 é de 31046 dias
    assert calcula_diferenca([24, 7, 1991], [24, 7, 1991 + 85]) == 31047
    # A data 24/10/2024 representa 39.12259228241963% entre 24/7/1991 e 24/7/2076
