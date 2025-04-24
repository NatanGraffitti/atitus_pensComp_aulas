def real_para_dolar(valor, tx_conversao):
    return round(valor / tx_conversao, 2)

def test():
    assert real_para_dolar(500, 5.20) == 96.23 
    assert real_para_dolar(500, 1) == 500
    assert real_para_dolar(500, 6) == 83.33
