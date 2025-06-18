from datetime import date
import calendar

def parcelamento(valor, parcelas, dt_venda):
    if parcelas <= 0:
        return []
    
    valor_base = valor // parcelas
    resto = valor % parcelas
    resultado = []
    
    for i in range(parcelas):
        valor_parcela = valor_base + (resto if i == parcelas - 1 else 0)
        
        if i == 0:
            data_venc = dt_venda
        else:
            ano = dt_venda.year
            mes = dt_venda.month + i
            
            while mes > 12:
                mes -= 12
                ano += 1
            
            _, ultimo_dia = calendar.monthrange(ano, mes)
            data_venc = date(ano, mes, ultimo_dia)
        
        resultado.append([valor_parcela, data_venc])
    
    return resultado

def test():
    dt_venda = date(2025, 1, 28)
    assert parcelamento(100, 1, dt_venda) == [[100, dt_venda]]
    assert parcelamento(100, 2, dt_venda) == [
        [50, dt_venda],
        [50, date(2025, 2, 28)]
    ]
    assert parcelamento(100, 3, dt_venda) == [
        [33, dt_venda],
        [33, date(2025, 2, 28)],
        [34, date(2025, 3, 31)]
    ]
    assert parcelamento(100, 4, dt_venda) == [
        [25, dt_venda],
        [25, date(2025, 2, 28)],
        [25, date(2025, 3, 31)],
        [25, date(2025, 4, 30)]
    ]
    assert parcelamento(100, 6, dt_venda) == [
        [16, dt_venda],
        [16, date(2025, 2, 28)],
        [16, date(2025, 3, 31)],
        [16, date(2025, 4, 30)],
        [16, date(2025, 5, 31)],
        [20, date(2025, 6, 30)]
    ]
