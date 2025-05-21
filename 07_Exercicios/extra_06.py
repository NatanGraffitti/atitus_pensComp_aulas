def valor_pgto(valor, forma_pgto):
    if forma_pgto == 1:
        resultado = valor - (valor * (15 / 100))
        print(f"Valor com desconto de 15%: {resultado}")
        return resultado
    elif forma_pgto == 2:
        resultado = valor - (valor * (10 / 100))
        print(f"Valor com desconto de 10%: {resultado}")
        return resultado
    elif forma_pgto == 3:
        print(f"Parcelado em 2x sem juros. Valor total {valor}")
        return valor
    elif forma_pgto == 4:
        resultado = valor + (valor * (10 / 100))
        print(f"Valor com acréscimo de 10%: {resultado}")
        return resultado
    else:
        print("Opção inválida. Por favor, escolha uma das opções listadas.")
        return None

# Função de teste
def test():
    assert valor_pgto(100, 1) == 85
    assert valor_pgto(100, 2) == 90
    assert valor_pgto(100, 3) == 100
    assert valor_pgto(100, 4) == 110
    print("Todos os testes passaram.")

valor_pgto(100, 2)
