from datetime import date, timedelta
import calendar 

# Crie método que recebe uma string (mm-dd-aaaa) e retorna uma data
def str_to_date(date_str):
    try:
        day, month, year = date_str.split('-')
        return date(int(year), int(month), int(day))
    except (ValueError, AttributeError):
        return None

def test_str_to_date():
    assert str_to_date('01-10-2025') == date(year=2025, month=10, day=1) 
    assert str_to_date('99-10-2025') is None


# O nome do dia da semana (“sábado”, “domingo”, …)
def nome_dia_semana(data):
    dias = [ 
        "segunda-feira",
        "terça-feira",
        "quarta-feira",
        "quinta-feira",
        "sexta-feira",
        "sábado",
        "domingo"
    ]
    return dias[data.weekday()]
    
def test_nome_dia_semana():
    assert nome_dia_semana(date(year=2025, month=1, day=1)) == 'quarta-feira'
    assert nome_dia_semana(date(year=2025, month=1, day=2)) == 'quinta-feira'


# Quantos dias faltam para o final de semana
def dias_para_finde(data):
    dia_semana = data.weekday()
    if dia_semana >= 5:
        return 0
    else:
        return 5 - dia_semana

def test_dias_para_finde():
    assert dias_para_finde(date(year=2025, month=1, day=1)) == 3
    assert dias_para_finde(date(year=2025, month=1, day=2)) == 2


# Quantos dias existem entre a data e hoje
def delta_dias(data_a, data_b):
    return (data_b - data_a).days 
    
def test_delta_dias():
    assert delta_dias(date(year=2025, month=1, day=1), date(year=2026, month=1, day=2)) == 366
    assert delta_dias(date(year=2026, month=1, day=1), date(year=2025, month=1, day=2)) == -364 
    assert delta_dias(date(year=2025, month=1, day=1), date(year=2025, month=1, day=2)) == 1


# O mesmo dia no próximo mês (ou o anterior próximo)
def proximo_mes(data_a):
    ano = data_a.year
    mes = data_a.month + 1

    if mes > 12:
        mes = 1
        ano += 1

    _, ultimo_dia_prox_mes = calendar.monthrange(ano, mes)

    dia = min(data_a.day, ultimo_dia_prox_mes)

    return date(ano, mes, dia)

def test_proximo_mes():
    assert proximo_mes(date(year=2025, month=1, day=1)) == date(year=2025, month=2, day=1)
    assert proximo_mes(date(year=2025, month=1, day=29)) == date(year=2025, month=2, day=28)
    assert proximo_mes(date(year=2024, month=1, day=29)) == date(year=2024, month=2, day=29)
    assert proximo_mes(date(year=2025, month=1, day=30)) == date(year=2025, month=2, day=28)


# 1 se esta data está no futuro, -1 se no passado ou 0 se for hoje.
def data_futuro(data: date) -> str:
    hoje = date.today()
    if data > hoje:
        return 1
    elif data < hoje:
        return -1
    else:
        return 0

def test_data_futuro():
    assert data_futuro(date(day=1, month=1, year=2099)) == 1
    assert data_futuro(date(day=1, month=1, year=1999)) == -1
    assert data_futuro(date.today()) == 0
