def letra_em_texto(texto, letra):
    for char in texto:
        if char == letra:
            return True
    return False

def conta_letra_em_texto(texto, letra):
     contador = 0
    for char in texto:
        if char == letra:
            contador += 1
    return contador

def texto_sem_letra(texto, letra):
   novo_texto = ""
    for char in texto:
        if char != letra:
            novo_texto += char
    return novo_texto

def texto_com_letra_upper(texto, letra):
    novo_texto = ""
    for char in texto:
        if char == letra:
            novo_texto += char.upper()
        else:
            novo_texto += char
    return novo_texto

def test():
    assert letra_em_texto("Pensamento Computacional", "a")
    assert letra_em_texto("Pensamento Computacional", " ")
    assert not letra_em_texto("Pensamento Computacional", "A")
    assert not letra_em_texto("Pensamento Computacional", "c")

    assert conta_letra_em_texto("Pensamento Computacional", "a") == 3
    assert conta_letra_em_texto("Pensamento Computacional", "A") == 0
    assert conta_letra_em_texto("Pensamento Computacional", "e") == 2

    assert texto_sem_letra("Pensamento Computacional", "a") == "Pensmento Computcionl"
    assert texto_sem_letra("Pensamento Computacional", "z") == "Pensamento Computacional"
    assert texto_sem_letra("Pensamento Computacional", " ") == "PensamentoComputacional"

    assert (
        texto_com_letra_upper("Pensamento Computacional", "a") == "PensAmento ComputAcionAl"
    )
    assert (
        texto_com_letra_upper("Pensamento Computacional", "z") == "Pensamento Computacional"
    )
    assert (
        texto_com_letra_upper("Pensamento Computacional", " ") == "Pensamento Computacional"
    )
