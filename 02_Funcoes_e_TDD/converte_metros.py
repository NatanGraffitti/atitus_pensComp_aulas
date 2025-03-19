def metro_para_centimetro(valor):
    return valor * 100


def centimetro_para_metro(valor):
    return valor / 100


    assert metro_para_centimetro(1) == 100
    assert metro_para_centimetro(10) == 1000
    assert metro_para_centimetro(0) == 0
    
    assert centimetro_para_metro(100) == 1
    assert centimetro_para_metro(1000) == 10
    assert centimetro_para_metro(0) == 0

print("Terminou com sucesso!")
