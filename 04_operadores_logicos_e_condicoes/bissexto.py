def eh_bissexto(ano): #função que se o ano for divisível por 4 retorna que o ano é bissexto
    if ano % 4 == 0:
        return True #(com alterações nos asserts poderia retornar como uma resposta de Bissexto ou não bissexto)
        print ("Bissexto")
    else:
        return False
        print ("Não bissexto")
        
def proximo_bissexto(ano): #return (ano + 3) // 4 * 4 -> solução em uma linha da correção em aula
    if ano % 4 == 0:
        return ano
    if ano % 4 == 1:
        return ano + 3
    if ano % 4 == 2:
        return ano + 2
    if ano % 4 == 3:
        return ano + 1

def test():
    assert eh_bissexto(0)
    assert eh_bissexto(2020)
    assert eh_bissexto(2024)

    assert not eh_bissexto(1)
    assert not eh_bissexto(2022)
    assert not eh_bissexto(2023)

    assert proximo_bissexto(2024) == 2024
    assert proximo_bissexto(2025) == 2028
    assert proximo_bissexto(2029) == 2032
    assert proximo_bissexto(2020) == 2020

print (eh_bissexto(20))
print (proximo_bissexto(23))
