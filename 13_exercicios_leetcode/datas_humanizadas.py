MINUTO = 60
HORA = 60 * MINUTO

def data_humanizada(duracao: int) -> str:
    horas = duracao // HORA
    resto = duracao % HORA
    minutos = resto // MINUTO
    segundos = resto % MINUTO

    partes = []
    if horas > 0:
        partes.append(f"{horas} hora" + ("s" if horas > 1 else ""))
    if minutos > 0:
        partes.append(f"{minutos} minuto" + ("s" if minutos > 1 else ""))
    if segundos > 0 or (horas == 0 and minutos == 0):
        partes.append(f"{segundos} segundo" + ("s" if segundos != 1 else ""))
    return " ".join(partes)

def test():
    assert data_humanizada(10) == "10 segundos"
    assert data_humanizada(1 * MINUTO) == "1 minuto"
    assert data_humanizada(2 * MINUTO) == "2 minutos"
    assert data_humanizada(2 * MINUTO + 20) == "2 minutos 20 segundos"
    assert data_humanizada(2 * HORA + 3 * MINUTO + 20) == "2 horas 3 minutos 20 segundos"
