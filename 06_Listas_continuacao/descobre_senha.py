segredo = 5
tentativas = 0
palpites = [3, 8, 5]  # Lista de palpites predefinidos

for palpite in palpites:
    tentativas += 1
    if palpite == segredo:
        print('Parabéns você acertou o segredo em', tentativas, 'tentativas!')
        break  # Sai do loop quando o palpite correto é encontrado
    else:
        print('Errado, tente novamente!')

if palpite != segredo:
    print('Você não acertou o número secreto.')
