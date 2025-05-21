def caesar_cipher(texto, desvio):
    resultado = []

    for char in texto:
        codigo = ord(char)
        if 65 <= codigo <= 90:
            deslocado = (codigo - 65 + desvio) % 26 + 65
            resultado.append(chr(deslocado))
        elif 97 <= codigo <= 122:
            deslocado = (codigo - 97 + desvio) % 26 + 97
            resultado.append(chr(deslocado))
        else:
            resultado.append(char)
    
    return ''.join(resultado)

def test():
    assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"
    assert caesar_cipher("Khoor, Zruog!", -3) == "Hello, World!"
    assert caesar_cipher("Matheus Jardim", 3) == "Pdwkhxv Mduglp"
    assert caesar_cipher("Pdwkhxv Mduglp", -3) == "Matheus Jardim"
    assert caesar_cipher(caesar_cipher("Atitus", 3), -3) == "Atitus"


print (caesar_cipher("Hello, World", 3))
