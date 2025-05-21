def advinha_senha(numero_sorteado, palpites):
    respostas = []
    tentativas = 3  # Número máximo de tentativas

    for tentativa, palpite in enumerate(palpites[:tentativas], 1):
        if palpite == numero_sorteado:
            respostas.append(f"Parabéns! Você acertou o número {numero_sorteado} na tentativa {tentativa}.")
            break
        elif palpite < numero_sorteado:
            respostas.append("O número sorteado é MAIOR do que o seu palpite.")
        else:
            respostas.append("O número sorteado é MENOR do que o seu palpite.")
    else:
        respostas.append(f"Suas tentativas acabaram! O número sorteado era {numero_sorteado}.")

    return respostas  

def test():
    numero_sorteado = 7  # Definindo a variável corretamente
    palpites = [3, 8, 7]  # Palpites fornecidos
    resultado = advinha_senha(numero_sorteado, palpites)

    assert resultado[0] == "O número sorteado é MAIOR do que o seu palpite."
    assert resultado[1] == "O número sorteado é MENOR do que o seu palpite."
    assert resultado[2] == "Parabéns! Você acertou o número 7 na tentativa 3."
