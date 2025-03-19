def hora_para_minuto(valor):
    return valor * 60

def minuto_para_segundo(valor):
    return valor * 60

def hora_para_segundo(valor):
    return hora_para_minuto(valor * 60)

def dia_para_segundo(valor):
    return dia_para_segundo(valor * 24 * 60 * 60)

def dia_para_horas(valor):
    return dia_para_horas(valor * 24)


    assert hora_para_minuto(0) == 0
    assert hora_para_minuto(1) == 60
    assert hora_para_minuto(2) == 120
    
    assert minuto_para_segundo(0) == 0
    assert minuto_para_segundo(1) == 60
    assert minuto_para_segundo(2) == 120
    
    assert hora_para_segundo(0) == 0
    assert hora_para_segundo(1) == 3600  # 1 * 60 * 60
    assert hora_para_segundo(2) == 7200  # 2 * 60 * 60
    
    assert dia_para_segundo(0) == 0
    assert dia_para_segundo(1) == 86400
    assert dia_para_segundo(2) == 172800
    
    assert dia_para_horas(0) == 0
    assert dia_para_horas(1) == 24
    assert dia_para_horas(2) == 48

print("Terminou com sucesso!")
