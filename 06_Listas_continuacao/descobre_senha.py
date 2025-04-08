segredo = 5
tentativas = 1
palpite = int(input('Digite o seu palpite de segredo: '))

while palpite != segredo:
    print('Errado, tente novamente!')
    tentativas += 1
    palpite = int(input('Tente adivinhar o número novamente: '))

print('Parabéns você acertou o segredo em ', tentativas, 'tentativas!')
